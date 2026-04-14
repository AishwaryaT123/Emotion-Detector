"""
Flask web server for the Emotion Detector application.
Provides a web interface and REST API for emotion detection.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def sent_detector():
    """
    Endpoint to detect emotions in the provided text.
    Reads 'textToAnalyze' from query parameters and returns emotion analysis.

    Returns:
        str: Formatted string with emotion scores and dominant emotion,
             or an error message if input is blank.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    # Handle empty or missing input
    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    # Handle status 400 / invalid response (None values)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """
    Renders the main index page of the Emotion Detector web application.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
