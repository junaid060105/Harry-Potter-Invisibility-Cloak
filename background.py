#opencv for image processing
import cv2 

#creating a videocapture obj
#this is my webcam 
#0 represents the default camera i.e. webcam
#cap is the object that allows us to access the camera
cap = cv2.VideoCapture("0")

#getting the background image
#it keeps taking pictures from webcam - ret(return) says if it worked, background is the picture.
#Or this is simple reading from the webcam
while cap.isOpened():
    ret, background = cap.read()
    
    if ret:
        cv2.imshow("image", background)
        #waitkey is the framerate, every 5ms it will capture image, and when press 'q' it will click the image and get out of the loop.
        if cv2.waitKey(5) == ord('q'):
            #save the bg image
            #saving the bg image with the name image.jpg.
            cv2.imwrite("image.jpg", background) 
            break

#release all the resources
cap.release()

#destroy all the files.
cv2.destroyAllWindows()

