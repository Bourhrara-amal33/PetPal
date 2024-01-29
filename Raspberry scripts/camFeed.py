import picamera
import pygame
import sys
from pygame.locals import QUIT

# Set the resolution of the camera
CAMERA_RESOLUTION = (640, 480)

# Initialize Pygame
pygame.init()

# Create a Pygame window to display the camera feed
screen = pygame.display.set_mode(CAMERA_RESOLUTION)
pygame.display.set_caption("Camera Feed")

# Create a Pygame clock to control the frame rate
clock = pygame.time.Clock()

# Initialize the camera
with picamera.PiCamera() as camera:
    # Set the camera resolution
    camera.resolution = CAMERA_RESOLUTION

    try:
        # Capture video from the camera and display it on the Pygame window
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # Capture a frame from the camera
            camera.capture('temp.jpg', format='jpeg')

            # Load the captured frame and display it on the Pygame window
            img = pygame.image.load('temp.jpg')
            screen.blit(img, (0, 0))
            pygame.display.flip()

            # Control the frame rate
            clock.tick(30)  # Adjust the frame rate as needed
    finally:
        # Release resources when the program is terminated
        pygame.quit()
