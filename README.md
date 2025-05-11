# Sign Language Translator

A real-time **Sign Language Translator** that uses hand gesture recognition to translate sign language into text using **Gradio**, **MediaPipe**, and **OpenCV**. This project aims to enhance communication between the hearing-impaired community and the general public, focusing on recognizing and translating simple, everyday sign language gestures.

---

## 📝 **Features**

- **Real-time Hand Gesture Recognition**:  
  Uses **MediaPipe** to detect hand movements and recognize gestures from a live webcam feed.

- **Simple Gestures Translation**:  
  Translates common sign language gestures like "thank you", "yes", "no", "help", and "please" into text in real-time.

- **Interactive User Interface**:  
  Built using **Gradio** for a smooth, easy-to-use interface that displays both the live webcam feed and the translated text.

- **Lightweight and Efficient**:  
  Optimized for basic and essential gestures, making it simple and easy for beginners to use.

---

## 🤖 **How It Works**

1. **Hand Detection with MediaPipe**:  
   **MediaPipe**'s hand tracking model detects the position and movement of hands in the video feed. It analyzes the hands based on keypoints and landmarks, capturing all the important features like finger positions, orientation, and gestures.

2. **Gesture Recognition**:  
   Once the hand is detected, the system identifies specific gestures by recognizing patterns in the finger movements. These gestures are mapped to pre-defined actions, such as "yes", "no", "thank you", and "help".

3. **Text Conversion**:  
   The recognized gesture is translated into its corresponding **text** using Python logic. This text is displayed in real-time on the screen, allowing the user to see what the gesture means instantly.

4. **Gradio Interface**:  
   **Gradio** is used to create an interactive user interface. This provides a smooth and simple web interface, where users can see the webcam stream and receive translations instantly.

---

## 🌱 **Benefits of Simple Gestures**

Even with a few simple gestures, the **Sign Language Translator** offers powerful benefits for communication:

- **Improved Accessibility**:  
   Simple gestures like "thank you", "yes", "no", "help", and "please" can significantly enhance the ability of non-signers to communicate with the hearing-impaired community.

- **Ease of Use**:  
   The application provides an accessible entry point for beginners to learn and use sign language.

- **Encourages Awareness and Understanding**:  
   Recognizing basic gestures increases awareness of sign language and encourages more people to learn it.

- **Instant Feedback**:  
   Real-time translations allow users to instantly see if their gesture is recognized correctly, providing valuable feedback for improvement.

- **Focus on Simple Interactions**:  
   The translator focuses on small but essential gestures, making it practical for real-world communication.

---

## 🚀 **Installation**

1. Clone the repository:

   ```bash
   git clone https://github.com/khadija-faisal/sign-language-translator.git
Navigate to the project directory:

bash
Copy code
cd sign-language-translator
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
🖥️ Usage
Start the application:

bash
Copy code
python app.py
Open the Gradio interface in your browser, and the webcam feed will be displayed. As you sign simple gestures, the system will translate them into text in real-time.

🛠️ Technologies Used
Python: For the core logic and integration.

MediaPipe: For real-time hand tracking and gesture detection.

OpenCV: For capturing the webcam feed and processing the images.

Gradio: For building the interactive user interface.

🙋‍♂️ Acknowledgements
Gradio: For the amazing library that makes building interactive UIs simple.

MediaPipe: For providing the hand tracking model used in the project.

OpenCV: For helping capture and process the webcam feed.


created by khadija Mughal 
Junior frontend developer 
and this project ins't too good but I'm working on it 
