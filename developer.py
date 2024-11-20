from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_label=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_label.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"D:\Projects\Face-Recognition System\Images\bgimage.jpg")
        img_top=img_top.resize((1530,720),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img_top)

        img_lbl=Label(self.root,image=self.photoimg)
        img_lbl.place(x=0,y=55,width=1530,height=720)

        #Frame
        main_frame=Frame(img_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1=Image.open(r"D:\Projects\Face-Recognition System\Images\MyPicture.jpg")
        img_top1=img_top1.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img_top1)

        img_lbl=Label(main_frame,image=self.photoimg1)
        img_lbl.place(x=300,y=0,width=200,height=200)

        #Developer info
        dev_label=Label(main_frame,text="Hello my name is Sameer",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="Hello my name is Sameer",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=40)

        img_top2=Image.open(r"D:\Projects\Face-Recognition System\Images\wallpaperflare.com_wallpaper (1).jpg")
        img_top2=img_top2.resize((500,300),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img_top2)

        img_lbl=Label(main_frame,image=self.photoimg2)
        img_lbl.place(x=0,y=210,width=500,height=300)




if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()     