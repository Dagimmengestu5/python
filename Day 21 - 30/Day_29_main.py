from tkinter import *
win = Tk()
win.title("Password Manager")
win.config(pady=50, padx=50)
canvas = Canvas(height=200 , width=200)
log_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=log_img)
canvas.grid( row=0, column=1)

# Labels
web_lable = Label(text="Website:")
web_lable.grid(column=0,row=1)
email_label = Label(text="Email/User name:")
email_label.grid(column=0,row=2)
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

# Entry
web_entry = Entry(width=40)
web_entry.grid(column=1,row=1, columnspan=2)
email_entry = Entry(width=40)
email_entry.grid(column=1,row=2, columnspan=2)
Password_entry = Entry(width=40)
Password_entry.grid(column=1,row=3 ,columnspan=2)
# Butten
pass_gen_butten = Button(text="Password Generate")
pass_gen_butten.grid(column=2, row=3)
add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4,columnspan=2)

win.mainloop()