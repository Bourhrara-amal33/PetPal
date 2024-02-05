import cv2

# Open a connection to the USB camera (change the index if you have multiple cameras)
camera = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not camera.isOpened():
    print("Error: Could not open camera.")
    exit()

# Set the video capture properties (optional)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Capture a single frame
ret, frame = camera.read()

# Check if the frame is read successfully
if not ret:
    print("Error: Couldn't read frame.")
    exit()

# Save the captured frame to a file (e.g., out.jpg)
cv2.imwrite('out.jpg', frame)

# Release the camera
camera.release()
