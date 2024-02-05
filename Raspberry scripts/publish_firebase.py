import firebase_admin
from firebase_admin import storage
import time

# Replace these values with the path to your ADC JSON file and your Firebase Storage bucket name
FIREBASE_STORAGE_BUCKET = 'petpal-petfeeder.appspot.com'
VIDEO_PATH = '5sec_video.mp4'

def initialize_firebase():
    cred = firebase_admin.credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {'storageBucket': FIREBASE_STORAGE_BUCKET})

def upload_video_to_firebase(video_path, destination_path):
    try:
        bucket = storage.bucket()

        # Upload the video file
        blob = bucket.blob(destination_path)
        blob.upload_from_filename(video_path)

        # Make the file public
        blob.make_public()

        # Get the public download URL
        download_url = blob.public_url

        print(f"Video uploaded to Firebase Storage. Download URL: {download_url}")

        return download_url

    except Exception as e:
        print(f"Error uploading video to Firebase Storage: {e}")
        return None

if __name__ == '__main__':
    initialize_firebase()

    # Define the destination path in Firebase Storage (e.g., videos/5sec_video.mp4)
    destination_path = f"videos/{int(time.time())}_{VIDEO_PATH}"

    # Upload the video to Firebase Storage
    download_url = upload_video_to_firebase(VIDEO_PATH, destination_path)

    if download_url:
        print(f"Video uploaded successfully. Download URL: {download_url}")
    else:
        print("Failed to upload video to Firebase Storage.")
