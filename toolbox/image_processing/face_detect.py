""" Shivali Chandra
 Experiment with face detection and image filtering using OpenCV """

import cv2 
import numpy as np

cap = cv2.VideoCapture(0) 
face_cascade = cv2.CascadeClassifier('/home/kiki/Downloads/opencv-3.0.0-beta/data/haarcascades/haarcascade_frontalface_alt.xml')
kernel = np.ones((21,21),'uint8')

while(True): #Capture frame-by-frame 
	ret, frame = cap.read()
	faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))	
	
	for (x,y,w,h) in faces:
		#blur face
		frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
		
		#draw new face
		cv2.circle(frame,(int(x+w*0.27),int(y+h*0.35)),int(w*0.13),(0,0,0),thickness=-1)
		cv2.circle(frame,(int(x+w*0.7),int(y+h*0.35)),int(w*0.13),(0,0,0),thickness=-1)
		cv2.circle(frame,(int(x+w*0.27),int(y+h*0.35)),int(w*0.02),(0,0,255),thickness=-1)
		cv2.circle(frame,(int(x+w*(1-0.3)),int(y+h*0.35)),int(w*0.02),(0,0,255),thickness=-1)
		cv2.ellipse(frame,(int(x+w*0.5),int(y+h*0.9)),(int(w*0.2),int(h*0.2)),0,360,180,(0,0,0),thickness=9)
		cv2.line(frame,(int(x+w*0.1),int(y+h*0.1)),(int(x+w*0.47),int(y+h*0.25)),(0,0,0),thickness=5)
		cv2.line(frame,(int(x+w*0.9),int(y+h*0.1)),(int(x+w*0.53),int(y+h*0.25)),(0,0,0),thickness=5)
		cv2.line(frame,(int(x+w*0.3),int(y+h*0.9)),(int(x+w*0.7),int(y+h*0.9)),(0,0,0),thickness=7)

	# Display the resulting frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('e'):
	    break



# When everything done, release the capture 
cap.release() 
cv2.destroyAllWindows()