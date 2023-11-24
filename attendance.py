from tkinter import (
    Tk,
    Label,
    Button,
    Frame,
    LabelFrame,
    RIDGE,
    PhotoImage,
    ttk,
    StringVar,
    filedialog,
    messagebox,
)
from tkinter import *
from PIL import Image, ImageTk
import os
import csv

mydata = []

class Attendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Attendence Management System")

        # Variables
        self.var_atten_id = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # Add missing variable definition
        self.var_std_id = StringVar()

        title_label = Label(
            self.root,
            text="Attendence Management System",
            font=("times new roman", 30, "bold"),
            bg="darkblue",
            fg="white",
        )
        title_label.place(x=0, y=0, width=1550, height=50)

        bg_image = Image.open("collage_image/background_img.jpg").resize(
            (1550, 750), Image.ADAPTIVE
        )
        self.photoimg1 = ImageTk.PhotoImage(bg_image)
        first_label = Label(self.root, image=self.photoimg1)
        first_label.place(x=0, y=50, width=1550, height=750)

        main_frame = Frame(self.root, bd=2)
        main_frame.place(x=15, y=60, width=1510, height=720)

        # left label frame
        Left_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="lightblue",
            relief=RIDGE,
            text="Student Attendence Details",
            font=("times new roman", 12, "bold"),
            fg="black",
        )
        Left_frame.place(x=10, y=10, width=747, height=700)

        Left_inside_frame = LabelFrame(
            Left_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
        )
        Left_inside_frame.place(x=10, y=10, width=717, height=650)

        # Label and entry
        # student Id
        Attendence_Id_label = Label(
            Left_inside_frame,
            text="Attendence ID:",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        Attendence_Id_label.grid(row=0, column=0, padx=10, pady=5)
        Attendence_ID_entry = ttk.Entry(
            Left_inside_frame,
            width=56,
            textvariable=self.var_atten_id,
            font=("times new roman", 12, "bold"),
        )
        Attendence_ID_entry.grid(row=0, column=1, padx=10, pady=5)

        # Name
        Name_label = Label(
            Left_inside_frame,
            text="Name:",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        Name_label.grid(row=1, column=0, padx=10, pady=5)
        Name_entry = ttk.Entry(
            Left_inside_frame,
            width=56,
            textvariable=self.var_atten_name,
            font=("times new roman", 12, "bold"),
        )
        Name_entry.grid(row=1, column=1, padx=10, pady=5)

        # Roll
        Roll_label = Label(
            Left_inside_frame,
            text="Roll:",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        Roll_label.grid(row=2, column=0, padx=10, pady=5)
        Roll_entry = ttk.Entry(
            Left_inside_frame,
            width=56,
            textvariable=self.var_atten_roll,
            font=("times new roman", 12, "bold"),
        )
        Roll_entry.grid(row=2, column=1, padx=10, pady=5)

        # Department
        Department_label = Label(
            Left_inside_frame,
            text="Department:",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        Department_label.grid(row=3, column=0, padx=10, pady=5)
        Department_entry = ttk.Entry(
            Left_inside_frame,
            width=56,
            textvariable=self.var_atten_dep,
            font=("times new roman", 12, "bold"),
        )
        Department_entry.grid(row=3, column=1, padx=10, pady=5)

        # Date
        Date_label = Label(
            Left_inside_frame,
            text="Date:",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        Date_label.grid(row=4, column=0, padx=10, pady=5)
        Date_entry = ttk.Entry(
            Left_inside_frame,
            width=56,
            textvariable=self.var_atten_date,
            font=("times new roman", 12, "bold"),
        )
        Date_entry.grid(row=4, column=1, padx=10, pady=5)

        # Time
        Time_label = Label(
            Left_inside_frame,
            text="Time:",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        Time_label.grid(row=5, column=0, padx=10, pady=5)
        Time_entry = ttk.Entry(
            Left_inside_frame,
            width=56,
            textvariable=self.var_atten_time,
            font=("times new roman", 12, "bold"),
        )
        Time_entry.grid(row=5, column=1, padx=10, pady=5)

        # Attendence
        Attendence_label = Label(
            Left_inside_frame,
            text="Attendance:",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        Attendence_label.grid(row=6, column=0, padx=10, pady=5)
        self.atten_status = ttk.Combobox(
            Left_inside_frame,
            width=54,
            textvariable=self.var_atten_attendance,
            font=("comicsansns", 11, "bold"),
            state="readonly",
        )
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=6, column=1, pady=8)
        self.atten_status.current(0)

        # Import CSV
        save_button = Button(
            self.root,
            text="Import CSV",
            width=200,
            font=("times new roman", 12, "bold"),
            command=self.importCsv,
            bg="green",
            fg="white",
        )
        save_button.place(x=250, y=450, width=200, height=40)

        # Export Csv
        update_button = Button(
            self.root,
            text="Export CSV",
            width=200,
            font=("times new roman", 12),
            command=self.exportCsv,
            bg="blue",
            fg="white",
        )
        update_button.place(x=250, y=525, width=200, height=40)

        # Update
        delete_button = Button(
            self.root,
            text="Update",
            width=200,
            font=("times new roman", 12),
            bg="purple",
            fg="white",
        )
        delete_button.place(x=250, y=600, width=200, height=40)

        # reset button
        reset_button = Button(
            self.root,
            text="Reset",
            width=18,
            command=self.reset_data,
            font=("times new roman", 12),
            bg="orange",
            fg="white",
        )
        reset_button.place(x=250, y=675, width=200, height=40)

        # Right label frame
        Right_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="yellow",
            relief=RIDGE,
            text="Attendence Details",
            font=("times new roman", 12, "bold"),
        )
        Right_frame.place(x=747, y=10, width=747, height=700)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=0, y=5, width=744, height=550)

        # ===================Scroll bar table=================
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendenceReportTable = ttk.Treeview(
            table_frame,
            column=("id", "name", "roll", "department", "time", "date", "attendance"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id", text="Attendance ID")
        self.AttendenceReportTable.heading("name", text="Name")
        self.AttendenceReportTable.heading("roll", text="Roll")
        self.AttendenceReportTable.heading("department", text="Departmet")
        self.AttendenceReportTable.heading("time", text="Time")
        self.AttendenceReportTable.heading("date", text="Date")
        self.AttendenceReportTable.heading("attendance", text="Attendance")

        self.AttendenceReportTable["show"] = "headings"
        self.AttendenceReportTable.column("id", width=100)
        self.AttendenceReportTable.column("name", width=100)
        self.AttendenceReportTable.column("roll", width=100)
        self.AttendenceReportTable.column("department", width=100)
        self.AttendenceReportTable.column("time", width=100)
        self.AttendenceReportTable.column("date", width=100)
        self.AttendenceReportTable.column("attendance", width=100)

        self.AttendenceReportTable.pack(fill=BOTH, expand=1)

        self.AttendenceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # ==================fetchdata =======================
    def fetchdata(self, rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("", END, values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
            parent=self.root,
        )
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

    # ==========================export ==========================
    def exportCsv(self):
        try:
            if len(mydata) <= 1:
                messagebox.showerror(
                    "No Data", "No Data Found To Export", parent=self.root
                )
                return False
            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save CSV",
                filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
                parent=self.root,
            )
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo(
                    "Data Export",
                    f"Your Data Exported to {os.path.basename(fln)} Successfully",
                )
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendenceReportTable.focus()
        content = self.AttendenceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_roll.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_roll.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()
