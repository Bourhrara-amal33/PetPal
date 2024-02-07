import firebase_admin
from firebase_admin import storage, credentials
import requests
import time

# Replace these values with the path to your ADC JSON file, your Firebase Storage bucket name,
# and your Firebase Realtime Database URL
FIREBASE_STORAGE_BUCKET = 'petpal-petfeeder.appspot.com'
FIREBASE_DATABASE_URL = 'https://petpal-petfeeder-default-rtdb.europe-west1.firebasedatabase.app/camera_data.json'
VIDEO_PATH = '5sec_video.mp4'

def initialize_firebase():
    cred = credentials.ApplicationDefault()
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

def send_post_request(date, device, time, video_url):
    data = {
        'date': date,
        'device': device,
        'time': time,
        'videoUrl': video_url
    }

    try:
        response = requests.post(FIREBASE_DATABASE_URL, json=data)
        response.raise_for_status()
        print(f"POST request sent successfully. Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending POST request: {e}")

if __name__ == '__main__':
    initialize_firebase()

    # Define the destination path in Firebase Storage (e.g., videos/5sec_video.mp4)
    destination_path = f"videos/{int(time.time())}_{VIDEO_PATH}"

    # Upload the video to Firebase Storage
    download_url = upload_video_to_firebase(VIDEO_PATH, destination_path)

    if download_url:
        print(f"Video uploaded successfully. Download URL: {download_url}")

        # Get the current date and time
        current_date = time.strftime("%Y-%m-%d", time.localtime())
        current_time = time.strftime("%H:%M:%S", time.localtime())

        # Send a POST request to Firebase Realtime Database
        send_post_request(current_date, 'camera', current_time, download_url)
    else:
        print("Failed to upload video to Firebase Storage.")
