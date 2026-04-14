# Emotion Detector

## Project Name: Emotion Detector

An AI-based Emotion Detector web application built using Watson NLP and Flask.

## Description

This project uses IBM Watson NLP's EmotionPredict function to detect emotions (anger, disgust, fear, joy, sadness) in a given piece of text and identifies the dominant emotion.

## Tasks Completed

- **Task 1:** Clone the project repository
- **Task 2:** Create an emotion detection application using the Watson NLP library
- **Task 3:** Format the output of the application
- **Task 4:** Package the application as `EmotionDetection`
- **Task 5:** Run Unit tests on the application
- **Task 6:** Web deployment of the application using Flask
- **Task 7:** Incorporate error handling
- **Task 8:** Run static code analysis

## Project Structure

```
emotion_detector/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── server.py
├── test_emotion_detection.py
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python server.py
```

Visit `http://localhost:5000` in your browser.

## Running Unit Tests

```bash
python -m pytest test_emotion_detection.py -v
```

## Running Static Code Analysis

```bash
pylint server.py EmotionDetection/emotion_detection.py
```

## API Usage

```
GET /emotionDetector?textToAnalyze=<your text>
```

**Example:**
```
GET /emotionDetector?textToAnalyze=I am so happy today!
```

**Response:**
```
For the given statement, the system response is 'anger': 0.006, 'disgust': 0.002, 'fear': 0.009, 'joy': 0.976 and 'sadness': 0.014. The dominant emotion is joy.
```

## Error Handling

- Blank input returns: `"Invalid text! Please try again!"`
- Status 400 from Watson NLP also returns: `"Invalid text! Please try again!"`

## Technologies Used

- Python 3.x
- Flask
- Requests
- IBM Watson NLP (EmotionPredict)
- Pylint (static analysis)
