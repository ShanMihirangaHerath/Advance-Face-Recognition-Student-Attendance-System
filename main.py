from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import subprocess
from student import Student
from train import Train
from face_recognition import Face_Recognition

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Face Recognition System")

        # First Image
        img = Image.open("C:/Users/Solo Coder/Face-Recognition-Python-Project/Face-Recognition-Python-Project-1/collage_image/facial-id-collage-concept(1).jpg")
        img = img.resize((550, 130),Image.ADAPTIVE)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=0, y=0, width=550, height=130)

        # Second Image
        img1 = Image.open("C:/Users/Solo Coder/Face-Recognition-Python-Project/Face-Recognition-Python-Project-1/collage_image/facial-recognition-collage-concept(0).jpg")
        img1 = img1.resize((500, 130),Image.ADAPTIVE) 
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_label = Label(self.root, image=self.photoimg1)
        first_label.place(x=550, y=0, width=500, height=130)

        # Third_image
        img2 = Image.open("C:/Users/Solo Coder/Face-Recognition-Python-Project/Face-Recognition-Python-Project-1/collage_image/facial-recognition-collage-concept(2).jpg")
        img2 = img2.resize((550, 130),Image.ADAPTIVE)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_label = Label(self.root, image=self.photoimg2)
        first_label.place(x=1050, y=0, width=550, height=130)

        # Background Image
        img3 = Image.open("C:/Users/Solo Coder/Face-Recognition-Python-Project/Face-Recognition-Python-Project-1/collage_image/background_img.jpg")
        img3 = img3.resize((1550, 710),Image.ADAPTIVE)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # background Image
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1550, height=710)

        # Label
        title_label=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWATE",font=("times new roman",30,"bold"),bg="black",fg="white")
        title_label.place(x=0, y=0, width=1530,height=40)

        # student Button
        img4 = Image.open("C:/Users/Solo Coder/Face-Recognition-Python-Project/Face-Recognition-Python-Project-1/collage_image/student-button-1.jpg")
        img4 = img4.resize((200, 200),Image.ADAPTIVE)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=200,height=200)
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="white")
        b1_1.place(x=200,y=300,width=200,height=40)

        # Detect face Button
        img5 = Image.open("C:/Users/Solo Coder/Face-Recognition-Python-Project/Face-Recognition-Python-Project-1/collage_image/face-detect-button-1.jpg")
        img5 = img5.resize((200, 200),Image.ADAPTIVE)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_recognition)
        b1.place(x=500,y=100,width=200,height=200)
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_recognition,font=("times new roman",20,"bold"),bg="black",fg="white")
        b1_1.place(x=500,y=300,width=200,height=40)

        # Attendence face Button
        img6 = Image.open("C:/Users/Solo Coder/Face-Recognition-Python-Project/Face-Recognition-Python-Project-1/collage_image/attendence-button1.jpg")
        img6 = img6.resize((200, 200),Image.ADAPTIVE)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=200,height=200)
        b1_1=Button(bg_img,text="Attendence",cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="white")
        b1_1.place(x=800,y=300,width=200,height=40)

        # Help face Button
        img7 = Image.open("C:/Users/Solo Coder/Face-Recognition-Python-Project/Face-Recognition-Python-Project-1/collage_image/help-button-1.jpg")
        img7 = img7.resize((200, 200),Image.ADAPTIVE)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=200,height=200)
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="white")
        b1_1.place(x=1100,y=300,width=200,height=40)

        # Train Data Button
        img8 = Image.open("C:/Users/Solo Coder/Face-Recognition-Python-Project/Face-Recognition-Python-Project-1/collage_image/data-train.jpg")
        img8 = img8.resize((200, 200),Image.ADAPTIVE)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=400,width=200,height=200)
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",20,"bold"),bg="black",fg="white")
        b1_1.place(x=200,y=600,width=200,height=40)

        # Photo Data Button
        img9 = Image.open("C:/Users/Solo Coder/Face-Recognition-Python-Project/Face-Recognition-Python-Project-1/collage_image/gallery-photo.jpg")
        img9 = img9.resize((200, 200),Image.ADAPTIVE)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_image)
        b1.place(x=500,y=400,width=200,height=200)
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_image, font=("times new roman",20,"bold"),bg="black",fg="white")
        b1_1.place(x=500,y=600,width=200,height=40)

        # Developer Button
        img10 = Image.open("C:/Users/Solo Coder/Face-Recognition-Python-Project/Face-Recognition-Python-Project-1/collage_image/developer-button.jpg")
        img10 = img10.resize((200, 200),Image.ADAPTIVE)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=400,width=200,height=200)
        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="white")
        b1_1.place(x=800,y=600,width=200,height=40)

        # Exit Button
        img11 = Image.open("C:/Users/Solo Coder/Face-Recognition-Python-Project/Face-Recognition-Python-Project-1/collage_image/exit-button.jpg")
        img11 = img11.resize((200, 200),Image.ADAPTIVE)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=400,width=200,height=200)
        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="white")
        b1_1.place(x=1100,y=600,width=200,height=40)

    def open_image(self):
        directory_path = r"C:\Users\Solo Coder\Face-Recognition-Python-Project\Face-Recognition-Python-Project-1\data"

        try:
            subprocess.Popen(["explorer", directory_path])
        except FileNotFoundError:
            print(f"Error: The directory '{directory_path}' does not exist.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        # ==========================Function Buttons============================
    def student_details(self):
        self.new__window=Toplevel(self.root)
        self.app=Student(self.new__window)

    def train_data(self):
        self.new__window=Toplevel(self.root)
        self.app=Train(self.new__window)

    def face_recognition(self):
        self.new__window=Toplevel(self.root)
        self.app=Face_Recognition(self.new__window)

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
