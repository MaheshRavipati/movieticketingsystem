from tkinter import *
import  tkinter as tk
from  tkinter import ttk
root=Tk()
root.configure(bg="#00ee54")
root.geometry("8000x8000")
root.title("CINEMAX")
text=Label(root,text="CINEMAX ",bg="#00ee54")
text.configure(font=("Segoe Script",45,"bold"))
text.place(x=550,y=0)
text1=Label(root,text="BOOK YOUR FAVORITE MOVIE TICKETS HERE ",bg="#00ee54")
text1.configure(font=("Cooper",17,"bold"))
text1.place(x=450,y=89)
text2=Label(root,text="A",bg="#00ee54")
text2.configure(font=("Cooper",15,"bold"))
text2.place(x=0,y=300)
text3=Label(root,text="B",bg="#00ee54")
text3.configure(font=("Cooper",15,"bold"))
text3.place(x=0,y=350)
text4=Label(root,text="C",bg="#00ee54")
text4.configure(font=("Cooper",15,"bold"))
text4.place(x=0,y=400)
text5=Label(root,text="D",bg="#00ee54")
text5.configure(font=("Cooper",15,"bold"))
text5.place(x=0,y=450)    
v=tk.StringVar()
m=tk.StringVar()
z=tk.StringVar()
l=tk.StringVar()
i=tk.StringVar()
a1=Radiobutton(root,variable=v,value="A1",relief=SUNKEN).place(x=45,y=305)
a2=Radiobutton(root,variable=v,value="B1",relief=SUNKEN).place(x=45,y=355)
a3=Radiobutton(root,variable=v,value="C1",relief=SUNKEN).place(x=45,y=405)
a4=Radiobutton(root,variable=v,value="D1",relief=SUNKEN).place(x=45,y=455)
a5=Radiobutton(root,variable=v,value="A2",relief=SUNKEN).place(x=95,y=305)
a6=Radiobutton(root,variable=v,value="B2",relief=SUNKEN).place(x=95,y=355)
a7=Radiobutton(root,variable=v,value="C2",relief=SUNKEN).place(x=95,y=405)
a8=Radiobutton(root,variable=v,value="D2",relief=SUNKEN).place(x=95,y=455)
a9=Radiobutton(root,variable=v,value="A3",relief=SUNKEN).place(x=145,y=305)
a10=Radiobutton(root,variable=v,value="B3",relief=SUNKEN).place(x=145,y=355)
a11=Radiobutton(root,variable=v,value="C3",relief=SUNKEN).place(x=145,y=405)
a12=Radiobutton(root,variable=v,value="D3",relief=SUNKEN).place(x=145,y=455)
a13=Radiobutton(root,variable=v,value="A4",relief=SUNKEN).place(x=195,y=305)
a14=Radiobutton(root,variable=v,value="B4",relief=SUNKEN).place(x=195,y=355)
a15=Radiobutton(root,variable=v,value="C4",relief=SUNKEN).place(x=195,y=405)
a16=Radiobutton(root,variable=v,value="D4",relief=SUNKEN).place(x=195,y=455)
a17=Radiobutton(root,variable=v,value="A5",relief=SUNKEN).place(x=245,y=305)
a18=Radiobutton(root,variable=v,value="B5",relief=SUNKEN).place(x=245,y=355)
a19=Radiobutton(root,variable=v,value="C5",relief=SUNKEN).place(x=245,y=405)
a20=Radiobutton(root,variable=v,value="D5",relief=SUNKEN).place(x=245,y=455)
a21=Radiobutton(root,variable=v,value="A6",relief=SUNKEN).place(x=295,y=305)
a22=Radiobutton(root,variable=v,value="B6",relief=SUNKEN).place(x=295,y=355)
a23=Radiobutton(root,variable=v,value="C6",relief=SUNKEN).place(x=295,y=405)
a24=Radiobutton(root,variable=v,value="D6",relief=SUNKEN).place(x=295,y=455)
a25=Radiobutton(root,variable=v,value="A7",relief=SUNKEN).place(x=345,y=305)
a26=Radiobutton(root,variable=v,value="B7",relief=SUNKEN).place(x=345,y=355)
a27=Radiobutton(root,variable=v,value="C7",relief=SUNKEN).place(x=345,y=405)
a28=Radiobutton(root,variable=v,value="D7",relief=SUNKEN).place(x=345,y=455)
a29=Radiobutton(root,variable=v,value="A8",relief=SUNKEN).place(x=395,y=305)
a30=Radiobutton(root,variable=v,value="B8",relief=SUNKEN).place(x=395,y=355)
a31=Radiobutton(root,variable=v,value="C8",relief=SUNKEN).place(x=395,y=405)
a32=Radiobutton(root,variable=v,value="D8",relief=SUNKEN).place(x=395,y=455)
a33=Radiobutton(root,variable=v,value="A9",relief=SUNKEN).place(x=445,y=305)
a34=Radiobutton(root,variable=v,value="B9",relief=SUNKEN).place(x=445,y=355)
a35=Radiobutton(root,variable=v,value="C9",relief=SUNKEN).place(x=445,y=405)
a36=Radiobutton(root,variable=v,value="D9",relief=SUNKEN).place(x=445,y=455)
a37=Radiobutton(root,variable=v,value="A10",relief=SUNKEN).place(x=495,y=305)
a38=Radiobutton(root,variable=v,value="B10",relief=SUNKEN).place(x=495,y=355)
a39=Radiobutton(root,variable=v,value="C10",relief=SUNKEN).place(x=495,y=405)
a40=Radiobutton(root,variable=v,value="D10",relief=SUNKEN).place(x=495,y=455)
a41=Radiobutton(root,variable=v,value="A11",relief=SUNKEN).place(x=545,y=305)
a42=Radiobutton(root,variable=v,value="B11",relief=SUNKEN).place(x=545,y=355)
a43=Radiobutton(root,variable=v,value="C11",relief=SUNKEN).place(x=545,y=405)
a44=Radiobutton(root,variable=v,value="D11",relief=SUNKEN).place(x=545,y=455)
a45=Radiobutton(root,variable=v,value="A12",relief=SUNKEN).place(x=595,y=305)
a46=Radiobutton(root,variable=v,value="B12",relief=SUNKEN).place(x=595,y=355)
a47=Radiobutton(root,variable=v,value="C12",relief=SUNKEN).place(x=595,y=405)
a48=Radiobutton(root,variable=v,value="D12",relief=SUNKEN).place(x=595,y=455)
a49=Radiobutton(root,variable=v,value="A13",relief=SUNKEN).place(x=645,y=305)
a50=Radiobutton(root,variable=v,value="B13",relief=SUNKEN).place(x=645,y=355)
a51=Radiobutton(root,variable=v,value="C13",relief=SUNKEN).place(x=645,y=405)
a52=Radiobutton(root,variable=v,value="D13",relief=SUNKEN).place(x=645,y=455)
a53=Radiobutton(root,variable=v,value="A14",relief=SUNKEN).place(x=695,y=305)
a54=Radiobutton(root,variable=v,value="B14",relief=SUNKEN).place(x=695,y=355)
a55=Radiobutton(root,variable=v,value="C14",relief=SUNKEN).place(x=695,y=405)
a56=Radiobutton(root,variable=v,value="D14",relief=SUNKEN).place(x=695,y=455)
a57=Radiobutton(root,variable=v,value="A15",relief=SUNKEN).place(x=745,y=305)
a58=Radiobutton(root,variable=v,value="B15",relief=SUNKEN).place(x=745,y=355)
a59=Radiobutton(root,variable=v,value="C15",relief=SUNKEN).place(x=745,y=405)
a60=Radiobutton(root,variable=v,value="D15",relief=SUNKEN).place(x=745,y=455)
a61=Radiobutton(root,variable=v,value="A16",relief=SUNKEN).place(x=795,y=305)
a62=Radiobutton(root,variable=v,value="B16",relief=SUNKEN).place(x=795,y=355)
a63=Radiobutton(root,variable=v,value="C16",relief=SUNKEN).place(x=795,y=405)
a64=Radiobutton(root,variable=v,value="D16",relief=SUNKEN).place(x=795,y=455)
a65=Radiobutton(root,variable=v,value="A17",relief=SUNKEN).place(x=845,y=305)
a66=Radiobutton(root,variable=v,value="B17",relief=SUNKEN).place(x=845,y=355)
a67=Radiobutton(root,variable=v,value="C17",relief=SUNKEN).place(x=845,y=405)
a68=Radiobutton(root,variable=v,value="D17",relief=SUNKEN).place(x=845,y=455)
a69=Radiobutton(root,variable=v,value="A18",relief=SUNKEN).place(x=895,y=305)
a70=Radiobutton(root,variable=v,value="B18",relief=SUNKEN).place(x=895,y=355)
a71=Radiobutton(root,variable=v,value="C18",relief=SUNKEN).place(x=895,y=405)
a72=Radiobutton(root,variable=v,value="D18",relief=SUNKEN).place(x=895,y=455)
a73=Radiobutton(root,variable=v,value="A19",relief=SUNKEN).place(x=945,y=305)
a74=Radiobutton(root,variable=v,value="B19",relief=SUNKEN).place(x=945,y=355)
a75=Radiobutton(root,variable=v,value="C19",relief=SUNKEN).place(x=945,y=405)
a76=Radiobutton(root,variable=v,value="D19",relief=SUNKEN).place(x=945,y=455)
a77=Radiobutton(root,variable=v,value="A20",relief=SUNKEN).place(x=995,y=305)
a78=Radiobutton(root,variable=v,value="B20",relief=SUNKEN).place(x=995,y=355)
a79=Radiobutton(root,variable=v,value="C20",relief=SUNKEN).place(x=995,y=405)
a80=Radiobutton(root,variable=v,value="D20",relief=SUNKEN).place(x=995,y=455)
button=Button(root,text="PROCEED TO PAY & BOOK",bg="blue",padx=20,pady=20,command=lambda : print("\n\n --------------------Download Your Movie--------------------\n\n""MOVIE : SYERAA Narasimhareddy\n""Theatre:",m.get(),"\nShow:",z.get(),"\nyour seat number :",v.get(),"\nPayment thro0ugh:",l.get(),"\nDate:",i.get()))
button.configure(font=("Rockwell Nova",10,"bold"))
button.place(x=420,y=500)
theatres=["GEETHA APSARA ","KUMARI ","RAMBA","SURYA PALACE"]
show=["Morning show","Matnee","Firstshow","Second show"]
payment=["paytm","creditcard","phonepe","googlepay","debitcard"]
date=["14-OCT","15-OCT","16-OCT","17-OCT"]
cb1=ttk.Combobox(root,values=theatres,textvariable=m)
cb2=ttk.Combobox(root,values=show,textvariable=z)
cb3=ttk.Combobox(root,values=payment,textvariable=l)
cb4=ttk.Combobox(root,values=date,textvariable=i)
cb1.place(x=20,y=200)
cb2.place(x=250,y=200)
cb3.place(x=470,y=200)
cb4.place(x=700,y=200)
a81=Label(root,text="Theatres",bg="#00ee54")
a81.configure(font=("Rockwell Nova",10,"bold"))
a81.place(x=45,y=226)
a82=Label(root,text="Select Show",bg="#00ee54")
a82.configure(font=("Rockwell Nova",10,"bold"))
a82.place(x=255,y=226)
a83=Label(root,text="Payment through",bg="#00ee54")
a83.configure(font=("Rockwell Nova",10,"bold"))
a83.place(x=475,y=226)
a84=Label(root,text="Date",bg="#00ee54")
a84.configure(font=("Rockwell Nova",10,"bold"))
a84.place(x=725,y=226)
canvas=Canvas(root, width=390, height = 248)
canvas.place(x=1100,y=175)
hello=PhotoImage(file='C:\\Users\\Mahesh\\Pictures\\image1.png')
canvas.create_image(0,0,anchor=NW,image=hello)
can=Canvas(root,width=391,height=300)
can.place(x=1101,y=426)
can1=PhotoImage(file='C:\\Users\\Mahesh\\Pictures\image2.png')
can.create_image(0,0,anchor=NW,image=can1)
a85=Label(root,text="SYEREAA NARASIMHA REDDY")
a85.configure(font=("Cooper",18,"bold"))
a85.place(x=1115,y=150)
root.mainloop()
