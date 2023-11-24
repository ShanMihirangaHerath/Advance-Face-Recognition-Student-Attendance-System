from tkinter import Tk, Label, Button, messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
import os
import cv2
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

    # =====================attendance=====================
    def mark_attendance(self, i, n, r, d):
        filename = "attendance.csv"

        # Check if the file exists, and create it if it doesn't
        if not os.path.isfile(filename):
            with open(filename, "w", newline="\n") as f:
                # Write header if the file is newly created
                f.write("ID,Name,Roll,Department,Time,Date,Status\n")

        try:
            with open(filename, "r+", newline="\n") as f:
                myDataList = f.readlines()
                name_list = []

                for line in myDataList:
                    entry = line.split(",")
                    name_list.append(entry[0])

                if (
                    (i not in name_list)
                    and (n not in name_list)
                    and (r not in name_list)
                    and (d not in name_list)
                ):
                    now = datetime.now()
                    d1 = now.strftime("%d/%m/%Y")
                    dtString = now.strftime("%H:%M:%A")
                    data = f"{i},{n},{r},{d},{dtString},{d1},Present\n"
                    f.write(data)
        except FileNotFoundError:
            messagebox.showerror("Error", f"File {filename} not found!")

    # ==================face recognition================
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors
            )

            crood = []
            for x, y, w, h in features:
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

                my_cursor.execute(
                    "SELECT `student_id` FROM `face-recognizer`.student WHERE student_id="
                    + str(id)
                )
                i = my_cursor.fetchone()
                i = "+".join(i)

                if confidence > 77:
                    cv2.putText(
                        img,
                        f"ID:{i}",
                        (x, y - 75),
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
                        f"Roll:{r}",
                        (x, y - 55),
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
                    self.mark_attendance(i, n, r, d)
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

        def recognize(img, clf, faceCascade):
            crood = draw_boundary(
                img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf
            )
            return img

        def on_close():
            nonlocal is_recognition_completed
            is_recognition_completed = True
            video_cap.release()
            cv2.destroyAllWindows()
            # Display a message box after recognition is completed
            messagebox.showinfo("Recognition Completed", "Face recognition completed!")

            # Close the Tkinter window
            self.root.destroy()

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        # Create a button to close the recognition explicitly
        close_button = Button(
            self.root,
            text="Close Recognition",
            command=on_close,
            cursor="hand2",
            font=("times new roman", 20, "bold"),
            bg="red",
            fg="white",
        )
        close_button.place(x=500, y=500, width=500, height=60)

        is_recognition_completed = False

        while not is_recognition_completed:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
