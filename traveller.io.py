""" The following project demonstrates the cource of action executed while a flight reservation is in progress..
    note: internet connectivity required.
Credits:
1) Amal Thomas - frontend(GUI, Forms, windows,etc)
2) Alan Johny - backend (database, schedules,etc)
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from PIL import ImageTk,Image
from plyer import notification
import mysql.connector as sqltor
import yagmail
import random
mailer = yagmail.SMTP('thomasamal856@gmail.com')         #connecting to SMTP server
con = sqltor.connect(host='localhost',user='root',passwd='amal2003',database='traveller_io')  #connecting to MySQL server
c = con.cursor()
def generate_PNR():
    a=random.randint(23,43)
    b=random.randint(3232,64656)
    alp = ['SDF','SSF','THH','RGGT','EGS','RGRE','GGTBT']
    return random.choice(alp)+str(a)+str(b)

def submit_f1():
    if name.get()=="":
        msg.showwarning("Traveller.io says","Please specify your name")
    elif age.get()=="":
        msg.showwarning("Traveller.io says","Please specify your age")
    elif gender.get()=="":
        msg.showwarning("Traveller.io says","Please specify your gender")
    elif mob.get()=="":
        msg.showwarning("Traveller.io says","Please specify your mobile number")
    elif email.get()=="":
        msg.showwarning("Traveller.io says","Please specify your email id")
    else:
        pnr = generate_PNR()
        c.execute(('insert into flight_bookings values("{}","{}","{}","{}","{}","{}","{}",{},"{}",{},"{}","{}","{}")').format(pnr,name.get(),data1[2],data1[3],date_of_dep.get(),data1[5],data1[7],age.get(),gender.get(),mob.get(),email.get(),data1[0],data1[1]))
        adr = email.get()
        mail = [''' <html><head><title></title></head><body><p>Your flight booking from:'''+data1[2]+''' to:'''+data1[3]+''' on '''+date_of_dep.get()+''' has been confirmed.</p>
    <p> Your itenerary is as below:</p>PNR:'''+pnr+'''<br>Airline:'''+data1[1]+'''<br> Flight No.:'''+data1[0]+'''<br>Name:'''+name.get()+'''<br>'''+'''From:'''+data1[2]+'''<br>'''+'''To:'''+data1[3]+'''<br>'''+'''Date of departure:'''+date_of_dep.get()+'''<br>'''+'''Departure time:'''+str(data1[5])+'''<br>'''+'''Arrival Time:'''+str(data1[7])+'''<br>'''+'''<p><b><u>Please take note of the following</u></b><br>''']
        try:
            mailer.send(adr,'Flight confirmation',mail)
            notification.notify(title = "Traveller_io",message = "Congrats! You booking has been confirmed. A confirmation mail has been sent to your inbox",app_icon = 'images\\travel.ico',timeout = 10)
            con.commit()
        except:
            notification.notify(title = "Traveller_io",message = "Sorry! Your booking could not be confirmed due to technical reasons. Please try again later.",app_icon = 'images\\travel.ico',timeout = 10)
            con.commit()
            con.close()
def submit_f2():
    if name.get()=="":
        msg.showwarning("Traveller.io says","Please specify your name")
    elif age.get()=="":
        msg.showwarning("Traveller.io says","Please specify your age")
    elif gender.get()=="":
        msg.showwarning("Traveller.io says","Please specify your gender")
    elif mob.get()=="":
        msg.showwarning("Traveller.io says","Please specify your mobile number")
    elif email.get()=="":
        msg.showwarning("Traveller.io says","Please specify your email id")
    else:
        pnr = generate_PNR
        c.execute(('insert into flight_bookings values("{}","{}","{}","{}","{}","{}","{}",{},"{}",{},"{}","{}","{}")').format(pnr,name.get(),data2[2],data2[3],date_of_dep.get(),data2[5],data2[7],age.get(),gender.get(),mob.get(),email.get(),data2[0],data2[1]))
        adr = email.get()
        try:
            mail = [''' <html><head><title></title></head><body><p>Your flight booking from:'''+data2[2]+''' to:'''+data2[3]+''' on '''+date_of_dep.get()+''' has been confirmed.</p>
            <p> Your itenerary is as below:</p>PNR:'''+pnr+'''<br>Airline:'''+data2[1]+'''<br> Flight No.:'''+data2[0]+'''<br>Name:'''+name.get()+'''<br>'''+'''From:'''+data2[2]+'''<br>'''+'''To:'''+data2[3]+'''<br>'''+'''Date of departure:'''+date_of_dep.get()+'''<br>'''+'''Departure time:'''+str(data2[5])+'''<br>'''+'''Arrival Time:'''+str(data2[7])+'''<br>'''+'''<p><b><u>Please take note of the following</u></b><br>''']
            mailer.send(adr,'Flight confirmation',mail)
            con.commit()
            notification.notify(title = "Traveller_io",message = "Congrats! You booking has been confirmed. A confirmation mail has been sent to your inbox",app_icon = 'images\\travel.ico',timeout = 10)
        except:
            notification.notify(title = "Traveller_io",message = "Sorry! Your booking could not be confirmed due to technical reasons. Please try again later.",app_icon = 'images\\travel.ico',timeout = 10)
            con.commit()
            con.close()

def submit_f3():
    if name.get()=="":
        msg.showwarning("Traveller.io says","Please specify your name")
    elif age.get()=="":
        msg.showwarning("Traveller.io says","Please specify your age")
    elif gender.get()=="":
        msg.showwarning("Traveller.io says","Please specify your gender")
    elif mob.get()=="":
        msg.showwarning("Traveller.io says","Please specify your mobile number")
    elif email.get()=="":
        msg.showwarning("Traveller.io says","Please specify your email id")
    else:
        pnr = generate_PNR
        c.execute(('insert into flight_bookings values("{}","{}","{}","{}","{}","{}","{}",{},"{}",{},"{}","{}","{}")').format(pnr,name.get(),data3[2],data3[3],date_of_dep.get(),data3[5],data3[7],age.get(),gender.get(),mob.get(),email.get(),data3[0],data3[1]))
        adr = email.get()
        mail = [''' <html><head><title></title></head><body><p>Your flight booking from:'''+data3[2]+''' to:'''+data3[3]+''' on '''+date_of_dep.get()+''' has been confirmed.</p>
    <p> Your itenerary is as below:</p>PNR:'''+pnr+'''<br>Airline:'''+data3[1]+'''<br> Flight No.:'''+data3[0]+'''<br>Name:'''+name.get()+'''<br>'''+'''From:'''+data3[2]+'''<br>'''+'''To:'''+data3[3]+'''<br>'''+'''Date of departure:'''+date_of_dep.get()+'''<br>'''+'''Departure time:'''+str(data3[5])+'''<br>'''+'''Arrival Time:'''+str(data3[7])+'''<br>'''+'''<p><b><u>Please take note of the following</u></b><br>''']
        try:
            mailer.send(adr,'Flight confirmation',mail)
            notification.notify(title = "Traveller_io",message = "Congrats! You booking has been confirmed. A confirmation mail has been sent to your inbox",app_icon = 'images\\travel.ico',timeout = 10)
            con.commit()
        except:
            notification.notify(title = "Traveller_io",message = "Sorry! Your booking could not be confirmed due to technical reasons. Please try again later.",app_icon = 'images\\travel.ico',timeout = 10)
            con.commit()
            con.close()
    
        
def book_1():
    win_book1 = tk.Toplevel()
    win_book1.title('Booking for '+data1[1])
    bg = Image.open('images\\'+data1[1]+'.png')
    global copy_bg
    copy_bg = bg.copy()
    bg = ImageTk.PhotoImage(bg)
    global bg_label
    bg_label = ttk.Label(win_book1,image=bg)
    bg_label.photo= bg
    bg_label.image = bg
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.bind('<Configure>', resize_image)
    ttk.Label(win_book1,text="You have opted for:",foreground = "red").grid(column=0,row=0)
    ttk.Label(win_book1,text="Flight no:",foreground = "blue").grid(column=0,row=1,pady=3)
    ttk.Label(win_book1,text=data1[0],foreground = "green").grid(column=1,row=1,pady=3)
    ttk.Label(win_book1,text="Airline:",foreground = "blue").grid(column=0,row=2,pady=3)
    ttk.Label(win_book1,text=data1[1],foreground = "green").grid(column=1,row=2,pady=3)
    ttk.Label(win_book1,text="Date of departure:",foreground = "blue").grid(column=0,row=3,pady=3)
    ttk.Label(win_book1,text=date_of_dep.get(),foreground = "green").grid(column=1,row=3,pady=3)
    ttk.Label(win_book1,text="From:",foreground = "blue").grid(column=0,row=4,pady=3)
    ttk.Label(win_book1,text=data1[2],foreground = "green").grid(column=1,row=4,pady=3)
    ttk.Label(win_book1,text="To:",foreground = "blue").grid(column=0,row=5,pady=3)
    ttk.Label(win_book1,text=data1[3],foreground = "green").grid(column=1,row=5,pady=3)
    ttk.Label(win_book1,text="Departure time",foreground = "blue").grid(column=0,row=6,pady=3)
    ttk.Label(win_book1,text=data1[5],foreground = "green").grid(column=1,row=6,pady=3)
    ttk.Label(win_book1,text="Arrival Time:",foreground = "blue").grid(column=0,row=7,pady=3)
    ttk.Label(win_book1,text=data1[7],foreground = "green").grid(column=1,row=7,pady=3)
    ttk.Label(win_book1,text="Enter your name:").grid(column=6,row=0,pady=3)
    global name
    name = tk.StringVar()
    name_ent = ttk.Entry(win_book1,width=20,textvariable = name)
    name_ent.grid(column=7,row=0,padx=5)
    global age
    age = tk.IntVar()
    ttk.Label(win_book1,text = "Enter your age:").grid(column=6,row=1,pady=3,padx=5)
    age_ent = ttk.Entry(win_book1,width=3,textvariable = age)
    age_ent.grid(column=7,row=1)
    global gender
    gender = tk.StringVar()
    ttk.Label(win_book1,text = "Select your gender:").grid(column=6,row=2,pady=3)
    gender_ent = ttk.Combobox(win_book1,width=7,textvariable = gender,state='readonly')
    gender_ent['values'] = ('Male','Female')
    gender_ent.grid(column=7,row=2)
    ttk.Label(win_book1,text="Enter your mobile number").grid(column=6,row=3,pady=3)
    global mob
    mob = tk.IntVar()
    mob_ent = ttk.Entry(win_book1,width=10,textvariable=mob)
    mob_ent.grid(column=7,row=3,padx=2)
    ttk.Label(win_book1,text="Enter your email-id:").grid(column=6,row=4,pady=3)
    global email
    email = tk.StringVar()
    email_ent = ttk.Entry(win_book1,width=35,textvariable=email)
    email_ent.grid(column=7,row=4,padx=2)

    book1_conf = ttk.Button(win_book1,text="Submit",command = submit_f1)
    book1_conf.grid(column=7,row=7,pady=4)

def book_2():
    win_book1 = tk.Toplevel()
    win_book1.title('Booking for '+data2[1])
    bg = Image.open('images\\'+data2[1]+'.png')
    global copy_bg
    copy_bg = bg.copy()
    bg = ImageTk.PhotoImage(bg)
    global bg_label
    bg_label = ttk.Label(win_book1,image=bg)
    bg_label.photo= bg
    bg_label.image = bg
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.bind('<Configure>', resize_image)
    ttk.Label(win_book1,text="You have opted for:",foreground = "red").grid(column=0,row=0)
    ttk.Label(win_book1,text="Flight no:",foreground = "blue").grid(column=0,row=1,pady=3)
    ttk.Label(win_book1,text=data2[0],foreground = "green").grid(column=1,row=1,pady=3)
    ttk.Label(win_book1,text="Airline:",foreground = "blue").grid(column=0,row=2,pady=3)
    ttk.Label(win_book1,text=data2[1],foreground = "green").grid(column=1,row=2,pady=3)
    ttk.Label(win_book1,text="Date of departure:",foreground = "blue").grid(column=0,row=3,pady=3)
    ttk.Label(win_book1,text=date_of_dep.get(),foreground = "green").grid(column=1,row=3,pady=3)
    ttk.Label(win_book1,text="From:",foreground = "blue").grid(column=0,row=4,pady=3)
    ttk.Label(win_book1,text=data2[2],foreground = "green").grid(column=1,row=4,pady=3)
    ttk.Label(win_book1,text="To:",foreground = "blue").grid(column=0,row=5,pady=3)
    ttk.Label(win_book1,text=data2[3],foreground = "green").grid(column=1,row=5,pady=3)
    ttk.Label(win_book1,text="Departure time",foreground = "blue").grid(column=0,row=6,pady=3)
    ttk.Label(win_book1,text=data2[5],foreground = "green").grid(column=1,row=6,pady=3)
    ttk.Label(win_book1,text="Arrival Time:",foreground = "blue").grid(column=0,row=7,pady=3)
    ttk.Label(win_book1,text=data2[7],foreground = "green").grid(column=1,row=7,pady=3)
    ttk.Label(win_book1,text="Enter your name:").grid(column=5,row=0,pady=3)
    global name
    name=tk.StringVar()
    name_ent = ttk.Entry(win_book1,width=20,textvariable = name)
    name_ent.grid(column=6,row=0)
    global age
    age = tk.IntVar()
    ttk.Label(win_book1,text = "Enter your age:").grid(column=5,row=1,pady=3)
    age_ent = ttk.Entry(win_book1,width=3,textvariable = age)
    age_ent.grid(column=6,row=1)
    global gender
    gender = tk.StringVar()
    ttk.Label(win_book1,text = "Select your gender:").grid(column=5,row=2,pady=3)
    gender_ent = ttk.Combobox(win_book1,width=7,textvariable = gender,state='readonly')
    gender_ent['values'] = ('Male','Female')
    gender_ent.grid(column=6,row=2)
    ttk.Label(win_book1,text="Enter your mobile number").grid(column=5,row=3,pady=3)
    global mob
    mob = tk.IntVar()
    mob_ent = ttk.Entry(win_book1,width=10,textvariable=mob)
    mob_ent.grid(column=6,row=3,padx=2)
    ttk.Label(win_book1,text="Enter your email-id:").grid(column=5,row=4,pady=3)
    global email
    email = tk.StringVar()
    email_ent = ttk.Entry(win_book1,width=35,textvariable=email)
    email_ent.grid(column=6,row=4,padx=2)

    book1_conf = ttk.Button(win_book1,text="Submit",command = submit_f2)
    book1_conf.grid(column=5,row=5,pady=4)

def book_3():
    win_book1 = tk.Toplevel()
    win_book1.title('Booking for '+data3[1])
    bg = Image.open('images\\'+data3[1]+'.png')
    global copy_bg
    copy_bg = bg.copy()
    bg = ImageTk.PhotoImage(bg)
    global bg_label
    bg_label = ttk.Label(win_book1,image=bg)
    bg_label.photo= bg
    bg_label.image = bg
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.bind('<Configure>', resize_image)
    ttk.Label(win_book1,text="You have opted for:",foreground = "red").grid(column=0,row=0)
    ttk.Label(win_book1,text="Flight no:",foreground = "blue").grid(column=0,row=1,pady=3)
    ttk.Label(win_book1,text=data3[0],foreground = "green").grid(column=1,row=1,pady=3)
    ttk.Label(win_book1,text="Airline:",foreground = "blue").grid(column=0,row=2,pady=3)
    ttk.Label(win_book1,text=data3[1],foreground = "green").grid(column=1,row=2,pady=3)
    ttk.Label(win_book1,text="Date of departure:",foreground = "blue").grid(column=0,row=3,pady=3)
    ttk.Label(win_book1,text=date_of_dep.get(),foreground = "green").grid(column=1,row=3,pady=3)
    ttk.Label(win_book1,text="From:",foreground = "blue").grid(column=0,row=4,pady=3)
    ttk.Label(win_book1,text=data3[2],foreground = "green").grid(column=1,row=4,pady=3)
    ttk.Label(win_book1,text="To:",foreground = "blue").grid(column=0,row=5,pady=3)
    ttk.Label(win_book1,text=data3[3],foreground = "green").grid(column=1,row=5,pady=3)
    ttk.Label(win_book1,text="Departure time",foreground = "blue").grid(column=0,row=6,pady=3)
    ttk.Label(win_book1,text=data3[5],foreground = "green").grid(column=1,row=6,pady=3)
    ttk.Label(win_book1,text="Arrival Time:",foreground = "blue").grid(column=0,row=7,pady=3)
    ttk.Label(win_book1,text=data3[7],foreground = "green").grid(column=1,row=7,pady=3)
    ttk.Label(win_book1,text="Enter your name:",foreground = "blue").grid(column=5,row=0,pady=3)
    global name
    name=tk.StringVar()
    name_ent = ttk.Entry(win_book1,width=20,textvariable = name)
    name_ent.grid(column=6,row=0)
    global age
    age = tk.IntVar()
    ttk.Label(win_book1,text = "Enter your age:").grid(column=5,row=1,pady=3)
    age_ent = ttk.Entry(win_book1,width=3,textvariable = age)
    age_ent.grid(column=6,row=1)
    global gender
    gender = tk.StringVar()
    ttk.Label(win_book1,text = "Select your gender:").grid(column=5,row=2,pady=3)
    gender_ent = ttk.Combobox(win_book1,width=7,textvariable = gender,state='readonly')
    gender_ent['values'] = ('Male','Female')
    gender_ent.grid(column=6,row=2)
    ttk.Label(win_book1,text="Enter your mobile number").grid(column=5,row=3,pady=3)
    global mob
    mob = tk.IntVar()
    mob_ent = ttk.Entry(win_book1,width=10,textvariable=mob)
    mob_ent.grid(column=6,row=3,padx=2)
    ttk.Label(win_book1,text="Enter your email-id:").grid(column=5,row=4,pady=3)
    global email
    email = tk.StringVar()
    email_ent = ttk.Entry(win_book1,width=35,textvariable=email)
    email_ent.grid(column=6,row=4,padx=2)

    book1_conf = ttk.Button(win_book1,text="Submit",command = submit_f3)
    book1_conf.grid(column=5,row=5,pady=4)
    
    
    
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_bg.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    bg_label.config(image = photo)
    bg_label.image = photo

def search_flight():
        if date_of_dep.get() == "":
            msg.showwarning("Traveller_io says:","Please specify the date of departure.")
        if city_dep.get()=="":
            msg.showwarning("Traveller_io says:","Please specify the city of departure.")
        elif city_arr.get()=="":
           msg.showwarning("Traveller_io says:","Please specify the city of arrival.")
        elif city_dep.get() == city_arr.get():
            msg.showwarning("Travrller.io says","City of departure cannot be the same as city of arrival.")
        else:
            con = sqltor.connect(host='localhost',user='root',passwd='amal2003',database='traveller_io')
            c = con.cursor()
            c.execute(('select * from flight_schedule where city_dep="{}" and city_arr= "{}"').format(city_dep.get(),city_arr.get()))
            global data1
            data1 = c.fetchone()
            print(data1)
            if data1 == None:
                msg.showinfo("Traveller_io says:","No flights available for the particular schedule.")
            else:
                win_flight_book = tk.Toplevel()
                bg = Image.open('images\\plane1.png') 
                global copy_bg
                copy_bg = bg.copy()
                bg = ImageTk.PhotoImage(bg)
                global bg_label
                bg_label = ttk.Label(win_flight_book,image=bg)
                bg_label.photo= bg
                bg_label.image = bg
                bg_label.place(x=0, y=0, relwidth=1, relheight=1)
                bg_label.bind('<Configure>', resize_image)
                win_flight_book.title("Flights available")
                ttk.Label(win_flight_book,text='Flight 1',foreground = "red").grid(column=0,row=2)
                ttk.Label(win_flight_book,text="Flight.No:",foreground = "blue").grid(column=0,row=3)
                ttk.Label(win_flight_book,text=data1[0],foreground = "green").grid(column=1,row=3)
                ttk.Label(win_flight_book,text="Airline:",foreground = "blue").grid(column=0,row=4)
                ttk.Label(win_flight_book,text=data1[1],foreground = "green").grid(column=1,row=4)
                ttk.Label(win_flight_book,text="From:",foreground = "blue").grid(column=0,row=5)
                ttk.Label(win_flight_book,text=data1[2],foreground = "green").grid(column=1,row=5)
                ttk.Label(win_flight_book,text="To:",foreground = "blue").grid(column=0,row=6)
                ttk.Label(win_flight_book,text=data1[3],foreground = "green").grid(column=1,row=6)
                ttk.Label(win_flight_book,text="Date of departure:",foreground = "blue").grid(column=0,row=7)
                ttk.Label(win_flight_book,text=date_of_dep.get(),foreground = "green").grid(column=1,row=7)
                ttk.Label(win_flight_book,text="Time of Departure:",foreground = "blue").grid(column=0,row=8)
                ttk.Label(win_flight_book,text=data1[5],foreground = "green").grid(column=1,row=8)
                ttk.Label(win_flight_book,text="Time of Arrival:",foreground = "blue").grid(column=0,row=9)
                ttk.Label(win_flight_book,text=data1[7],foreground = "green").grid(column=1,row=9)
                book1 = ttk.Button(win_flight_book,text="Book Flight 1",command=book_1)
                book1.grid(column=0,row=10,pady=3)
                global data2
                data2=c.fetchone()
                ttk.Label(win_flight_book,text='Flight 2',foreground = "red").grid(column=4,row=2)
                ttk.Label(win_flight_book,text="Flight.No:",foreground = "blue").grid(column=4,row=3)
                ttk.Label(win_flight_book,text=data2[0],foreground = "green").grid(column=5,row=3)
                ttk.Label(win_flight_book,text="Airline:",foreground = "blue").grid(column=4,row=4)
                ttk.Label(win_flight_book,text=data2[1],foreground = 'green').grid(column=5,row=4)
                ttk.Label(win_flight_book,text="From:",foreground  = "blue").grid(column=4,row=5)
                ttk.Label(win_flight_book,text=data2[2],foreground = "green").grid(column=5,row=5)
                ttk.Label(win_flight_book,text="To:",foreground = "blue").grid(column=4,row=6)
                ttk.Label(win_flight_book,text=data2[3],foreground = "green").grid(column=5,row=6)
                ttk.Label(win_flight_book,text="Date of departure:",foreground = "blue").grid(column=4,row=7)
                ttk.Label(win_flight_book,text=date_of_dep.get(),foreground = "green").grid(column=5,row=7)
                ttk.Label(win_flight_book,text="Time of Departure:",foreground = "blue").grid(column=4,row=8)
                ttk.Label(win_flight_book,text=data2[5],foreground = "green").grid(column=5,row=8)
                ttk.Label(win_flight_book,text="Time of Arrival:",foreground = "blue").grid(column=4,row=9)
                ttk.Label(win_flight_book,text=data2[7],foreground = "green").grid(column=5,row=9)
                book2 = ttk.Button(win_flight_book,text="Book Flight 2",command = book_2)
                book2.grid(column=4,row=10,pady=5)
                global data3
                data3=c.fetchone()
                ttk.Label(win_flight_book,text='Flight 3',foreground = "red").grid(column=8,row=2)
                ttk.Label(win_flight_book,text="Flight.No:",foreground = "blue").grid(column=8,row=3)
                ttk.Label(win_flight_book,text=data3[0],foreground = "green").grid(column=9,row=3)
                ttk.Label(win_flight_book,text="Airline:",foreground = "blue").grid(column=8,row=4)
                ttk.Label(win_flight_book,text=data3[1],foreground = "green").grid(column=9,row=4)
                ttk.Label(win_flight_book,text="From:",foreground = "blue").grid(column=8,row=5)
                ttk.Label(win_flight_book,text=data3[2],foreground = "green").grid(column=9,row=5)
                ttk.Label(win_flight_book,text="To:",foreground = "blue").grid(column=8,row=6)
                ttk.Label(win_flight_book,text=data3[3],foreground = "green").grid(column=9,row=6)
                ttk.Label(win_flight_book,text="Date of departure:",foreground = "blue").grid(column=8,row=7)
                ttk.Label(win_flight_book,text=date_of_dep.get(),foreground = "green").grid(column=9,row=7)
                ttk.Label(win_flight_book,text="Time of Departure:",foreground = "blue").grid(column=8,row=8)
                ttk.Label(win_flight_book,text=data3[5],foreground = "green").grid(column=9,row=8)
                ttk.Label(win_flight_book,text="Time of Arrival:",foreground = "blue").grid(column=8,row=9)
                ttk.Label(win_flight_book,text=data3[7],foreground = "green").grid(column=9,row=9)
                book3 = ttk.Button(win_flight_book,text="Book Flight 3",command=book_3)
                book3.grid(column=8,row=10,pady=3)
    
    
        
        
def optsel():
    win_flight = tk.Toplevel()
    win_main.minsize()
    bg = Image.open('images\\plane.png')
    global copy_bg
    copy_bg = bg.copy()
    bg = ImageTk.PhotoImage(bg)
    global bg_label
    bg_label = ttk.Label(win_flight,image=bg)
    bg_label.photo= bg
    bg_label.image = bg
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.bind('<Configure>', resize_image)
    win_flight.title('Traveller.io Flight booking portal')
    ttk.Label(win_flight,text='Enter the details below to filter flights available:',foreground = "red",font = ('times',16)).grid(row=0,column=0,padx = 7,pady = 5)
    global date_of_dep
    date_of_dep = tk.StringVar()
    global city_dep
    city_dep = tk.StringVar()
    global city_arr
    city_arr = tk.StringVar()
    
    ttk.Label(win_flight,text = "Enter Date of departure in dd-mm-yyyy format:",foreground = "blue",font = ('times',12)).grid(column=0,row=3)
    date_of_dep_ent = ttk.Entry(win_flight,width = 10,textvariable = date_of_dep)
    date_of_dep_ent.grid(column=0,row=4,pady = 5)
    ttk.Label(win_flight,text="Choose city of departure",foreground = "blue",font = ('times',12)).grid(column=0,row=6)
    city_dep_ent = ttk.Combobox(win_flight,width = 27,textvariable = city_dep,state = 'readonly')
    city_dep_ent['values'] = ("Amritsar(ATO)","Bangalore(BLR)","Calicut(CCJ)","Chennai(MAA)","Hyderabad(HYD)","Cochin(COK)","Kolkata(CCU)","Mumbai(BOM)","New Delhi(DEL)","Vasco da Gama(GOI)")
    city_dep_ent.grid(column = 0,row=7,pady=5)
    ttk.Label(win_flight,text = "Choose destination city",foreground = "blue",font = ('times',12)).grid(column=0,row=8)
    city_arr_ent = ttk.Combobox(win_flight,width = 27,textvariable = city_arr,state = 'readonly')
    city_arr_ent['values'] = ("Amritsar(ATO)","Bangalore(BLR)","Calicut(CCJ)","Chennai(MAA)","Hyderabad(HYD)","Cochin(COK)","Kolkata(CCU)","Mumbai(BOM)","New Delhi(DEL)","Vasco da Gama(GOI)")
    city_arr_ent.grid(column=0,row=9,pady=5)
    search = ttk.Button(win_flight,text = "Search flight",command = search_flight)
    search.grid(column=0,row=10,pady=5)
    win_flight.geometry('600x300')
    win_flight.mainloop()
        
win_main = tk.Tk()
win_main.iconbitmap("images\\travel.ico")
win_main.title('Traveller.io Home Screen')
win_main.geometry('300x230')
bg_main = tk.PhotoImage(file = 'images\\travel.png')
win_main.geometry('500x430')
bg_main_label = ttk.Label(win_main, image=bg_main)
bg_main_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_main_label.photo= bg_main
bg_main_label.image = bg_main
ttk.Label(win_main,text="Welcome to Traveller.io flight reservation portal",foreground = "red",font = ('times',16)).grid(column=0,row=0)
start = ttk.Button(win_main,text = "Book now",command = optsel)
start.grid(column = 0, row = 5,padx = 5,pady=5)

win_main.mainloop()