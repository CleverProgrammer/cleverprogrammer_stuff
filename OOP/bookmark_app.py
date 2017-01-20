import tkinter as tk
import webbrowser

URL = 'https://cleverprogrammer.com'


# Event handler function
def doorbell(event):
    print("You rang the doorbell!!")


def open_cp(event):
    webbrowser.open_new_tab(URL)


def cp_blog(event):
    webbrowser.open_new_tab(URL + "/blog")


window = tk.Tk()
window.geometry("300x200")

alabel = tk.Label(text="Banana")
alabel.grid(column=0, row=0)

blabel = tk.Label(text="Home")
blabel.grid(column=1, row=0)

clabel = tk.Label(text="Blog")
clabel.grid(column=2, row=0)

button = tk.Button(window, text="Doorbell")
button.grid(column=0)

button2 = tk.Button(window, text="Clever Programmer")
button2.grid(column=1, row=1)

button3 = tk.Button(window, text="CP Blog")
button3.grid(column=2, row=1)

button.bind("<Button-1>", doorbell)
button2.bind("<Button-1>", open_cp)
button3.bind("<Button-1>", cp_blog)

window.mainloop()
