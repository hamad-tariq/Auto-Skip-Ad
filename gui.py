#create a user interface for the autoskipad.py

from tkinter import *
from tkinter import messagebox
import tkinter
import webbrowser

window=Tk()
window.title("Auto Skip Ad")
window.geometry("1000x800")
window.configure(bg="black")

url="https://github.com/hamad-tariq/Auto-Skip-Ad"

frame= tkinter.Frame(bg="black")

def start():
    messagebox.showinfo("Auto Skip Ad","Auto Skip Ad Started")
    import autoskipad


def stop():
    messagebox.showinfo("Auto Skip Ad","Auto Skip Ad Stopped Successfully. Give a Feedback on Github.")

def gthub():
    webbrowser.open(url)

def lnkdin():
    lk="https://www.linkedin.com/in/hammad-tariq-269623207/"
    webbrowser.open(lk)

def about():
    webbrowser.open(url)

def help():
    webbrowser.open(url)

def contact():
    lntree="https://linktr.ee/hamadtariq"
    webbrowser.open(lntree)

def exit():
    messagebox.showinfo("Auto Skip Ad","Thank you for using Auto Skip Ad")
    window.destroy()

def main():
    l1=Label(frame,text="Auto Skip Ad",font=("Candara",30),bg="black",fg="white")
    l1.grid(row=0,column=0,columnspan=5,pady=40)
    b1=Button(frame,text="Ad Free Youtube",font=("Candara",15),bg="black",fg="white",command=start)
    b1.grid(row=1,column=1,padx=30, pady=40)
    b2=Button(frame,text="Stop Ad Blocker",font=("Candara",15),bg="black",fg="white",command=stop)
    b2.grid(row=1,column=2,padx=30,pady=40)
    b3=Button(frame,text="About the tool",font=("Candara",15),bg="black",fg="white",command=about)
    b3.grid(row=1,column=3,padx=30,pady=40)
    b4=Button(frame,text="User Guide",font=("Candara",15),bg="black",fg="white",command=help)
    b4.grid(row=1,column=4,padx=30,pady=40)
    b5=Button(frame,text="Contact",font=("Candara",15),bg="black",fg="white",command=contact)
    b5.grid(row=2,column=2,pady=40)
    b6=Button(frame,text="Exit",font=("Candara",15),bg="black",fg="white",command=exit)
    b6.grid(row=2,column=3,pady=40)
    l2=Label(frame,text="Developed by Hammad Tariq",font=("Candara",18),bg="black",fg="white")
    l2.grid(row=4,column=0,columnspan=5,pady=20)
    b7=Button(frame,text="Github",font=("Candara",15),bg="black",fg="white",command=gthub)
    b7.grid(row=5,column=2,pady=40)
    b8=Button(frame,text="LinkedIn",font=("Candara",15),bg="black",fg="white",command=lnkdin)
    b8.grid(row=5,column=3,pady=40)
    frame.pack(expand=True)
    window.mainloop()

if __name__=="__main__":
    main()



