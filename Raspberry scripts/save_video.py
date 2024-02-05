import cv2
import time

# Open a connection to the USB camera (change the index if you have multiple cameras)
camera = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not camera.isOpened():
    print("Error: Could not open camera.")
    exit()

# Set the video capture properties (optional)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Define the duration for capturing video (in seconds)
duration = 5

# Define the video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter('5sec_video.mp4', fourcc, 20.0, (1280, 720))

# Get the current time
start_time = time.time()

while True:
    # Capture frame-by-frame
    ret, frame = camera.read()

    # Check if the frame is read successfully
    if not ret:
        print("Error: Couldn't read frame.")
        break

    # Write the frame to the video file
    video_writer.write(frame)

    # Break the loop if the specified duration is reached
    if time.time() - start_time >= duration:
        break

# Release the camera and video writer
camera.release()
video_writer.release()
