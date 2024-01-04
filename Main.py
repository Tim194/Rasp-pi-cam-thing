from flask import Flask, render_template
import picamera
import time
import os
import threading

app = Flask(__name__)

def capture_photo(file_path):
    # Create a PiCamera object
    with picamera.PiCamera() as camera:
        # Wait for the camera to warm up
        time.sleep(2)

        # Capture a photo and save it to the specified file path
        camera.capture(file_path)
        print("Photo saved")

def runCam():
    while True:
        #Take photo. Can take up to 2 sekunds
        capture_photo("static/current.jpg")

        #Wait for the photo to be taken
        time.sleep(3)

        #rename the old photo to when it was taken and so it dose not get overwriten.
        os.rename("static/current.jpg", "static/" + str(time.time()) + ".jpg")

        #---- To Do ----
        #Delite to old photos
        #---------------

@app.route("/")
def index():
    return render_template("index.html")


#Create and run cam thread
CamThread = threading.Thread(target=runCam)
CamThread.start()

if(__name__ == "__main__"):
    app.run(debug=True, host="0.0.0.0")