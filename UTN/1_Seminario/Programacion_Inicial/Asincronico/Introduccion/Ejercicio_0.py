from customtkinter import *

app = CTk()


def button_on_click():
    print("Vamos a aprenter python!!")


button = CTkButton(master=app, text="Clike me!", command=button_on_click)
button.grid()

app.mainloop()