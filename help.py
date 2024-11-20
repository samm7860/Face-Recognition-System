from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_label=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_label.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"D:\Projects\Face-Recognition System\Images\wallpaperflare.com_wallpaper.jpg")
        img_top=img_top.resize((1530,720),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img_top)

        img_lbl=Label(self.root,image=self.photoimg)
        img_lbl.place(x=0,y=55,width=1530,height=720)

        help_label=Label(img_lbl,text="help989@gmail.com",font=("times new roman",20,"bold"),bg="brown")
        help_label.place(x=600,y=400)



if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()     