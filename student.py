from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_stdId=StringVar()
        self.var_stdName=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        #first Image

        img=Image.open(r"D:\Projects\Face-Recognition System\Images\student1.jpeg")
        img=img.resize((500,200),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        first_label=Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=0,width=500,height=200)

        #second Image

        img1=Image.open(r"D:\Projects\Face-Recognition System\Images\student3.jpg")
        img1=img1.resize((500,300),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_label=Label(self.root,image=self.photoimg1)
        first_label.place(x=500,y=0,width=550,height=200)

        #Third Image

        img2=Image.open(r"D:\Projects\Face-Recognition System\Images\student1.jpeg")
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

        title_label=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_label.place(x=0,y=0,width=1530,height=45)

        #FRAME Label

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=510)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)

        #current course
        curr_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        curr_frame.place(x=5,y=11,width=720,height=500)

        #department
        dep_label=Label(curr_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        dep_combo=ttk.Combobox(curr_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=17)
        dep_combo["values"]=("Select Department","CS","IT","Civil","AIML","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        Course_label=Label(curr_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        Course_label.grid(row=0,column=2,padx=10,sticky=W)
        Course_combo=ttk.Combobox(curr_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=17)
        Course_combo["values"]=("Select Department","FE","SE","TE","BE")
        Course_combo.current(0)
        Course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(curr_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        year_combo=ttk.Combobox(curr_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=17)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label=Label(curr_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        semester_combo=ttk.Combobox(curr_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=17)
        semester_combo["values"]=("Select Year","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student infor or ID
        class_stu_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_stu_frame.place(x=5,y=135,width=720,height=300)
        studentId_label=Label(class_stu_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        studentId_entry=ttk.Entry(class_stu_frame,textvariable=self.var_stdId,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

       #student name
        studentName_label=Label(class_stu_frame,text="StudentName:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        studentName_entry=ttk.Entry(class_stu_frame,textvariable=self.var_stdName,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Class Division
        class_div_label=Label(class_stu_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        div_combo=ttk.Combobox(class_stu_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=19)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Roll no
        RollNo_label=Label(class_stu_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        RollNo_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        RollNo_entry=ttk.Entry(class_stu_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        RollNo_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_stu_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        #gender_entry=ttk.Entry(class_stu_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        #gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_stu_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=19)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        #DOB
        DOB_label=Label(class_stu_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        DOB_entry=ttk.Entry(class_stu_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        Email_label=Label(class_stu_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        Email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        Email_entry=ttk.Entry(class_stu_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone no
        PhoneNo_label=Label(class_stu_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        PhoneNo_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        PhoneNo_entry=ttk.Entry(class_stu_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        PhoneNo_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        address_label=Label(class_stu_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        address_entry=ttk.Entry(class_stu_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Class Teacher 
        teacher_label=Label(class_stu_frame,text="Class Teacher:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        teacher_entry=ttk.Entry(class_stu_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #Radio Buttons (using ttk)
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_stu_frame,variable=self.var_radio1,text="Take a photo sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(class_stu_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobtn2.grid(row=6,column=1)

        #Buttons Frame
        btn_frame=Frame(class_stu_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=220,width=725,height=120)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=19,font=("times new roman",12,"bold"),bg="black",fg="white")
        save_btn.grid(row=0,column=0)

        Update_btn=Button(btn_frame,text="Update",command=self.update_data,width=19,font=("times new roman",12,"bold"),bg="black",fg="white")
        Update_btn.grid(row=0,column=1)

        Delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=19,font=("times new roman",12,"bold"),bg="black",fg="white")
        Delete_btn.grid(row=0,column=2)

        Reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="black",fg="white")
        Reset_btn.grid(row=0,column=3)

        take_photo_btn=Button(btn_frame,text="Take Photo Sample",command=self.generate_dataset,width=19,font=("times new roman",12,"bold"),bg="black",fg="white")
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn=Button(btn_frame,text="Update Photo Sample",width=19,font=("times new roman",12,"bold"),bg="black",fg="white")
        update_photo_btn.grid(row=1,column=1)

        #Right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=730,height=580)

        #search System
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=10,width=720,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="blue")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=15,font=("times new roman",12,"bold"),bg="black",fg="white")
        search_btn.grid(row=0,column=3,padx=2)

        ShowAll_btn=Button(search_frame,text="Show All",width=14,font=("times new roman",12,"bold"),bg="black",fg="white")
        ShowAll_btn.grid(row=0,column=4,padx=2)

       #table frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=90,width=720,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student Id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll_No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSample")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    #function declaration    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stdName.get()=="" or self.var_stdId.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Oracle@@@123",database="face-recognition_system")
                mycursor=conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_dep.get(),
                                                                                    self.var_course.get(),
                                                                                    self.var_year.get(),
                                                                                    self.var_semester.get(),
                                                                                    self.var_stdId.get(),
                                                                                    self.var_stdName.get(),
                                                                                    self.var_div.get(),
                                                                                    self.var_roll.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_dob.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_phone.get(),
                                                                                    self.var_address.get(),
                                                                                    self.var_teacher.get(),
                                                                                    self.var_radio1.get()
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student detail has been added",parent=self.root) 
            except Exceptionas as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                                                                   
    
    #Fetch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Oracle@@@123",database="face-recognition_system")
        mycursor=conn.cursor()
        mycursor.execute("select * from student")
        data=mycursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #Get Cursor
    def get_cursor(self,event):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0])
        self.var_course.set(data[1])    
        self.var_year.set(data[2])    
        self.var_semester.set(data[3])    
        self.var_stdId.set(data[4])    
        self.var_stdName.set(data[5])                
        self.var_div.set(data[6])    
        self.var_roll.set(data[7])    
        self.var_gender.set(data[8])    
        self.var_dob.set(data[9])    
        self.var_email.set(data[10])    
        self.var_phone.set(data[11])    
        self.var_address.set(data[12])    
        self.var_teacher.set(data[13])    
        self.var_radio1.set(data[14])
    #Update Function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stdName.get()=="" or self.var_stdId.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Oracle@@@123",database="face-recognition_system")
                    mycursor=conn.cursor()
                    mycursor.execute("Update student set `Dep`=%s,`course`=%s,`Year`=%s,`Semester`=%s,`Student Id`=%s,`Name`=%s,`Division`=%s,`Roll No`=%s,`Gender`=%s,`DOB`=%s,`Email`=%s,`Phone`=%s,`Address`=%s,`Teacher`=%s,`PhotoSample`=%s where `Student ID`=%s",(
                                                                                    self.var_dep.get(),
                                                                                    self.var_course.get(),
                                                                                    self.var_year.get(),
                                                                                    self.var_semester.get(),
                                                                                    self.var_stdId.get(),
                                                                                    self.var_stdName.get(),
                                                                                    self.var_div.get(),
                                                                                    self.var_roll.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_dob.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_phone.get(),
                                                                                    self.var_address.get(),
                                                                                    self.var_teacher.get(),
                                                                                    self.var_radio1.get(),
                                                                                    self.var_stdId.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Students details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #Delete Function
    def delete_data(self):
        if self.var_stdId.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Oracle@@@123",database="face-recognition_system")
                    mycursor=conn.cursor()
                    sql="delete from student where `Student ID`=%s"
                    val=(self.var_stdId.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #Reset Button
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")   
        self.var_year.set("Select Year")   
        self.var_semester.set("Select Semester")
        self.var_stdId.set("")
        self.var_stdName.set("Select Department")   
        self.var_div.set("Select Division")   
        self.var_roll.set("")         
        self.var_gender.set("Male")   
        self.var_dob.set("") 
        self.var_email.set("")   
        self.var_phone.set("")   
        self.var_address.set("")   
        self.var_teacher.set("")   
        self.var_radio1.set("")   

    
    #Generate Data set or Take photo Sample
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_stdName.get()=="" or self.var_stdId.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Oracle@@@123",database="face-recognition_system")
                mycursor=conn.cursor()
                mycursor.execute("select * from student")
                myresult=mycursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                mycursor.execute("Update student set `Dep`=%s,`course`=%s,`Year`=%s,`Semester`=%s,`Student Id`=%s,`Name`=%s,`Division`=%s,`Roll No`=%s,`Gender`=%s,`DOB`=%s,`Email`=%s,`Phone`=%s,`Address`=%s,`Teacher`=%s,`PhotoSample`=%s where `Student Id`=%s",(
                                                                                    self.var_dep.get(),
                                                                                    self.var_course.get(),
                                                                                    self.var_year.get(),
                                                                                    self.var_semester.get(),
                                                                                    self.var_stdId.get(),
                                                                                    self.var_stdName.get(),
                                                                                    self.var_div.get(),
                                                                                    self.var_roll.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_dob.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_phone.get(),
                                                                                    self.var_address.get(),
                                                                                    self.var_teacher.get(),
                                                                                    self.var_radio1.get(),
                                                                                    self.var_stdId.get()==id+1
                                                                                ))    
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #Load Pre defined data on face frontals from openCV
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimum Neighbor=5

                    for (x,y,w,h) in faces:
                        return img[y:y+h,x:x+w]
                    return None
                    
                cap=cv2.VideoCapture(0)      #By default 0 for web camera        
                img_id=0
                id=1
                while True:
                    ret,my_frame=cap.read()
                    if not ret:
                        print("Failed to Capture Image")
                        continue

                    face = face_cropped(my_frame)

                    if face is not None:
                        img_id+=1
                        face=cv2.resize(face,(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data Sets completed")        
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


            
            
        
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()        