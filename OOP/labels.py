import tkinter as tk

window = tk.Tk()
window.geometry("300x200")

alabel = tk.Label(text="Banana")
alabel.grid(column=0, row=0)

blabel = tk.Label(text="Apple")
blabel.grid(column=1, row=0)

window.mainloop()
