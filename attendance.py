from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #variables
        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()

        #first Image

        img=Image.open(r"D:\Projects\Face-Recognition System\Images\attendance image.jpg")
        img=img.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        first_label=Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=0,width=800,height=200)

        #second Image

        img1=Image.open(r"D:\Projects\Face-Recognition System\Images\attendance image 2.png")
        img1=img1.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_label=Label(self.root,image=self.photoimg1)
        first_label.place(x=800,y=0,width=800,height=200)

        #Background Image

        img3=Image.open(r"D:\Projects\Face-Recognition System\Images\pexels-gdtography-911738.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_label=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_label.place(x=0,y=0,width=1530,height=45)

        #Main Frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=530)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)

        inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        inside_frame.place(x=0,y=25,width=723,height=300)

        #Labels and Entry
        #Attendance ID
        attendanceId_label=Label(inside_frame,text="AttendanceID:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        attendanceId_entry=ttk.Entry(inside_frame,width=20,textvariable=self.var_attend_id,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Roll No
        roll_label=Label(inside_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        roll_entry=ttk.Entry(inside_frame,width=20,textvariable=self.var_attend_roll,font=("times new roman",12,"bold"))
        roll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Name
        name_label=Label(inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        name_entry=ttk.Entry(inside_frame,width=20,textvariable=self.var_attend_name,font=("times new roman",12,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Department
        dep_label=Label(inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        dep_entry=ttk.Entry(inside_frame,width=20,textvariable=self.var_attend_dep,font=("times new roman",12,"bold"))
        dep_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #time
        time_label=Label(inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        time_entry=ttk.Entry(inside_frame,width=20,textvariable=self.var_attend_time,font=("times new roman",12,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Date
        date_label=Label(inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        date_entry=ttk.Entry(inside_frame,width=20,textvariable=self.var_attend_date,font=("times new roman",12,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Attendance
        attendance_label=Label(inside_frame,text="Attendance Status:",font=("times new roman",12,"bold"),bg="white")
        attendance_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        self.attend_status=ttk.Combobox(inside_frame,textvariable=self.var_attend_attendance,font=("times new roman",12,"bold"),state="readonly",width=17)
        self.attend_status["values"]=("Status","Present","Absent")
        self.attend_status.grid(row=3,column=1,padx=2,pady=10,sticky=W)
        self.attend_status.current(0)

        #Buttons Frame
        btn_frame=Frame(inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=260,width=725,height=120)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=19,font=("times new roman",12,"bold"),bg="black",fg="white")
        save_btn.grid(row=0,column=0)

        Update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=19,font=("times new roman",12,"bold"),bg="black",fg="white")
        Update_btn.grid(row=0,column=1)

        Delete_btn=Button(btn_frame,text="Update",width=19,font=("times new roman",12,"bold"),bg="black",fg="white")
        Delete_btn.grid(row=0,column=2)

        Reset_btn=Button(btn_frame,text="Reset",width=19,command=self.reset_data,font=("times new roman",12,"bold"),bg="black",fg="white")
        Reset_btn.grid(row=0,column=3)

        #Right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=730,height=580)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=445)

        #Scroll bar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #fetch data
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata) 

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export !",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Success","Your Data exported to "+os.path.basename(fln)+" Successfully")                
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])            
        self.var_attend_time.set(rows[4])            
        self.var_attend_date.set(rows[5])            
        self.var_attend_attendance.set(rows[6])  

    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")            
        self.var_attend_time.set("")            
        self.var_attend_date.set("")            
        self.var_attend_attendance.set("")












if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()   