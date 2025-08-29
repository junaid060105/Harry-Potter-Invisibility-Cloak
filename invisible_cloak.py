#for image processing
import cv2
#mathematical library for image handling
import numpy as np

cap = cv2.VideoCapture("0")
address = "https://192.168.1.4:8080/video"
cap.open(address)

background = cv2.imread('./image.jpg')

while cap.isOpened():
    #capture the live frame
    ret, current_frame = cap.read()
    
    if ret:
        #converting the image from RGB to HSV, because with hsv we can differentiate colors more accurately.
        hsv_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)

        #set HSV(hue, saturation, value) values for red color detection
        #range for lower red
        lower_red = np.array([0, 120, 70])
        upper_red = np.array([10, 255, 255])
        mask1 = cv2.inRange(hsv_frame, lower_red, upper_red)

        #range for upper red
        lower_red = np.array([170, 120, 70])
        upper_red = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv_frame, lower_red, upper_red)

        #generate the final red mask
        red_mask = mask1 + mask2
        
        #remove any small reasons of false detection
        #avoid random glitches
        #detects edges of clothes more preciously
        red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations= 10)
        red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_DILATE, np.ones((3,3), np.uint8), iterations=1)

        #substituting the red portion with background image i.e. making cloth invisible
        part1 = cv2.bitwise_and(background, background, mask = red_mask)
        
        #detecting the things that are not red
        not_red = cv2.bitwise_not(red_mask)

        #if cloak is not present show the current image/frame
        part2 = cv2.bitwise_and(current_frame, current_frame, mask = not_red)

        #final output
        cv2.imshow("cloak", part1 + part2)

        if cv2.waitKey(5) == ord('q'): 
            break

cap.release()

cv2.destroyAllWindows()
        