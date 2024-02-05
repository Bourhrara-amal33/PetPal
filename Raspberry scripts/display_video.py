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

while True:
    # Capture frame-by-frame
    ret, frame = camera.read()

    # Check if the frame is read successfully
    if not ret:
        print("Error: Couldn't read frame.")
        break

    # Display the captured frame in a window
    cv2.imshow('USB Camera', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
camera.release()
cv2.destroyAllWindows()
