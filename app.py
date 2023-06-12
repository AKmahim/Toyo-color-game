from flask import Flask, render_template, Response
import cv2
from playsound import playsound
import pygame
pygame.init()
# from flask_cors import CORS
app = Flask(__name__)
# CORS(app)
# red_music = "red.mp3" 
# blue_music = "blue.mp3" 
# yellow_music = "yellow.mp3" 
# green_music = "green.mp3"
# 
red_music = "Red.mp3" 
blue_music = "blue.mp3" 
yellow_music = "yellow.mp3" 
green_music = "green.mp3"  

def detect_color():
    cap = cv2.VideoCapture(2)
    
    while True:
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        height, width, _ = frame.shape

        cx = int(width/2)
        cy = int(height/2)

        pixel_center = hsv_frame[cy, cx]
        hue_value = pixel_center[0]

        color = "Undefined"
        if hue_value < 5:
            color = "RED"
        elif hue_value < 22:
            color = "ORANGE"
        elif hue_value < 33:
            color = "YELLOW"
        elif hue_value < 78:
            color = "GREEN"
        elif hue_value < 131:
            color = "BLUE"
        

        pixel_center_bgr = frame[cy,cx]
        b,g,r = int(pixel_center_bgr[0]),int(pixel_center_bgr[1]),int(pixel_center_bgr[2])

        # cv2.putText(frame, color, (10, 50), 0, 1.5, (b, g, r), 2)
        cv2.circle(frame, (cx, cy), 100, (255, 255, 255), 5)
        counter1 = 0 
        if color == "RED":
        
            cv2.putText(frame,color,(10,50),0,1.5,(0,0,255),2) 
            if counter1  < 1:
                pygame.mixer.music.load(red_music)
                
                pygame.mixer.music.play()
                counter1 = counter1 + 1
                # print('worked')
            
        else:
            pygame.mixer.music.stop()
    
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(detect_color(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run()
