from tkinter import *
windows = Tk()
windows.title("my first GUI")
windows.minsize(width=500, height=400)
word = Label(text="This is the bast of my life")
word.pack(side="top")
# word["text"] = "new text"
word.config(text="hi their")

def click():
    print("yes this is work")
    new = Input.get()
    word.config(text=new)

Input =Entry(width=30 )
Input.pack()
button = Button(text="click me", command=click)
button.pack()



windows.mainloop()