from tkinter import Tk, Label, Button, messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os
import cv2
import numpy as np
import mysql.connector


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Face Recognition System")

        title_label = Label(
            self.root,
            text="Face Recognition",
            font=("times new roman", 30, "bold"),
            bg="blue",
            fg="white",
        )
        title_label.place(x=0, y=0, width=1550, height=50)

        img = Image.open("collage_image/face-reg-1.jpeg").resize(
            (775, 750), Image.ADAPTIVE
        )
        self.photoimg = ImageTk.PhotoImage(img)
        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=0, y=50, width=775, height=750)

        img1 = Image.open("collage_image/face-reg-2.jpeg").resize(
            (775, 750), Image.ADAPTIVE
        )
        self.photoimg1 = ImageTk.PhotoImage(img1)
        first_label = Label(self.root, image=self.photoimg1)
        first_label.place(x=775, y=50, width=775, height=750)

        b1_1 = Button(
            self.root,
            command=self.face_recog,
            text="Face Recognition",
            cursor="hand2",
            font=("times new roman", 20, "bold"),
            bg="red",
            fg="white",
        )
        b1_1.place(x=500, y=550, width=500, height=60)

    # ==================face recognition================
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, mainNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, mainNeighbors)

            crood = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y : y + h, x : x + w])
                confidence = int(100 * (1 - predict / 300))

                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Shan_200630103728",
                    database="face-recognizer",
                )
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "SELECT `name` FROM `face-recognizer`.student WHERE student_id="
                    + str(id)
                )
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute(
                    "SELECT `roll` FROM `face-recognizer`.student WHERE student_id="
                    + str(id)
                )
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute(
                    "SELECT `dep` FROM `face-recognizer`.student WHERE student_id="
                    + str(id)
                )
                d = my_cursor.fetchone()
                d = "+".join(d)

                if confidence > 77:
                    cv2.putText(
                        img,
                        f"Roll:{r}",
                        (x, y - 55),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )
                    cv2.putText(
                        img,
                        f"Name:{n}",
                        (x, y - 30),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )
                    cv2.putText(
                        img,
                        f"Department:{d}",
                        (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(
                        img,
                        "Unknown Face",
                        (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )

                crood = [x, y, w, y]
            return crood

        def recognize(img, clf, faceCasscade):
            crood = draw_boundray(img, faceCasscade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        FaceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, FaceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
