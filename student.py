from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Face Recognition System")

        # ===========variables===================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_emil=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

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
        title_label=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="lightgreen",fg="black")
        title_label.place(x=0, y=0, width=1530,height=40)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=15, y=50, width=1500, height=600)

        # left lable frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="purple", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"), fg="white")
        Left_frame.place(x=10, y=20, width=750, height=570)

        img_left = Image.open("C:/Users/Solo Coder/Face-Recognition-Python-Project/Face-Recognition-Python-Project-1/collage_image/student_ms-1.jpg") 
        img_left = img_left.resize((750, 150), Image.ADAPTIVE)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=0, y=0, width=750, height=100)  

        # current course
        current_curse_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",14))
        current_curse_frame.place(x=0, y=110,width=747, height=140)

        # department
        dep_label=Label(current_curse_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0, column=0,padx=10)

        dep_combo=ttk.Combobox(current_curse_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=30, state="readonly")
        dep_combo["values"]=("Select Department","Computer","Science","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1,padx=2,pady=10)

        # course
        course_label=Label(current_curse_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0, column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_curse_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=30,state="readonly")
        course_combo["values"]=("Select Course","FE","CS","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3,padx=2,pady=10,sticky=W)

        # Year
        year_label=Label(current_curse_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1, column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_curse_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=30,state="readonly")
        year_combo["values"]=("Select Year","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1,padx=2,pady=10,sticky=W)

        # Semester
        semester_label=Label(current_curse_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1, column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_curse_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=30,state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3,padx=2,pady=10,sticky=W)

        # class student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",14))
        class_student_frame.place(x=0, y=260,width=747, height=280)

        # student Id
        studentId_label=Label(class_student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0, column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=26,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0, column=1, padx=10,pady=5,sticky=W)

        # student Name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0, column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=26,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0, column=3, padx=10,pady=5,sticky=W)

        # class division
        class_div_label=Label(class_student_frame,text="Class division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1, column=0,padx=10,pady=5,sticky=W)

        class_div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=25,height=10,state="readonly")
        class_div_combo["values"]=("Select Division","A","B","C")
        class_div_combo.current(0)
        class_div_combo.grid(row=1, column=1,padx=2,pady=10,sticky=W)

        # Roll No
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1, column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=26,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1, column=3, padx=10,pady=5,sticky=W)

        # Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2, column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=25,state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1,padx=2,pady=10,sticky=W)

        # Dob No
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2, column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=26,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2, column=3, padx=10,pady=5,sticky=W)

        # email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3, column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_emil,width=26,font=("times new roman",12,"bold"))
        email_entry.grid(row=3, column=1, padx=10,pady=5,sticky=W)

        # Phone No
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3, column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=26,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3, column=3, padx=10,pady=5,sticky=W)

        # Address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4, column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=26,font=("times new roman",12,"bold"))
        address_entry.grid(row=4, column=1, padx=10,pady=5,sticky=W)

        # Teacher name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4, column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=26,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4, column=3, padx=10,pady=5,sticky=W)

        # radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="no")
        radiobtn2.grid(row=6,column=1)

        # buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=15,y=190,width=700,height=30)

        # save button
        save_button=Button(btn_frame,text="Save",command=self.add_data,width=19,font=("times new roman",12),bg="green",fg="white")
        save_button.grid(row=0, column=0)

        # update button
        update_button=Button(btn_frame,text="Update",command=self.update_data,width=18,font=("times new roman",12),bg="skyblue",fg="white")
        update_button.grid(row=0, column=1)

        # delete button
        delete_button=Button(btn_frame,text="Delete",width=18,font=("times new roman",12),bg="red",fg="white")
        delete_button.grid(row=0, column=2)

        # reset button
        reset_button=Button(btn_frame,text="Reset",width=18,font=("times new roman",12),bg="orange",fg="white")
        reset_button.grid(row=0, column=3)

        # buttons frame1
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=15,y=222,width=700,height=30)

        # take pkoto
        take_photo_button=Button(btn_frame1,text="Take Photo",width=38,font=("times new roman",12),bg="gray",fg="white")
        take_photo_button.grid(row=0, column=0)

        # update pkoto
        take_photo_button=Button(btn_frame1,text="Update Photo",width=38,font=("times new roman",12),bg="blue",fg="white")
        take_photo_button.grid(row=0, column=1)


        # Right lable frame
        Right_farme=LabelFrame(main_frame,bd=2,bg="skyblue",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_farme.place(x=760, y=20, width=725, height=570)

        img_right = Image.open("C:/Users/Solo Coder/Face-Recognition-Python-Project/Face-Recognition-Python-Project-1/collage_image/student_ms-2.jpeg") 
        img_right = img_right.resize((750, 150), Image.ADAPTIVE)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_farme, image=self.photoimg_right)
        f_lbl.place(x=0, y=0, width=750, height=100)

        # ============Search System===========
        search_frame=LabelFrame(Right_farme,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",14))
        search_frame.place(x=0, y=110,width=720, height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",14,"bold"),bg="red",fg="white")
        search_label.grid(row=0, column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=12,state="readonly")
        search_combo["values"]=("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",13,"bold"))
        search_entry.grid(row=0, column=2, padx=10,pady=5,sticky=W)

        search_button=Button(search_frame,text="Search",width=14,font=("times new roman",12),bg="green",fg="white")
        search_button.grid(row=0, column=3,padx=4)

        shaowAll_button=Button(search_frame,text="Show All",width=14,font=("times new roman",12),bg="blue",fg="white")
        shaowAll_button.grid(row=0, column=4,padx=4)

        # ==========Table Frame==========
        table_frame=Frame(Right_farme,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=0, y=190,width=720, height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Devision")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    
    # ====================function decration======================
    def add_data(self):
        if self.var_dep.get()=="Select Departmant" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn= mysql.connector.connect(host="localhost",username="root",password="Shan_200630103728",database="face-recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO `face-recognizer`.student VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_emil.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details Has Been Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)

    # ===================Fetch Data=============================
    def fetch_data(self):
        conn= mysql.connector.connect(host="localhost",username="root",password="Shan_200630103728",database="face-recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM `face-recognizer`.student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # =====================get Cursor===============
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_emil.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # update Functon=============

    def update_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno(
                    "Update", "Do You Want To Update This Student Details", parent=self.root
                )
                if update > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Shan_200630103728",
                        database="face-recognizer",
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "UPDATE `face-recognizer`.student SET dep=%s,course=%s,year=%s,semester=%s,student_id=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photo=%s WHERE student_id=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_id.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_emil.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get(),
                        ),
                    )
                    messagebox.showinfo(
                        "Success", "Student Details Successfully Updated", parent=self.root
                    )
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                else:
                    if not update:
                        return
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()