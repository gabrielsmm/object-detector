import cv2
import time

class Deteccao:

    def __init__(self):
        self.COLORS = [(106,90,205), (154,205,50), (0, 255, 0), (255, 0, 0)]

        self.class_names = []
        with open("obj.names", "r") as f:
            self.class_names = [cname.strip() for cname in f.readlines()]

        self.net = cv2.dnn.readNet("yolov4_custom_drill.weights", "yolov4_custom.cfg")

        self.model = cv2.dnn_DetectionModel(self.net)
        self.model.setInputParams(size=(608, 608), scale=1/255)

    def detectar_imagem(self, path = ''):
        img = cv2.imread(path)

        classes, scores, boxes = self.model.detect(img, 0.1, 0.2)

        if len(classes) <= 0:
            print('não detectou')

        for (classid, score, box) in zip(classes, scores, boxes):
            color = self.COLORS[int(classid) % len(self.COLORS)]

            label = f"{self.class_names[classid[0]]} : {score}"

            cv2.rectangle(img, box, color, 2)

            cv2.putText(img, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            
        cv2.namedWindow('Deteccao', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Deteccao', 600, 600)
        cv2.imshow('Deteccao', img)
        cv2.waitKey()    
        cv2.destroyAllWindows()

    def detectar_video(self, path = ''):
        cap = cv2.VideoCapture(path)

        while True:

            _, frame = cap.read()

            start = time.time()

            classes, scores, boxes = self.model.detect(frame, 0.5, 0.2)

            end = time.time()

            for (classid, score, box) in zip(classes, scores, boxes):
                color = self.COLORS[int(classid) % len(self.COLORS)]

                label = f"{self.class_names[classid[0]]} : {score}"

                cv2.rectangle(frame, box, color, 2)

                cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            fps_label = f"FPS: {round((1.0/(end - start )), 2)}"

            cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 5)
            cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

            cv2.namedWindow('Deteccao', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Deteccao', 600, 600)
            cv2.imshow('Deteccao', frame)

            if cv2.waitKey(1) == 27:
                break

        cap.release()
        cv2.destroyAllWindows()