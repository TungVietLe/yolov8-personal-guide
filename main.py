from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt") 
img = cv2.imread("https://ultralytics.com/images/bus.jpg")

results = model(img)  # predict on an image
annotated_img = results[0].plot()

cv2.imshow("window", annotated_img)
if cv2.waitKey(0) == ord("q"):
    cv2.destroyAllWindows()