Face Recognition Attendance System
Introduction

This Python script implements a simple Face Recognition Attendance System using the OpenCV and Face Recognition libraries. The system captures video from a webcam or a specified video file, detects faces, recognizes them, and maintains attendance records in a CSV file.
Prerequisites

    Python 3.x
    Required Python packages: cv2, face_recognition, numpy, PyQt5, dlib

Setup

    Install the required Python packages:

    pip install opencv-python face_recognition numpy PyQt5 dlib

    Ensure you have a webcam connected or provide a video file path when prompted.

Usage

    Run the script:

    python your_script_name.py

    The system will prompt you to select a video file (supports formats: mp4, avi, mkv).

    Detected faces will be framed with a green rectangle, and recognized names will be displayed.

    The attendance records will be saved in a CSV file with the current date (e.g., YY-MM-DD.csv).

Notes

    The system uses a predefined image encoding for face recognition. You can extend the code to include more faces as needed.
    Adjust the threshold variable to fine-tune the face recognition accuracy.

Feel free to modify the code to suit your specific requirements. For any questions or issues, contact the script owner.
