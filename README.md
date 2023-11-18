Face Detection in Live Video using OpenCV
Overview
This Python script uses the OpenCV library to perform real-time face detection in a live video stream from your webcam. The Haar Cascade Classifier is employed to detect faces, and rectangles are drawn around the detected faces in the video feed.

Prerequisites
Python 3.x
OpenCV
bash
Copy code
pip install opencv-python
Usage
Clone this repository:

bash
Copy code
git clone https://github.com/your-username/face-detection.git
Navigate to the project directory:

bash
Copy code
cd face-detection
Run the script:

bash
Copy code
python face_detection.py
Press the 'a' key to exit the program.

Configuration
Make sure to provide the correct path to the Haar Cascade XML file in the face_cascade variable:

python
Copy code
face_cascade = cv2.CascadeClassifier("path/to/haarcascade_frontalface_default.xml")
License
This project is licensed under the MIT License.
