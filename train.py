from tkinter import Tk, Label, Button, messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os
import cv2
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Face Recognition System")

        title_label = Label(
            self.root,
            text="Train Data Set",
            font=("times new roman", 25, "bold"),
            bg="white",
            fg="green",
        )
        title_label.place(x=0, y=0, width=1550, height=40)

        img = Image.open("collage_image/facial-id-collage-concept(1).jpg").resize(
            (550, 130), Image.ADAPTIVE
        )
        self.photoimg = ImageTk.PhotoImage(img)
        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=0, y=40, width=550, height=130)

        img1 = Image.open(
            "collage_image/facial-recognition-collage-concept(0).jpg"
        ).resize((500, 130), Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        first_label = Label(self.root, image=self.photoimg1)
        first_label.place(x=550, y=40, width=500, height=130)

        img2 = Image.open(
            "collage_image/facial-recognition-collage-concept(2).jpg"
        ).resize((550, 130), Image.ADAPTIVE)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        first_label = Label(self.root, image=self.photoimg2)
        first_label.place(x=1050, y=40, width=550, height=130)

        img3 = Image.open("collage_image/background_img.jpg").resize(
            (1550, 710), Image.ADAPTIVE
        )
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=230, width=1550, height=710)

        train_button = Button(
            self.root,
            text="Train Data",
            command=self.train_classifier,
            cursor="hand2",
            font=("times new roman", 30, "bold"),
            bg="green",
            fg="white",
        )
        train_button.place(x=0, y=170, width=1550, height=60)

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image_path in path:
            try:
                img = Image.open(image_path).convert("L")
            except Exception as e:
                messagebox.showerror(
                    "Error", f"Error reading image: {image_path}\n{str(e)}"
                )
                continue

            image_np = np.array(img, "uint8")
            person_id = int(os.path.split(image_path)[1].split(".")[1])

            faces.append(image_np)
            ids.append(person_id)
            cv2.imshow("Training", image_np)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        # Check OpenCV version and use the appropriate method
        if cv2.__version__.startswith("4"):
            clf = cv2.face.LBPHFaceRecognizer_create()
        else:
            clf = cv2.createLBPHFaceRecognizer()

        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Datasets Completed!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
