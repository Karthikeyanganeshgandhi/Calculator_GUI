from tkinter import *

user=Tk()
user.title("online calulator/onlinecalculations.ac.in")

entry=Entry(user,justify=CENTER,bg="black",fg="white",width=15,font=(("arial","30")))
entry.place(x=215)

def on_button_click(value):
    present=entry.get()

    if value == "=":
        try:
            out=str(eval(present))
            entry.delete(0,END)
            entry.insert(END,out)

        except:
            entry.delete(0,END)
            entry.insert(END,"error occured")

    elif value == "C":
        entry.delete(0,END)

    else:
        entry.insert(END,value)
    
btn=Button(user,text="7",fg="white",bg="black",activebackground="silver",height=3,width=5,font="5",command=lambda : on_button_click("7"))
btn.place(x=227,y=50)

btn1=Button(user,text="9",bg="black",fg="white",activebackground="silver",height=3,width=5,font="5",command=lambda : on_button_click("9"))
btn1.place(x=390,y=50)


btn2=Button(user,text="8",bg="black",fg="white",activebackground="silver",height=3,width=5,font="5",command=lambda : on_button_click("8"))
btn2.place(x=310,y=50)



btn3=Button(user,text="4",bg="black",fg="white",activebackground="silver",height=3,width=5,font="5",command=lambda : on_button_click("4"))
btn3.place(x=227,y=150)


btn4=Button(user,text="1",bg="black",fg="white",activebackground="silver",height=3,width=5,font="5",command=lambda : on_button_click("1"))
btn4.place(x=227,y=250)


btn5=Button(user,text="5",bg="black",fg="white",activebackground="silver",height=3,width=5,font="5",command=lambda : on_button_click("5"))
btn5.place(x=310,y=150)


btn6=Button(user,text="2",bg="black",fg="white",activebackground="silver",height=3,width=5,font="5",command=lambda : on_button_click("2"))
btn6.place(x=310,y=250)



btn6=Button(user,text="0",bg="black",fg="white",activebackground="silver",height=3,width=5,font="5",command=lambda : on_button_click("0"))
btn6.place(x=310,y=350)
        


btn7=Button(user,text="6",bg="black",fg="white",activebackground="silver",height=3,width=5,font="5",command=lambda : on_button_click("6"))
btn7.place(x=390,y=150)



btn8=Button(user,text="3",bg="black",fg="white",activebackground="silver",height=3,width=5,font="5",command=lambda : on_button_click("3"))
btn8.place(x=390,y=250)



btn9=Button(user,text="C",bg="brown",fg="white",activebackground="silver",height=3,width=5,font="5",command=lambda : on_button_click("C"))
btn9.place(x=227,y=350)



btn9=Button(user,text="=",bg="green",fg="white",activebackground="silver",height=3,width=5,font="5",command=lambda : on_button_click("="))
btn9.place(x=390,y=350)



btn9=Button(user,text="+",bg="dark orange",fg="white",activebackground="silver",height=3,width=5,font="5",command=lambda : on_button_click("+"))
btn9.place(x=470,y=50)



btn9=Button(user,text="-",bg="dark orange",fg="white",activebackground="silver",height=3,width=5,font="5",command=lambda : on_button_click("-"))
btn9.place(x=470,y=150)



btn9=Button(user,text="*",bg="dark orange",fg="white",activebackground="silver",height=3,width=5,font="5",command=lambda : on_button_click("*"))
btn9.place(x=470,y=250)



btn9=Button(user,text="/",bg="dark orange",fg="white",activebackground="silver",height=3,width=5,font="5",command=lambda : on_button_click("/"))
btn9.place(x=470,y=350) 


path=PhotoImage(file="C:/Users/karth/Downloads/fab38714b8aac3775296bc4ea4781ba7.png")
my_image=Label(user,image=path,width=550,height=850)
my_image.place(x=900,y=-50)

lbl=Label(user,text="Welcome To The Digital Calculator",bg="black",fg="white",font=(("normal","30")))
lbl.place(x=90,y=570)
        
user.geometry("900x900")
user.mainloop()
