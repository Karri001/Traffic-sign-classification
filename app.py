import streamlit as st
import cv2
import torch
import numpy as np
from PIL import Image

# Load your trained YOLOv5 model
weights = 'weights/best.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path=weights)

def detect_objects(frame):
    results = model(frame)
    results = results.xyxy[0]
    
    for *box, conf, cls in results.tolist():
        class_id = int(cls)
        x1, y1, x2, y2 = map(int, box)
        label = f"{model.names[class_id]}: {conf:.2f}"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    return frame

# Streamlit UI
st.title("Real-Time YOLOv5 Object Detection for Traffic Signs, Speed Bumps, and Potholes")

# File uploader for image detection
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = np.array(image)
    detected_image = detect_objects(image)
    st.image(detected_image, caption='Detected Image', use_column_width=True)

# File uploader for video detection
uploaded_video = st.file_uploader("Upload a Video", type=["mp4", "avi", "mov"])
if uploaded_video is not None:
    # Save uploaded video temporarily to disk
    with open("temp_video.mp4", "wb") as f:
        f.write(uploaded_video.read())

    cap = cv2.VideoCapture("temp_video.mp4")
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Detect objects in the frame
        detected_frame = detect_objects(frame)
        stframe.image(detected_frame, channels='BGR')

    cap.release()

# State management for controlling webcam stream
webcam_active = st.session_state.get('webcam_active', False)

# Webcam Streaming controls
start_webcam = st.button('Start Webcam')
stop_webcam = st.button('Stop Webcam')

if start_webcam:
    st.session_state['webcam_active'] = True
    webcam_active = True

if stop_webcam:
    st.session_state['webcam_active'] = False
    webcam_active = False

# Webcam streaming logic
if webcam_active:
    cap = cv2.VideoCapture(0)
    stframe = st.empty()
    
    while st.session_state['webcam_active']:
        ret, frame = cap.read()
        if not ret:
            st.warning("Failed to grab frame from webcam. Exiting...")
            break

        detected_frame = detect_objects(frame)
        stframe.image(detected_frame, channels='BGR')

    cap.release()
    stframe.empty()
