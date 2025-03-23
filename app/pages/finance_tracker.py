import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
import os

def show():
    st.title("Finance Tracker")
    
    # Define tabs for different financial management features
    tab1, tab2, tab3 = st.tabs(["Monthly Overview", "Track Expenses", "Budget Planning"])
    
    # Load or initialize expense data
    if 'expenses' not in st.session_state:
        # Try to load from file, or create new if file doesn't exist
        try:
            with open('data/expenses.json', 'r') as f:
                st.session_state.expenses = json.load(f)
        except:
            # Default empty expense data structure
            st.session_state.expenses = {
                'transactions': [],
                'categories': ["Food", "Rent", "Utilities", "Textbooks", "Entertainment", "Transportation", "Other"]
            }
    
    # Define expense categories and a default month
    categories = st.session_state.expenses['categories']
    current_month = datetime.now().strftime('%Y-%m')
    
    # Monthly Overview Tab
    with tab1:
        st.header("Monthly Expense Overview")
        
        # Month selector
        selected_month = st.selectbox(
            "Select Month", 
            [datetime.now().replace(month=i).strftime('%Y-%m') for i in range(1, 13)],
            index=[datetime.now().replace(month=i).strftime('%Y-%m') for i in range(1, 13)].index(current_month)
        )
        
        # Filter transactions for the selected month
        month_transactions = [t for t in st.session_state.expenses['transactions'] 
                            if t['date'].startswith(selected_month)]
        
        # Calculate total expenses for the month
        total = sum(t['amount'] for t in month_transactions)
        
        # Display key metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Expenses", f"₹{total:.2f}")
        
        # Only show average daily and category breakdown if there are transactions
        if month_transactions:
            # Calculate average daily expense
            days_in_month = 30  # Simplified
            with col2:
                st.metric("Average Daily", f"₹{total/days_in_month:.2f}")
            
            # Calculate largest category
            category_totals = {}
            for t in month_transactions:
                category_totals[t['category']] = category_totals.get(t['category'], 0) + t['amount']
            
            largest_category = max(category_totals.items(), key=lambda x: x[1]) if category_totals else ("None", 0)
            with col3:
                st.metric("Largest Expense", f"{largest_category[0]}: ₹{largest_category[1]:.2f}")
            
            # Create dataframe for plotting
            expense_by_category = pd.DataFrame([
                {"Category": cat, "Amount": category_totals.get(cat, 0)} 
                for cat in categories
            ])
            
            # Pie chart for expense breakdown
            st.subheader("Expense Breakdown")
            fig = px.pie(
                expense_by_category, 
                values='Amount', 
                names='Category',
                title="Spending by Category",
                hole=0.4  # Create a donut chart
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Bar chart for daily expenses over time
            daily_expenses = {}
            for t in month_transactions:
                day = t['date']
                daily_expenses[day] = daily_expenses.get(day, 0) + t['amount']
            
            daily_df = pd.DataFrame([
                {"Date": day, "Amount": amount} 
                for day, amount in daily_expenses.items()
            ])
            daily_df = daily_df.sort_values("Date")
            
            st.subheader("Daily Spending")
            fig2 = px.bar(
                daily_df, 
                x="Date", 
                y="Amount",
                title="Daily Expenses"
            )
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.info("No transactions recorded for this month. Add some expenses to see your financial breakdown.")
    
    # Track Expenses Tab
    with tab2:
        st.header("Add New Expenses")
        
        # Form for adding new expenses
        with st.form("expense_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                description = st.text_input("Description")
                amount = st.number_input("Amount (₹)", min_value=0.0, step=10.0)
                
            with col2:
                category = st.selectbox("Category", categories)
                expense_date = st.date_input("Date", datetime.now())
            
            submitted = st.form_submit_button("Add Expense")
            
            if submitted and description and amount > 0:
                # Add new transaction
                new_transaction = {
                    'description': description,
                    'amount': amount,
                    'category': category,
                    'date': expense_date.strftime('%Y-%m-%d')
                }
                st.session_state.expenses['transactions'].append(new_transaction)
                
                # Save to file (create directory if it doesn't exist)
                try:
                    os.makedirs('data', exist_ok=True)
                    with open('data/expenses.json', 'w') as f:
                        json.dump(st.session_state.expenses, f)
                    st.success(f"Added expense: {description} (₹{amount:.2f})")
                except Exception as e:
                    st.error(f"Error saving expense: {e}")
                
        # Display recent transactions
        st.subheader("Recent Transactions")
        if st.session_state.expenses['transactions']:
            # Show the most recent 10 transactions
            recent = sorted(st.session_state.expenses['transactions'], 
                           key=lambda x: x['date'], reverse=True)[:10]
            
            for i, t in enumerate(recent):
                col1, col2, col3 = st.columns([3, 1, 1])
                with col1:
                    st.write(f"**{t['description']}** ({t['category']})")
                with col2:
                    st.write(f"₹{t['amount']:.2f}")
                with col3:
                    st.write(t['date'])
                
                # Add delete button for each transaction
                if st.button("Delete", key=f"del_{i}"):
                    st.session_state.expenses['transactions'].remove(t)
                    # Save updated expenses
                    try:
                        with open('data/expenses.json', 'w') as f:
                            json.dump(st.session_state.expenses, f)
                        st.success("Transaction deleted")
                        st.experimental_rerun()
                    except Exception as e:
                        st.error(f"Error deleting transaction: {e}")
                
                st.divider()
        else:
            st.info("No transactions recorded yet. Add some expenses to track your spending.")
    
    # Budget Planning Tab
    with tab3:
        st.header("Budget Planning")
        
        # Budget setup section
        st.subheader("Set Monthly Budget")
        
        # Load or initialize budget data
        if 'budget' not in st.session_state:
            try:
                with open('data/budget.json', 'r') as f:
                    st.session_state.budget = json.load(f)
            except:
                # Default empty budget with float values
                st.session_state.budget = {
                    'monthly_total': 1000.0,  # Changed to float
                    'categories': {cat: 0.0 for cat in categories}  # Changed to float
                }
        
        # Budget form
        with st.form("budget_form"):
            # Overall monthly budget
            monthly_budget = st.number_input(
                "Total Monthly Budget (₹)", 
                min_value=0.0,  # Changed to float
                value=float(st.session_state.budget['monthly_total']),  # Convert to float
                step=100.0,  # Updated step for Rupees
                format="%.2f"  # Add format to show 2 decimal places
            )
            
            st.subheader("Category Allocation")
            
            # Category budgets
            category_budgets = {}
            cols = st.columns(2)
            for i, category in enumerate(categories):
                with cols[i % 2]:
                    category_budgets[category] = st.number_input(
                        f"{category} Budget (₹)",
                        min_value=0.0,  # Changed to float
                        value=float(st.session_state.budget['categories'].get(category, 0)),  # Convert to float
                        step=100.0,  # Updated step for Rupees
                        format="%.2f"  # Add format to show 2 decimal places
                    )
            
            submitted = st.form_submit_button("Save Budget")
            
            if submitted:
                # Update budget
                st.session_state.budget['monthly_total'] = monthly_budget
                st.session_state.budget['categories'] = category_budgets
                
                # Save to file
                try:
                    os.makedirs('data', exist_ok=True)
                    with open('data/budget.json', 'w') as f:
                        json.dump(st.session_state.budget, f)
                    st.success("Budget updated successfully!")
                except Exception as e:
                    st.error(f"Error saving budget: {e}")
        
        # Budget tracker - compare actual spending vs budget
        st.subheader("Budget Tracker")
        
        # Month selector for budget tracking
        budget_month = st.selectbox(
            "Select Month for Budget Tracking", 
            [datetime.now().replace(month=i).strftime('%Y-%m') for i in range(1, 13)],
            index=[datetime.now().replace(month=i).strftime('%Y-%m') for i in range(1, 13)].index(current_month),
            key="budget_month_select"
        )
        
        # Filter transactions for the selected month
        budget_transactions = [t for t in st.session_state.expenses['transactions'] 
                              if t['date'].startswith(budget_month)]
        
        # Calculate spending by category
        spending_by_category = {}
        for t in budget_transactions:
            spending_by_category[t['category']] = spending_by_category.get(t['category'], 0) + t['amount']
        
        # Calculate total spending
        total_spending = sum(spending_by_category.values())
        
        # Display budget progress
        st.metric(
            "Monthly Budget Progress", 
            f"₹{total_spending:.2f} / ₹{st.session_state.budget['monthly_total']:.2f}",
            f"₹{total_spending - st.session_state.budget['monthly_total']:.2f}" if total_spending > st.session_state.budget['monthly_total'] else None,
            delta_color="inverse"
        )
        
        # Progress bar for overall budget
        progress = min(total_spending / st.session_state.budget['monthly_total'], 1) if st.session_state.budget['monthly_total'] > 0 else 0
        st.progress(progress)
        
        # Budget vs actual by category
        st.subheader("Budget vs. Actual by Category")
        
        budget_comparison = []
        for category in categories:
            budget_amount = st.session_state.budget['categories'].get(category, 0)
            spent_amount = spending_by_category.get(category, 0)
            budget_comparison.append({
                "Category": category,
                "Budget": budget_amount,
                "Spent": spent_amount,
                "Remaining": budget_amount - spent_amount
            })
        
        budget_df = pd.DataFrame(budget_comparison)
        
        # Horizontal bar chart comparing budget vs actual
        fig = go.Figure()
        fig.add_trace(go.Bar(
            y=budget_df["Category"],
            x=budget_df["Budget"],
            name="Budget",
            orientation='h',
            marker=dict(color='rgba(58, 71, 80, 0.6)')
        ))
        fig.add_trace(go.Bar(
            y=budget_df["Category"],
            x=budget_df["Spent"],
            name="Actual",
            orientation='h',
            marker=dict(color='rgba(246, 78, 139, 0.6)')
        ))
        
        fig.update_layout(
            title="Budget vs. Actual Spending by Category",
            barmode='group',
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Tips based on spending
        st.subheader("Money-Saving Tips")
        
        # Generate personalized tips based on spending patterns
        if total_spending > 0:
            highest_category = max(spending_by_category.items(), key=lambda x: x[1])[0]
            
            if highest_category == "Food":
                st.info("💡 **Tip**: Your highest expense is food. Consider using mess facilities or cooking with roommates to share costs.")
            elif highest_category == "Entertainment":
                st.info("💡 **Tip**: Look for student discounts and use platforms like PayTM, PhonePe for entertainment booking offers.")
            elif highest_category == "Transportation":
                st.info("💡 **Tip**: Consider using metro/local trains with student passes or share auto/cab rides with classmates.")
            elif highest_category == "Textbooks":
                st.info("💡 **Tip**: Check for second-hand books in local shops or online marketplaces like OLX or Amazon.")
            else:
                st.info("💡 **Tip**: Use UPI payments and track expenses through digital wallets to better manage your spending.")
        else:
            st.info("💡 **Tip**: Start tracking your expenses regularly to identify areas where you can save money.") 