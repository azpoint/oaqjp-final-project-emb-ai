from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection_joy(self):
        response1 = emotion_detector('I am glad this happened')
        self.assertEqual(response1['dominant_emotion'], 'joy')

    def test_emotion_detection_anger(self):
        response2 = emotion_detector('I am really mad about this')
        self.assertEqual(response2['dominant_emotion'], 'anger')

    def test_emotion_detection_disgust(self):
        response3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(response3['dominant_emotion'], 'disgust')

    def test_emotion_detection_sadness(self):
        response4 = emotion_detector('I am so sad about this')
        self.assertEqual(response4['dominant_emotion'], 'sadness')

    def test_emotion_detection_fear(self):
        response5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(response5['dominant_emotion'], 'fear')        
    
unittest.main()