import cv2
import uuid
import os
import time

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

folder_name = 'images'

try:
	os.mkdir(folder_name)
	count = 0
except:
	print('Folder already exists.')
    
	list_ = os.listdir(folder_name)
	count = len(list_)

while True:
	_, frame = cap.read()
    
	img = frame.copy()
	text = "count: " + str(count)
	cv2.putText(img, text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 1, cv2.LINE_AA)
	cv2.imshow('win', img)
    
	keyin = cv2.waitKey(1) & 0xFF

	if keyin == ord('q'):
		break
	elif keyin == ord('s'):
		cv2.imwrite('{}/{}.jpg'.format(folder_name, uuid.uuid1()), frame)
		count += 1
		time.sleep(0.01)

cap.release()
cv2.destroyAllWindows()
