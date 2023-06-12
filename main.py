import cv2
from playsound import playsound
import pygame
pygame.init()

red_music = "Red.mp3" 
blue_music = "blue.mp3" 
yellow_music = "yellow.mp3" 
green_music = "green.mp3" 
# pygame.mixer.music.load(blue_music)
# pygame.mixer.music.load(yellow_music)
# pygame.mixer.music.load(green_music)

# img = cv2.imread("red.jpg")
# img = cv2.imread("green.png")
cap = cv2.VideoCapture(2)

while True:

    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height,width, _ = frame.shape

    cx = int(width/2)
    cy = int(height/2)

    # pick pixel value
    pixel_center = hsv_frame[cy,cx]
    hue_value = pixel_center[0]

    color = "Undefined"
    if hue_value < 5:
        color = "RED"
        # pygame.mixer.music.load(red_music)
        # pygame.mixer.music.play()
        # pygame.time.delay(1000) 
        # pygame.mixer.music.stop()
    elif hue_value < 22:
        color = "RED"
    elif hue_value < 33:
        color = "YELLOW"
        # pygame.mixer.music.load(yellow_music)
        # pygame.mixer.music.play()
        # pygame.time.delay(1000) 
        # pygame.mixer.music.stop()
    elif hue_value < 78:
        color = "GREEN"
        # pygame.mixer.music.load(green_music)
        # pygame.mixer.music.play()
        # pygame.time.delay(1000) 
        # pygame.mixer.music.stop()
    elif hue_value < 131:
        color = "BLUE"
        # pygame.mixer.music.load(blue_music)
        # pygame.mixer.music.play()
        # pygame.time.delay(1000) 
        # pygame.mixer.music.stop()
    # elif hue_value < 170:
    #     color = "VIOLET"
    # else:
    #     color = "RED"
        # pygame.mixer.music.load(red_music)
        # pygame.mixer.music.play()
        # pygame.time.delay(1000) 
        # pygame.mixer.music.stop()

    
    print(pixel_center)
    pixel_center_bgr = frame[cy,cx]
    b,g,r = int(pixel_center_bgr[0]),int(pixel_center_bgr[1]),int(pixel_center_bgr[2])


    cv2.circle(frame, (cx,cy), 100 , (255, 255, 255), 5 )

    # cv2.putText(frame,color,(10,50),0,1.5,(b,g,r),2)
    counter1 = 0 
    if color == "RED":
        
        cv2.putText(frame,color,(10,50),0,1.5,(0,0,255),2) 
        if counter1  < 1:
            pygame.mixer.music.load(red_music)
            
            pygame.mixer.music.play()
            counter1 = counter1 + 1
            
        else:
            pygame.mixer.music.stop()
    

    

    cv2.imshow("Frame",frame)
    key = cv2.waitKey(50)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

