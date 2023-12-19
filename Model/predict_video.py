import os
from ultralytics import YOLO
import cv2

# Input video file path
video_path = 'cocacola.mp4'

# Output video file path
video_path_out = 'cocacola_out.mp4'

# Open the video file for reading
cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()

# Get the height (H), width (W), and channels of the video frames
H, W, _ = frame.shape

# Create a VideoWriter object to write the output video
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

# Path to the pre-trained YOLO model
model_path = 'best.pt'

# Load the pre-trained YOLO model
model = YOLO(model_path)  # load a custom model

# Confidence threshold for object detection
threshold = 0.5

# Loop through each frame in the input video
while ret:

    # Run object detection on the current frame
    results = model(frame)[0]

    # Loop through each detected object in the frame
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        # Check if the detection confidence is above the threshold
        if score > threshold:

            # Draw a rectangle around the brand
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)

            # Get the size of the brand
            width = round(x2 - x1, 2)
            height = round(y2 - y1, 2)

            # Get the position of the brand
            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2

            # Print the name of the brand
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 100)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

            # Print the confidence of the detection
            cv2.putText(frame, 'Confidence: {:.2f}%'.format(score * 100), (int(x1), int(y1 - 70)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

            # Print the size and position of the brand
            cv2.putText(frame, 'Size: {:.2f}x{:.2f}'.format(width, height), (int(x1), int(y1 - 40)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.putText(frame, 'Position: ({}, {})'.format(round(center_x, 2), round(center_y, 2)), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

    # Write the annotated frame to the output video
    out.write(frame)

    # Read the next frame
    ret, frame = cap.read()

# Release video capture and writer objects, and close all windows
cap.release()
out.release()
cv2.destroyAllWindows()
