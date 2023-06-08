from ultralytics import YOLO
import cv2
import numpy as np
import serial
from serial import *

bluetooth_port = '/dev/rfcomm0'
baud_rate = 9600
bluetooth = serial.Serial(bluetooth_port, baud_rate)

model = YOLO("best.pt")

cap = cv2.VideoCapture(0)

detect_list = {0:'Bear', 1:'Bird', 2:'WaterDeer', 3:'Pig', 4:'Deer'}

objects = []

while cap.isOpened():
	ret, frame = cap.read()
	results = model(source=frame, conf=0.7, show=True, save_txt=True, device='mps')
	# print(results.pred)
	# print(results)
	for r in results:
			boxes = r.boxes  # Boxes object for bbox outputs
			masks = r.masks  # Masks object for segment masks outputs
			probs = r.probs  # Class probabilities for classification outputs
			objects.append(boxes.cls)
			# print("결과 = " + str(boxes.cls.tolist()))
			items = boxes.cls.tolist()
			for item in items:
				print(detect_list[int(item)])
				data = detect_list[int(item)] + '\n'
				bluetooth.write(data.encode())

# while cap.isOpened():
# 	ret, frame = cap.read()
# 	result = model.predict(source=frame, show=True, device="cpu")


# 	bluetooth.write(data.encode())

cv2.destroyAllWindows()
bluetooth.close()
