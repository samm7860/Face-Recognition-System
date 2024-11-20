from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_label=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_label.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"D:\Projects\Face-Recognition System\Images\bgimage.jpg")
        img_top=img_top.resize((1530,325),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img_top)

        img_lbl=Label(self.root,image=self.photoimg)
        img_lbl.place(x=0,y=55,width=1530,height=325)

        b1_1=Button(self.root,text="TRAIN DATA",cursor="hand2",command=self.train_classifier,font=("times new roman",17,"bold"),bg="black",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)

        img_bottom=Image.open(r"D:\Projects\Face-Recognition System\Images\bgimage.jpg")
        img_bottom=img_bottom.resize((1530,325),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img_bottom)

        img1_lbl=Label(self.root,image=self.photoimg1)
        img1_lbl.place(x=0,y=440,width=1530,height=325)

    def train_classifier(self):
        data_dir=("Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)] 

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')      #converting to grayscale image
            imageNp=np.array(img,'uint8')     #uint8 is a datatype
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13    #press enter to close the window
        ids=np.array(ids)

        #Train the classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training of dataset is completed")        





        
if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()             