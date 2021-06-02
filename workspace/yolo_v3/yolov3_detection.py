import cv2
import numpy as np

# read 3 files (weights, configuration, and class names)
net = cv2.dnn.readNet('/workspace/yolo_v3/Trial_2/yolov3_trial2_training_final.weights', '/workspace/yolo_v3/Trial_2/yolov3_trial2_training_final.cfg')
classes = []
with open('/workspace/yolo_v3/Trial_2/yolov3_trial2_classes.txt', 'r') as f:
    classes = f.read().splitlines()

# bring video file
cap = cv2.VideoCapture('test.MOV')

# save result as a video file (.mp4)
w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*"DIVX")
out = cv2.VideoWriter('/workspace/yolo_v3/Trial_2/yolov3_trial2_result.mp4', fourcc, fps, (w,h))

# extra setting
font = cv2.FONT_HERSHEY_PLAIN

# draw bounding box (bbox) per frame
while True:
    ## prepare before drawing bbox
    _, img = cap.read()
    height, width, _ = img.shape

    blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    output_layers = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers)

    boxes = []
    confidences = []
    class_ids = []

    ## gather the information for all bboxes which have confidence over threshold
    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.333:  #### round(1/3, 3) for each class (total: 3 classes)
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w/2)
                y = int(center_y - h/2) #### Top-left corner

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    ## Non-Maximal Suppression
    if len(boxes) != None:
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.333, 0.3)  # 0.5, 0.4 for 1 class

        ### randomize color for each bbox
        colors = np.random.uniform(0, 255, size=(len(boxes), 3))

        ### draw bbox with annotation : class name & confidence level
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i], 2))
            color = colors[i]
            cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
            cv2.putText(img, label+ " " + confidence, (x, y+20), font, 2, (255,255,255), 2)

    ## save the result as a video file
    out.write(img)

    ## show the video being processed in a new window; and stop the whole process if esc is entered
    cv2.imshow('Image', img)
    key = cv2.waitKey(1)
    if key == 27:
        break

# Close
cap.release()
out.release()

cv2.destroyAllWindows()
