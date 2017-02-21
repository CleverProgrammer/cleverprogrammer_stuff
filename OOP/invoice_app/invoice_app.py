import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.geometry('800x600')
window.title('Invoice APP')
frame_1 = tk.Frame(master=window, width=300, height=300)

# Let's create the menu
menubar = tk.Menu(window)
file_menu = tk.Menu(menubar, tearoff=0)  # this will be our file menu

menubar.add_cascade(label='File', menu=file_menu)


def cp_print_cp():
    print('Clever Programmer!')


def file_save(event=None):
    # a+ --> add stuff to the end of the file you are writing to
    f = filedialog.asksaveasfile(mode='a+', defaultextension='.txt')

    if f is None:
        return

    # lesson_details_to_save = str('\n' + str((subject_entry.get(), hours_entry.get(), amount_entry.get())))
    lessons_to_save = notes_text.get(0.0, tk.END)
    f.write(lessons_to_save)
    f.close()


def submit_lesson(event=None):
    lesson_details_to_save = '{}, {}, {}\n'.format(subject_entry.get(), hours_entry.get(), amount_entry.get())
    notes_text.insert(tk.END, lesson_details_to_save)


file_menu.add_command(label="Save As", accelerator='Ctrl + S',
                      compound=tk.LEFT, image=None, underline=0, command=file_save)

window.config(menu=menubar)

# radio button boolean variable
paid_tick = tk.BooleanVar()

# Let's make the labels.
subject_label = tk.Label(master=frame_1, text="Lesson Subject")
hours_label = tk.Label(master=frame_1, text="Hours")
amount_label = tk.Label(master=frame_1, text='Amount')
paid_label = tk.Label(master=frame_1, text="Paid")
notes_label = tk.Label(master=frame_1, text='Notes')

# Let's make the entry fields + RadioButton + Textfield
subject_entry = tk.Entry(master=frame_1)
hours_entry = tk.Entry(master=frame_1)
amount_entry = tk.Entry(master=frame_1)
paid_radio_button = tk.Radiobutton(master=frame_1, text='Yes', variable=paid_tick, value=True)
paid_radio_button2 = tk.Radiobutton(master=frame_1, text='No', variable=paid_tick, value=False)
notes_text = tk.Text(master=frame_1, width=40, height=20)
submit_button = tk.Button(master=frame_1, text="Submit", command=submit_lesson)

# bind button
window.bind('<Return>', submit_lesson)

# bind save
window.bind('<Control-s>', file_save)

# Let's put the labels in a GRID geometry manager!
subject_label.grid(row=1, column=0, sticky='w')
hours_label.grid(row=2, column=0, sticky='w')
amount_label.grid(row=3, column=0, sticky='w')
paid_label.grid(row=4, column=0, sticky='w')
notes_label.grid(row=6, column=0, sticky='w')

# Let's put the entry fields in a GRID geometry manager!
subject_entry.grid(row=1, column=1, sticky='e')
hours_entry.grid(row=2, column=1, sticky='e')
amount_entry.grid(row=3, column=1, sticky='e')
paid_radio_button.grid(row=4, column=1, sticky='w')
paid_radio_button2.grid(row=4, column=2)
submit_button.grid(row=5, column=1)
notes_text.grid(row=6, column=1, sticky='e')

# Most importantly, GRID the frame
frame_1.grid(row=0, column=0)

window.mainloop()
