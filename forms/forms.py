# forms.py
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class FeedbackForm(FlaskForm):
    feedback = TextAreaField('Feedback', validators=[
                             DataRequired(), Length(min=5, max=500)])
    submit = SubmitField('Analyze Sentiment')
