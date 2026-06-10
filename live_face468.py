import cv2
import mediapipe as mp
import os
import json
import face_recognition
import csv
import time

# Create a directory to save the landmarks
output_dir = "landmarks_output"
os.makedirs(output_dir, exist_ok=True)

# Create a directory for known faces
known_faces_folder = "faces"
os.makedirs(known_faces_folder, exist_ok=True)

# Initialize Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()



# Function to load known face encodings
def load_known_encodings(known_faces_folder):
    known_face_encodings = []
    known_face_names = []

    for filename in os.listdir(known_faces_folder):
        if filename.endswith((".jpg", ".png", ".jpeg")):
            name = os.path.splitext(filename)[0]
            image_path = os.path.join(known_faces_folder, filename)
            face_image = face_recognition.load_image_file(image_path)
            face_encoding = face_recognition.face_encodings(face_image)[0]
            known_face_encodings.append(face_encoding)
            known_face_names.append(name)

    return known_face_encodings, known_face_names

# Load known face encodings and names
known_face_encodings, known_face_names = load_known_encodings(known_faces_folder)

# Initialize Video Capture
video_capture = cv2.VideoCapture(0)  # Use the default camera (change to a file or camera index if needed)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if not ret:
        break

    # Convert the frame to RGB for face mesh and face recognition
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform face mesh detection
    result = face_mesh.process(rgb_frame)

    # Get image dimensions
    height, width, _ = frame.shape

    # Create a list to store landmarks
    landmarks_list = []

    if result.multi_face_landmarks:
        # Iterate through detected faces
        for facial_landmarks in result.multi_face_landmarks:
            for i in range(0, 468):
                pt1 = facial_landmarks.landmark[i]
                x = int(pt1.x * width)
                y = int(pt1.y * height)
                landmarks_list.append((x, y))

        # Save the landmarks as a JSON file
        output_filename = "landmarks.json"
        output_path = os.path.join(output_dir, output_filename)

        with open(output_path, "w") as json_file:
            json.dump(landmarks_list, json_file)

    # Real-time face recognition
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Try to match the face encoding with known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"  # Default name if no match found
        confidence = None

        for i, is_match in enumerate(matches):
            if is_match:
                confidence = 100 - face_recognition.face_distance([known_face_encodings[i]], face_encoding)[0]
                if confidence > 99:
                    name = known_face_names[i]
                    # Check if the name is "Bill"

        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Display the name (without confidence) on top of the rectangle
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, top - 6), font, 2, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
video_capture.release()
cv2.destroyAllWindows()
