
import gradio as gr
import cv2
from gtts import gTTS
import os
from recognizer import GestureRecognizer  # ✅ Import your class

import pygame


pygame.mixer.init()
audio_folder = 'temp_audio/'
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)

# Initialize the recognizer
recognizer = GestureRecognizer()
recognizer.activate()

# To prevent repeating the same output
last_gesture = {"gesture": None}

def play_audio(path):
    pygame.mixer.music.stop() 
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def frame_tranlator(frame):
    global last_gesture

    # Convert to BGR from RGB for OpenCV
    frame_background = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Recognize gesture and get the annotated frame
    gesture, annotation_frame = recognizer.recognize(frame_background)

    print(f"Type of annotated_frame: {type(annotation_frame)}")

    # If a new gesture is detected and is different from the last one
    if gesture != "unknown" and gesture != last_gesture["gesture"]:
        last_gesture["gesture"] = gesture

        # Convert text to speech
        tts = gTTS(text=gesture, lang="en")
        
        # Specify the directory and file path for the audio
        audio_path = os.path.join(audio_folder, f"{gesture}.mp3")
        print(f"Audio file will be saved at: {audio_path}") 
        # Save the audio file
        tts.save(audio_path)
        play_audio(audio_path)
        print(f"Audio file saved at: {audio_path}")
        
        # Play audio once the file is saved
        # You may need to use a different method if you want to play audio directly

        # Return the frame, audio path, and gesture text
        if not os.path.exists(audio_path):
          tts.save(audio_path)
          print(f"Audio file saved at: {audio_path}")
        else:
          print(f"Using cached audio for: {gesture}")
          play_audio(audio_path)
    # No new gesture detected, just return the annotated frame with no audio and text
    return annotation_frame, None, last_gesture["gesture"] or "No Gesture"

# User Interface using Gradio
demo = gr.Interface(
    fn=frame_tranlator,
    inputs=gr.Image(type="numpy", streaming=True),
    outputs=[gr.Image(type="numpy"), gr.Audio(), gr.Textbox(label="Detected Gesture")],
    live=True,
    title="AI Sign Language Translator",
    description="Show hand signs like 'hello', 'thank you', 'yes', etc. It will detect and speak!"
)

def display_gesture(gesture):
    return gesture

gesture_text = gr.Textbox(placeholder="Detected Gesture", lines=1)


if __name__ == "__main__":
    demo.launch()
