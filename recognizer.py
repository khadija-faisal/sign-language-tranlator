import cv2 
# (opencv-python) used for webcam input and image processing to prepare frame 
import mediapipe as mp 
import os
# mediapipe forAI-powered hand tracking with pre-trained ML models for real-time gesture recognition.

from abc import ABC, abstractmethod

class Recognizer(ABC):

    def __init__(self):
        self._is_active = False #Encapsulated attribute to track state
    @abstractmethod
    def recognize(self, input_data):
        pass
    
    def activate(self):
        self._is_active = True
    
    def deactivate(self):
        self._is_active = False



class GestureRecognizer(Recognizer):
    
    def __init__(self):
        super().__init__() # Inheritance: Call parent constructor
        self._mp_hands = mp.solutions.hands
        self._mp_drawing = mp.solutions.drawing_utils
        self._hands = self._mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

        # gesture name and with function sa value
        self.gesture_list = {
            "hello": self.is_hello,
            "thank you": self.is_thank_you,
            "yes": self.is_yes,
            "no": self.is_no,
            "help": self.is_help,
            "please": self.is_plz,
            "good job": self.is_good_job,
            "sorry": self.is_sorry,
            "✌️ peace": self.is_peace,
            "👍 thumbs up": self.is_thumbs_up
        }

    def recognize(self, frame):
        if not self._is_active:
            return "Recognizer is not active"
        
        if frame is None or frame.size == 0:
            return "Invalid frame"
        
        # Convert frame to RGB for MediaPipe
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self._hands.process(frame_rgb)
        gesture = "unknown"

        # Convert back to BGR for OpenCV display
        annotated_frame = frame.copy()

        if results.multi_hand_landmarks:
            print("Hand detected ✅") 
            for hand_landmarks in results.multi_hand_landmarks:
                print(hand_landmarks) 
                self._mp_drawing.draw_landmarks(
                    annotated_frame,
                    hand_landmarks,
                    self._mp_hands.HAND_CONNECTIONS,
                    self._mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2),
                    self._mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2)
                )

                for name, checker in self.gesture_list.items():
                    if checker(hand_landmarks):
                        gesture = name
                        break

        cv2.putText(annotated_frame, gesture, (10, 50), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        return gesture, annotated_frame
                 
    # "hello" : Index finger extended
     # Individual Gesture Checkers (logic can be improved later)
    
    def is_hello(self, lm):
            # Check if index finger (landmark 8) is above the base of the hand (landmark 6)
          # and if the middle finger (landmark 12) is above the base of the hand (landmark 10
        return lm.landmark[8].y < lm.landmark[6].y and lm.landmark[12].y > lm.landmark[10].y
    # 🙏 THANK YOU: , Index, middle, and ring fingers bent downward, resembling a "thank you" gesture.
    def is_thank_you(self, lm):
        return all([
            lm.landmark[8].y > lm.landmark[6].y,  # Index bent
            lm.landmark[12].y > lm.landmark[10].y,  # Middle bent
            lm.landmark[16].y > lm.landmark[14].y # Ring bent
        ])
    # 👍 YES: Thumb up, Thumb up, index finger pointing up (typical thumbs-up gesture).
    def is_yes(self, lm):
        return lm.landmark[4].y < lm.landmark[3].y and lm.landmark[8].y > lm.landmark[6].y
    # ❌ NO: Index finger moved sideways, other fingers down (common "no" gesture).
    def is_no(self, lm):
        return abs(lm.landmark[8].x - lm.landmark[6].x) > 0.1 and lm.landmark[12].y > lm.landmark[10].y
    
    # ✋ HELP: Index and middle fingers extended upward (common "help" gesture).
    def is_help(self, lm):
        return lm.landmark[8].y < lm.landmark[6].y and lm.landmark[12].y < lm.landmark[10].y
    # 🤲 PLEASE: Thumb near index and middle fingers, commonly used for "please".
    def is_plz(self, lm):
        return lm.landmark[4].x < lm.landmark[8].x and abs(lm.landmark[8].y - lm.landmark[12].y) < 0.05
    # 👌 GOOD JOB: Thumb extended, index finger pointing down (symbolizes "good job").
    def is_good_job(self, lm):
        return lm.landmark[4].y < lm.landmark[2].y and lm.landmark[8].y > lm.landmark[6].y
    # 🙇 SORRY: Thumb and index finger close together, thumb above wrist (used for "sorry").
    def is_sorry(self, lm):
        return abs(lm.landmark[4].x - lm.landmark[8].x) < 0.05 and lm.landmark[4].y < lm.landmark[0].y
    # ✌️ PEACE: Index and middle fingers extended upward, commonly used for "peace".
    def is_peace(self, lm):
        return lm.landmark[8].y < lm.landmark[6].y and lm.landmark[12].y < lm.landmark[10].y
    # 👍 THUMBS UP: Thumb extended, other fingers pointing downward (traditional thumbs-up gesture).
    def is_thumbs_up(self, lm):
        return lm.landmark[4].y < lm.landmark[3].y and lm.landmark[8].y > lm.landmark[6].y

    def __del__(self):
        self._hands.close()
#test standalone
if __name__ == "__main__":
    capture = cv2.VideoCapture(0)
    recognizer = GestureRecognizer()
    recognizer.activate()
    while True:
        ret, frame = capture.read()
        if not ret:
            break
        gesture, annotated_frame = recognizer.recognize(frame)
        cv2.putText(annotated_frame, gesture,(10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Gesture", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    capture.release()
    cv2.destroyAllWindows()              


