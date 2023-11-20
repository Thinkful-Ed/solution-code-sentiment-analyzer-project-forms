# app.py
from flask import Flask, render_template, redirect, url_for, flash, request
from forms.forms import FeedbackForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# routes go here


@app.route('/feedback', methods=['GET'])
def display_feedback():
    form = FeedbackForm()
    return render_template('feedback.html', form=form)


@app.route('/feedback', methods=['POST'])
def submit_feedback():
    form = FeedbackForm(request.form)
    if form.validate():
        feedback_text = form.feedback.data
        sentiment = analyze_sentiment(feedback_text)
        flash(f'Sentiment: {sentiment}', 'success')
        return redirect(url_for('display_feedback'))
    return render_template('feedback.html', form=form)


def analyze_sentiment(text):
    # Replace this function with your AI model or API for sentiment analysis
    return "positive"  # Placeholder sentiment result


if __name__ == '__main__':
    app.run(debug=True, port=5001)
