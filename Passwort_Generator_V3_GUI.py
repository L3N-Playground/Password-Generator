from tkinter import*
from tkinter import messagebox
from random import randint


def password():
    try:
        pw_length = int(entrynumber.get())

        abc = r'-_=!?qwertzuiopasdfghjklyxcvbnm-_=!?QWERTZUIOPASDFGHJKLYXCVBNM-_=!?1234567890-_=!?'
        mypass = ''
        for i in range(pw_length):
            r = randint(0, len(abc)-1)
            mypass += abc[r]
        #return mypass
        print(mypass)

        labeloutput.config(text=mypass)

    except ValueError:
        messagebox.showwarning("Warning", "Error: Only Numbers Accepted")
##########################################
def close():
    exit()


##########################################
tkfenster = Tk()
tkfenster.title ("Password Generator")
tkfenster.geometry ("800x400")
##########################################
label2=Label (master=tkfenster,bg='green' ,text="Enter a Number:")
label2.place (x=10,y=175,width=300,height=50)
label2.config (font=("Arial", 20))
##########################################
label1=Label (master=tkfenster,bg='green' ,text="Password:")
label1.place (x=10,y=250,width=300,height=50)
label1.config (font=("Arial", 20))
##########################################
entrynumber=Entry(master=tkfenster)
entrynumber.place(x=350,y=175,width=300,height=50)
##########################################
buttonergenerate=Button(master=tkfenster,bg='purple',text='Generate',command=password)
buttonergenerate.place (x=350,y=325,width=100,height=50)
buttonergenerate.config (font=("Arial", 10))
##########################################
labeloutput=Label (master=tkfenster,bg='red' ,text="?")
labeloutput.place (x=350,y=250,width=300,height=50)
##########################################
buttonclose=Button(master=tkfenster,bg='red',text='Close',command=close)
buttonclose.place (x=550,y=325,width=100,height=50)
buttonclose.config (font=("Arial", 10))
##########################################
tkfenster.mainloop()



