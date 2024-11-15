"""Final Project of Emotion Detector"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def em_detector():
    """To detect imotion of the input text"""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        response_string = "Invalid text! Please try again!"
    else:
        response_string = f"For the given statement, the system response is '" \
        f"'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, " \
        f"'joy': {joy_score} and 'sadness': {sadness_score}. " \
        f"The dominant emotion is {dominant_emotion}."

    # Return a formatted string with the sentiment label and score
    return response_string

@app.route("/")
def render_index_page():
    """Index page of the application"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)