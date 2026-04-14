"""
Unit tests for the EmotionDetection package.
Tests emotion_detector function for various inputs.
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Unit tests for the emotion_detector function."""

    def test_joy_emotion(self):
        """Test that joy is the dominant emotion for a joyful statement."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_emotion(self):
        """Test that anger is the dominant emotion for an angry statement."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_emotion(self):
        """Test that disgust is the dominant emotion for a disgusting statement."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness_emotion(self):
        """Test that sadness is the dominant emotion for a sad statement."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_emotion(self):
        """Test that fear is the dominant emotion for a fearful statement."""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_blank_input(self):
        """Test that blank input returns None for all emotions."""
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])
        self.assertIsNone(result['anger'])
        self.assertIsNone(result['disgust'])
        self.assertIsNone(result['fear'])
        self.assertIsNone(result['joy'])
        self.assertIsNone(result['sadness'])

    def test_returns_dict_with_all_keys(self):
        """Test that the function returns a dict with all expected keys."""
        result = emotion_detector("I love this!")
        expected_keys = {'anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion'}
        self.assertEqual(set(result.keys()), expected_keys)

    def test_emotion_scores_are_floats(self):
        """Test that emotion scores are float values."""
        result = emotion_detector("I am happy today")
        if result['dominant_emotion'] is not None:
            self.assertIsInstance(result['anger'], float)
            self.assertIsInstance(result['disgust'], float)
            self.assertIsInstance(result['fear'], float)
            self.assertIsInstance(result['joy'], float)
            self.assertIsInstance(result['sadness'], float)


if __name__ == '__main__':
    unittest.main()
