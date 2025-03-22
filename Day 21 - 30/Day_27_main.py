from tkinter import *


def mile_to_km():
    mile = float(mile_input.get())
    km = mile * 1.609
    calculated_resalt.config(text=f"{km}")


win = Tk()
win.title("convert mile to KM")
win.config(padx=20, pady=20)
mile_input = Entry(width=7)
mile_input.grid(column=1 , row=0 )
#
input_km = Label(text="input yor mile")
input_km.grid(column=2, row=0 )

word_mile = Label(text="Mile")
word_mile.grid(column=2, row=2)

is_equal = Label(text="is equal to")
is_equal.grid(column=0 , row=1 )
#
calculated_resalt = Label(text="0")
calculated_resalt.grid(column=1 , row=1 )

km_word = Label(text="KM")
km_word.grid(column=2 , row=1 )

calculate_beteen = Button(text="Calculate", command=mile_to_km)
calculate_beteen.grid(column=2 , row=2 )

win.mainloop()

#
# windows = Tk()
# windows.title("my first GUI")
# windows.minsize(width=500, height=400)
# word = Label(text="This is the bast of my life")
# word.pack(side="top")
# # word["text"] = "new text"
# word.config(text="hi their")
#
# def click():
#     print("yes this is work")
#     new = Input.get()
#     word.config(text=new)
#
# Input =Entry(width=30 )
# Input.pack()
# button = Button(text="click me", command=click)
# button.pack()

