from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first Image

        img=Image.open(r"D:\Projects\Face-Recognition System\Images\facial-recognition-attendance-system.jpg")
        img=img.resize((500,200),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        first_label=Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=0,width=500,height=200)

        #second Image

        img1=Image.open(r"D:\Projects\Face-Recognition System\Images\fr_system.png")
        img1=img1.resize((500,200),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_label=Label(self.root,image=self.photoimg1)
        first_label.place(x=500,y=0,width=500,height=200)

        #Third Image

        img2=Image.open(r"D:\Projects\Face-Recognition System\Images\facial-recognition-attendance-system.jpg")
        img2=img2.resize((500,200),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        first_label=Label(self.root,image=self.photoimg2)
        first_label.place(x=1000,y=0,width=550,height=200)

        #Background Image

        img3=Image.open(r"D:\Projects\Face-Recognition System\Images\bgimage.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_label=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_label.place(x=0,y=0,width=1530,height=45)

        #Time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_label,font=('times new roman',14,'bold'),background='white',foreground='black')
        lbl.place(x=0,y=0,width=110,height=50)
        time()    

        #Student BUttons

        img4=Image.open(r"D:\Projects\Face-Recognition System\Images\cc74bf05150b3fa245a03634f9f894d4.png")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=70,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=200,y=260,width=220,height=40)

        #Recognize Face BUttons

        img5=Image.open(r"D:\Projects\Face-Recognition System\Images\face detector.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=70,width=220,height=220)

        b2_2=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b2_2.place(x=500,y=260,width=220,height=40)

        #Attendance BUttons

        img6=Image.open(r"D:\Projects\Face-Recognition System\Images\Attendance.png")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b3.place(x=800,y=70,width=220,height=220)

        b3_3=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b3_3.place(x=800,y=260,width=220,height=40)

        #Help BUttons

        img7=Image.open(r"D:\Projects\Face-Recognition System\Images\helpdesk.png")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b4.place(x=1100,y=70,width=220,height=220)

        b4_4=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b4_4.place(x=1100,y=260,width=220,height=40)

        #Train Face BUttons

        img8=Image.open(r"D:\Projects\Face-Recognition System\Images\Train data.png")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=320,width=220,height=220)

        b5_5=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b5_5.place(x=200,y=520,width=220,height=40)

        #Photos BUttons

        img9=Image.open(r"D:\Projects\Face-Recognition System\Images\images.png")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_image)
        b6.place(x=500,y=320,width=220,height=220)

        b6_6=Button(bg_img,text="Photos",cursor="hand2",command=self.open_image,font=("times new roman",15,"bold"),bg="black",fg="white")
        b6_6.place(x=500,y=520,width=220,height=40)

        #Developer BUttons

        img10=Image.open(r"D:\Projects\Face-Recognition System\Images\developerimage.png")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b7.place(x=800,y=320,width=220,height=220)

        b7_7=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b7_7.place(x=800,y=520,width=220,height=40)

        #Exit BUttons

        img11=Image.open(r"D:\Projects\Face-Recognition System\Images\depositphotos_45737863-stock-photo-exit-blue-web-flat-icon.jpg")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b8=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b8.place(x=1100,y=320,width=220,height=220)

        b8_8=Button(bg_img,text="EXIT",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="black",fg="white")
        b8_8.place(x=1100,y=520,width=220,height=40)

    def open_image(self):
        os.startfile("Data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Exit","Are you sure to exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return             

    #Function Buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)  

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window) 

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)                  







if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()        