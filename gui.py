#create a user interface for the autoskipad.py

from tkinter import *
from tkinter import messagebox
import webbrowser

window=Tk()
window.title("Auto Skip Ad")
window.geometry("500x500")
window.configure(bg="black")

url="https://github.com/hamad-tariq/Auto-Skip-Ad"

def start():
    messagebox.showinfo("Auto Skip Ad","Auto Skip Ad Started")
    import autoskipad

def stop():
    messagebox.showinfo("Auto Skip Ad","Auto Skip Ad Stopped")
    window.destroy()

def about():
    messagebox.showinfo("Auto Skip Ad",f"""Auto Skip Ad is a python script that automatically skips the youtube ads. \n It is a free and open source software developed by Hammad Tariq. Published on 1st February 2024. \n For more information visit our github page: {url}                    
                        """)

def help():
    messagebox.showinfo("Auto Skip Ad","If you are facing any problem contact us at: \n hammadt451@gmail.com")

def contact():
    messagebox.showinfo("Auto Skip Ad","Contact us at: \n hammadt451@gmail.com")

def exit():
    messagebox.showinfo("Auto Skip Ad","Thank you for using Auto Skip Ad")
    window.destroy()

def main():
    l1=Label(window,text="Auto Skip Ad",font=("Arial Bold",30),bg="black",fg="white")
    l1.place(x=100,y=50)
    b1=Button(window,text="Ad Free Youtube",font=("Arial Bold",15),bg="black",fg="white",command=start)
    b1.place(x=100,y=200)
    b2=Button(window,text="Stop Ad Blocker",font=("Arial Bold",15),bg="black",fg="white",command=stop)
    b2.place(x=300,y=200)
    b3=Button(window,text="About",font=("Arial Bold",15),bg="black",fg="white",command=about)
    b3.place(x=100,y=300)
    b4=Button(window,text="Help",font=("Arial Bold",15),bg="black",fg="white",command=help)
    b4.place(x=300,y=300)
    b5=Button(window,text="Contact",font=("Arial Bold",15),bg="black",fg="white",command=contact)
    b5.place(x=100,y=400)
    b6=Button(window,text="Exit",font=("Arial Bold",15),bg="black",fg="white",command=exit)
    b6.place(x=300,y=400)
    window.mainloop()

if __name__=="__main__":
    main()



