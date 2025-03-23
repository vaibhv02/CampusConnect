# Campus Connect

Campus Connect is an AI-powered student companion application designed to help college students manage their academic life, find study resources, and plan their career path. Built with Streamlit, it provides a user-friendly interface for accessing various student services.

## Features

- **Personalized Dashboard**: View your academic schedule, upcoming deadlines, and study recommendations
- **Study Planner**: Organize your study sessions, track tasks, and analyze your study patterns
- **Smart Tutor**: Get AI-powered help with your coursework and academic questions
- **Campus Events**: Discover and RSVP for campus events, study groups, and workshops
- **Career Guidance**: Access career assessments, internship opportunities, and professional development resources

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/campus-connect.git
cd campus-connect
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

## Project Structure

```
campus-connect/
├── app/
│   ├── assets/         # Images, icons, and other static files
│   ├── components/     # Reusable UI components
│   ├── data/          # Data files and sample data
│   ├── models/        # AI/ML models and utilities
│   ├── pages/         # Individual page modules
│   └── utils/         # Helper functions and utilities
├── app.py             # Main application file
├── requirements.txt   # Project dependencies
└── README.md         # Project documentation
```

## Dependencies

- streamlit==1.32.0
- pandas==2.1.0
- numpy==1.24.4
- plotly==5.18.0
- scikit-learn==1.3.2
- pillow==10.1.0
- transformers==4.37.0
- openai==1.3.0
- firebase-admin==6.2.0

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Streamlit team for the amazing framework
- Contributors and maintainers of all the dependencies
- The open-source community for their valuable resources and tools 