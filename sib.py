import cv2
import face_recognition
import numpy as np
import csv
import os
import datetime
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import dlib


def select_video():
    app = qtw.QApplication([])
    dialog = qtw.QFileDialog()
    dialog.setWindowTitle("select video ")
    dialog.setFileMode(qtw.QFileDialog.ExistingFile)
    dialog.setFilter(qtc.QDir.Files)
    dialog.setNameFilters(["*.mp4", "*.avi", "*.mkv"])  
    if dialog.exec_():
        video_path = dialog.selectedFiles()[0]
        return video_path
    else:
        return None


video_capture = cv2.VideoCapture(select_video())

video_capture.set(3, 640)  
video_capture.set(4, 480)

mahdi_image = face_recognition.load_image_file("photos/mahdi nabilo1.jpg")  
mahdi_encoding = face_recognition.face_encodings(mahdi_image)[0]

known_face_encodings = [mahdi_encoding]

known_face_names = ["mahdi nabilo tabar"]

students = known_face_names.copy()

face_locations = []
face_encodings = []
face_names = []

threshold = 0.5  

now = datetime.datetime.now()
current_date = now.strftime("%y-%m-%d")

f = open(current_date + '.csv', 'w', newline='')
inwriter = csv.writer(f)

while True:
    success, frame = video_capture.read()
    if frame is not None:  
        small_frame = frame.copy()  
    else:
        print("فریم خالی است!")
        break

    rgb_small_frame = small_frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

            face_names.append(name)

           
            distances = face_recognition.face_distance(known_face_encodings, face_encoding)

            
            if distances[first_match_index] < threshold:
                name = known_face_names[first_match_index]

            face_names.append(name)


            for (top, right, bottom, left) in face_locations:  
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


        if name in students:
            students.remove(name)
            print(students)
            current_time = now.strftime("%H-%M-%S")
            inwriter.writerow([name, current_time])

       
        for (top, right, bottom, left) in face_locations:  
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("attendence system", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'): 
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
