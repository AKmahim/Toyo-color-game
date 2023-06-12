import cv2
import numpy as np
import pyaudio
import wave
import os

red_music = "Red.wav"
blue_music = "Blue.wav"
yellow_music = "Yellow.wav"
green_music = "Green.wav"

# Initialize PyAudio
p = pyaudio.PyAudio()

# Define audio parameters
chunk = 1024

# Set the desired frame resolution
width, height = 640, 480

# Set the size of the crop region around the center pixel
crop_size = 100

cap = cv2.VideoCapture(2)
cap.set(3, width)
cap.set(4, height)

while True:
    _, frame = cap.read()

    cx = int(width / 2)
    cy = int(height / 2)

    # Crop the frame to the region around the center pixel
    crop_frame = frame[cy - crop_size:cy + crop_size, cx - crop_size:cx + crop_size]
    hsv_frame = cv2.cvtColor(crop_frame, cv2.COLOR_BGR2HSV)

    # Pick pixel value
    pixel_center = hsv_frame[crop_size, crop_size]
    hue_value = pixel_center[0]

    color = "Undefined"
    if hue_value < 5:
        color = "RED"
        audio_path = red_music
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW"
        audio_path = yellow_music
    elif hue_value < 78:
        color = "GREEN"
        audio_path = green_music
    elif hue_value < 131:
        color = "BLUE"
        audio_path = blue_music
    elif hue_value < 170:
        color = "VIOLET"

    print(pixel_center)
    pixel_center_bgr = crop_frame[crop_size, crop_size]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    if color == "RED":
        cv2.putText(frame, color, (10, 50), 0, 1.5, (0, 0, 255), 2)
        # Open the WAV audio file
        wf = wave.open(audio_path, 'rb')

        # Open the default audio output stream
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        # Read audio data and play it
        data = wf.readframes(chunk)
        while data:
            stream.write(data)
            data = wf.readframes(chunk)

        # Close the audio stream
        stream.stop_stream()
        stream.close()

    cv2.circle(frame, (cx, cy), 100, (0, 0, 255), 5)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

# Terminate PyAudio
p.terminate()

cap.release()
cv2.destroyAllWindows()
