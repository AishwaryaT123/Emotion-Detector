"""
Emotion Detection module using Watson NLP library.
Detects emotions from text: anger, disgust, fear, joy, sadness.
Falls back to a keyword-based mock if the Watson API is unreachable.
"""

import json
import requests


def _mock_emotion_detector(text):
    """
    Keyword-based fallback when Watson NLP API is unreachable.
    Returns approximate emotion scores based on keywords in the text.
    """
    text_lower = text.lower()

    anger_words = ['mad', 'angry', 'furious', 'rage', 'hate', 'annoyed', 'irritated', 'livid']
    disgust_words = ['disgusting', 'gross', 'nasty', 'revolting', 'sick', 'awful', 'horrible']
    fear_words = ['afraid', 'scared', 'fear', 'terrified', 'nervous', 'anxious', 'worried', 'dread']
    joy_words = ['happy', 'glad', 'joy', 'excited', 'love', 'great', 'wonderful', 'amazing', 'fantastic', 'pleased']
    sadness_words = ['sad', 'unhappy', 'depressed', 'miserable', 'lonely', 'grief', 'cry', 'tears', 'sorrow']

    def score(words):
        count = sum(1 for w in words if w in text_lower)
        return round(min(0.1 + count * 0.35, 0.95), 3)

    scores = {
        'anger':   score(anger_words),
        'disgust': score(disgust_words),
        'fear':    score(fear_words),
        'joy':     score(joy_words),
        'sadness': score(sadness_words),
    }

    dominant_emotion = max(scores, key=scores.get)
    scores['dominant_emotion'] = dominant_emotion
    return scores


def emotion_detector(text_to_analyse):
    """
    Detects emotions in the given text using Watson NLP EmotionPredict function.
    Falls back to keyword-based mock if the API is unreachable.

    Args:
        text_to_analyse (str): The text to analyze for emotions.

    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion.
              Returns None values if the input is blank.
    """
    if not text_to_analyse or text_to_analyse.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    try:
        response = requests.post(url, json=input_json, headers=headers, timeout=5)

        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        response_dict = json.loads(response.text)
        emotions = response_dict['emotionPredictions'][0]['emotion']

        emotion_scores = {
            'anger':   emotions['anger'],
            'disgust': emotions['disgust'],
            'fear':    emotions['fear'],
            'joy':     emotions['joy'],
            'sadness': emotions['sadness'],
        }

        emotion_scores['dominant_emotion'] = max(emotion_scores, key=emotion_scores.get)
        return emotion_scores

    except Exception:
        # Watson API unreachable — use keyword-based fallback
        print("[INFO] Watson API unreachable. Using local mock emotion detector.")
        return _mock_emotion_detector(text_to_analyse)
