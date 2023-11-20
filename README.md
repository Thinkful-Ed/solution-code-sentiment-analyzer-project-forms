# Solution Code: Sentiment Analysis Project - Working With Forms

This repository hosts a Flask application for sentiment analysis. The project demonstrates the creation and handling of a web form for sentiment analysis using Flask and WTForms.

## Installation

1. Clone this repository.
2. Navigate to the project directory:
```bash
   cd flask_sentiment_analysis
```
3. Set up a virtual environment (recommended):
   - For macOS and Linux:
```bash
     python -m venv sentiment_analyzer_project_env;
     source sentiment_analyzer_project_env/bin/activate;
```
   - For Windows:
```bash
     python -m venv sentiment_analyzer_project_env
     .\sentiment_analyzer_project_env\Scripts\activate
```
4. Install the required packages:
```shell
   pip install -r requirements.txt
```

## Project Structure

The project is organized into the following files:

- `app.py`: Initializes the Flask application and defines routes for feedback form handling.
- `forms/forms.py`: Contains the definition of `FeedbackForm` using WTForms.
- `templates/feedback.html`: HTML template for the feedback form.
- `requirements.txt`: Lists all the required Python packages for the project.

## Running the Application

To run the Flask application:

```bash
python app.py
```

- The application will be accessible at `http://127.0.0.1:5001`.
- Navigate to `/feedback` to access and submit the feedback form.

## Features

1. **Feedback Form**:
   - Users can submit feedback which is then processed for sentiment analysis.
   - Access the feedback form: `GET /feedback`
   - Submit feedback: `POST /feedback`

2. **Sentiment Analysis**:
   - The submitted feedback is analyzed to determine the sentiment.
   - Currently, this feature uses a placeholder function. Replace `analyze_sentiment` function in `app.py` with your actual sentiment analysis logic or API.

## Customization

- Update `analyze_sentiment` function in `app.py` to integrate actual sentiment analysis.
- Modify `feedback.html` in `templates` to change the form layout and styling.

## Notes

- The project uses Flask and WTForms for web form handling.
- The sentiment analysis functionality needs to be integrated with an actual model or API for meaningful results.