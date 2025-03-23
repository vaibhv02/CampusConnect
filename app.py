import streamlit as st
from app.pages import home, study_planner, smart_tutor, campus_events, career_guidance, finance_tracker
import streamlit.components.v1 as components

# Configure page
st.set_page_config(
    page_title="Campus Connect",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    /* Main content background */
    .main {
        background-color: #f8f9fa;
    }
    
    /* Header styling */
    .stApp header {
        background-color: #4285F4;
    }
    
    /* General text colors */
    .st-emotion-cache-16idsys {
        color: #000000;
    }
    .st-emotion-cache-183lzff {
        color: #000000;
    }
    .st-emotion-cache-10trblm {
        color: #000000;
    }
    p, h1, h2, h3, h4, h5, h6, ol, ul, li {
        color: #000000 !important;
    }
    
    /* Button styling - ensure text is visible */
    .stButton button {
        color: white !important;
        background-color: #4285F4 !important;
        border: none !important;
    }
    
    /* Make all form buttons more visible */
    button[kind="primaryFormSubmit"] {
        color: white !important;
        background-color: #4285F4 !important;
    }
    
    /* Sidebar styling */
    .st-emotion-cache-16txtl3, .st-emotion-cache-ue6h4q, .st-emotion-cache-1y4p8pa,
    .st-emotion-cache-16txtl3 p, .st-emotion-cache-ue6h4q p, .st-emotion-cache-1y4p8pa p,
    .st-emotion-cache-16txtl3 h1, .st-emotion-cache-16txtl3 h2, .st-emotion-cache-16txtl3 h3,
    .st-emotion-cache-16txtl3 a {
        color: white !important;
    }
    
    /* Improve radio button contrast in sidebar */
    .st-emotion-cache-1inwz65 {
        color: white !important;
    }
    
    /* Calendar buttons and event buttons */
    .stExpander button, .stContainer button {
        color: white !important;
        background-color: #4285F4 !important;
    }
    
    /* Radio buttons text */
    .st-emotion-cache-pkbazv {
        color: black !important;
    }
    
    /* General button hover effect */
    .stButton button:hover {
        background-color: #3B78E7 !important;
    }

    /* Dropdown menu styling - updated with darker colors */
    .stSelectbox option {
        color: white !important;
        background-color: #2c3e50 !important;
    }
    
    /* More specific dropdown selectors - updated with darker colors */
    .st-emotion-cache-1v0mbdj, 
    div[data-baseweb="select"] ul,
    div[data-baseweb="select"] ul li,
    div[data-baseweb="select"] div,
    div[data-baseweb="popover"] ul,
    div[data-baseweb="popover"] ul li,
    div[data-baseweb="popover"] div,
    div[data-testid="stSelectbox"] ul,
    div[data-testid="stSelectbox"] li,
    [role="listbox"],
    [role="option"] {
        background-color: #2c3e50 !important;
        border-radius: 4px !important;
    }
    
    /* Text within dropdown options */
    div[data-baseweb="select"] ul li span,
    div[data-baseweb="select"] div span,
    div[data-baseweb="popover"] ul li span,
    div[data-baseweb="popover"] div span,
    div[data-testid="stSelectbox"] li span,
    [role="listbox"] span,
    [role="option"] span,
    [role="option"] p,
    [role="option"] {
        color: white !important;
    }
    
    /* Additional dropdown menu styles */
    div.st-emotion-cache-1vbkxwb, 
    div.st-emotion-cache-1qg05tj,
    [data-testid="stMarkdownContainer"] + div ul,
    [data-testid="stMarkdownContainer"] + div li {
        background-color: #2c3e50 !important;
    }
    
    div.st-emotion-cache-1vbkxwb p, 
    div.st-emotion-cache-1qg05tj p,
    [data-testid="stMarkdownContainer"] + div ul span,
    [data-testid="stMarkdownContainer"] + div li span {
        color: white !important;
    }
    
    /* Dropdown option hover state */
    [role="option"]:hover {
        background-color: #34495e !important;
        cursor: pointer !important;
    }
    
    /* Selected option highlighting */
    [aria-selected="true"] {
        background-color: #34495e !important;
    }
    
    /* Tab selector styling - updated to match theme */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
        background-color: #f0f2f6;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #f0f2f6;
        color: #262730;
        border-radius: 4px 4px 0 0;
        padding: 10px 20px;
        height: auto;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #2c3e50 !important;
        color: white !important;
        font-weight: bold;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #d8e1ec;
        color: #2c3e50;
    }
    
    .stTabs [data-baseweb="tab-highlight"] {
        background-color: #2c3e50;
    }
    
    .stTabs [data-baseweb="tab-border"] {
        display: none;
    }
    
    .stTabs [data-baseweb="tab"] p,
    .stTabs [data-baseweb="tab-list"] button p {
        color: inherit !important;
        font-size: 1rem;
    }
    
    /* Dashboard metrics styling - smoky grey with dark text */
    .element-container [data-testid="stMetric"] {
        background-color: #e0e0e0 !important;
        border-radius: 8px;
        padding: 16px;
        margin: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .element-container [data-testid="stMetric"] label,
    [data-testid="stMetricLabel"],
    div.stMetric label {
        color: #333333 !important;
        font-weight: bold !important;
        font-size: 1.2rem !important;
        margin-bottom: 8px !important;
        display: block !important;
    }
    
    .element-container [data-testid="stMetric"] div[data-testid="stMetricValue"],
    [data-testid="stMetricValue"],
    div.stMetric div[data-testid="stMetricValue"] {
        color: #000000 !important;
        font-size: 2.2rem !important;
        font-weight: bold !important;
        letter-spacing: 0.5px;
    }
    
    .element-container [data-testid="stMetric"] div[data-testid="stMetricDelta"] {
        color: #333333 !important;
        font-weight: 500 !important;
    }
    
    /* Additional metric styling with smoky grey */
    div.element-container div.stMetric {
        background-color: #e0e0e0 !important;
        border-radius: 8px;
        padding: 16px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    div.element-container div.stMetric p,
    div.element-container div.stMetric span {
        color: #333333 !important;
        font-weight: 500 !important;
    }
    
    /* Table styling for dashboard with improved contrast */
    .dataframe {
        color: black !important;
        border-collapse: separate !important;
        border-spacing: 0 !important;
        border-radius: 8px !important;
        overflow: hidden !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
    }
    
    .dataframe th {
        background-color: #2c3e50 !important;
        color: white !important;
        font-weight: bold !important;
        padding: 12px !important;
        border-bottom: 2px solid #1a2530 !important;
    }
    
    .dataframe td {
        background-color: #f8f9fa !important;
        color: black !important;
        padding: 10px !important;
        border-bottom: 1px solid #dee2e6 !important;
    }
    
    /* Super specific selectors for pink cells */
    table tr td:last-child,
    .dataframe td:last-child,
    [data-testid="stTable"] td:last-child,
    [data-testid="stDataFrame"] td:last-child,
    td[style*="background-color: pink"],
    td[style*="background-color: rgb(255, 192, 203)"],
    td[style*="background-color: #ffc0cb"],
    /* Targeting the styler.applymap in home.py */
    td[style*="background-color: #ffcccc"],
    td[style*="background-color: #ffcccb"],
    td[style*="background-color: #ff"],
    /* Force all pink-ish cells to dark grey */
    td[style*="background: pink"],
    td[style*="background: #ff"],
    td[style*="background-color"] {
        background-color: #4a4a4a !important;
        color: white !important;
        font-weight: bold !important;
    }
    
    /* Extra powerful catch-all override to force certain colors */
    .dataframe tr td:nth-child(5),
    .dataframe tr td:last-child {
        background-color: #4a4a4a !important;
        color: white !important;
        font-weight: bold !important;
    }
    
    /* Dashboard wrapper - ensure all elements are visible */
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {
        background-color: #ffffff !important;
        border-radius: 10px !important;
        padding: 5px !important;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05) !important;
    }
    
    /* Ensure all metric values are visible regardless of class */
    div[class*="stMetric"] div, 
    div[class*="stMetric"] p, 
    div[class*="stMetric"] span,
    div[class*="stMetric"] label {
        color: #333333 !important;
    }
    
    /* Specific styling for metric values */
    div[class*="stMetric"] [data-testid="stMetricValue"] {
        color: #000000 !important;
        font-size: 2.2rem !important;
        font-weight: bold !important;
    }
    
    /* Weekly schedule day styling - updated for expanders */
    .stExpander button[kind="secondary"] {
        background-color: #e9ecef !important;
        color: #333333 !important;
        border: none !important;
        border-radius: 5px !important;
        padding: 10px 15px !important;
        margin: 5px 0 !important;
        font-weight: 500 !important;
        transition: background-color 0.2s ease !important;
    }
    
    /* Weekly schedule day hover effect */
    .stExpander button[kind="secondary"]:hover {
        background-color: #c2c9d1 !important;
        color: #1a1a1a !important;
    }
    
    /* Make sure expander content has appropriate text color */
    .stExpander .st-emotion-cache-ue6h4q {
        color: #333333 !important;
    }
    
    /* Make weekly schedule expander buttons block-level for better appearance */
    .stExpander button[kind="secondary"] {
        display: block !important;
        width: 100% !important;
        text-align: left !important;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
# st.sidebar.image("app/assets/logo.png", width=200, use_column_width=True)
st.sidebar.title("Campus Connect 🎓")
st.sidebar.markdown("Your AI-Powered Student Companion")

# Navigation
pages = {
    "Home": home,
    "Study Planner": study_planner,
    "Smart Tutor": smart_tutor,
    "Campus Events": campus_events,
    "Career Guidance": career_guidance,
    "Finance Tracker": finance_tracker
}

selection = st.sidebar.radio("Navigate", list(pages.keys()))

# Display the selected page
if selection:
    pages[selection].show()

# Footer
st.sidebar.markdown("---")
st.sidebar.info("© 2025 Campus Connect") 