from PIL import Image, ImageTk
import datetime
import tkinter as tk

# create frame
window = tk.Tk()

# create frame geometry
window.geometry("400x400")

# set the title of the frame
window.title("Age Calculator APP!")

# adding labels
year_label = tk.Label(text="Year")
year_label.grid(column=0, row=1)

month_label = tk.Label(text="Month")
month_label.grid(column=0, row=2)

day_label = tk.Label(text="Day")
day_label.grid(column=0, row=3)

year_entry = tk.Entry()
year_entry.grid(column=1, row=1)

month_entry = tk.Entry()
month_entry.grid(column=1, row=2)

day_entry = tk.Entry()
day_entry.grid(column=1, row=3)


def calculate_age():
    print(year_entry.get())
    print(month_entry.get())
    print(day_entry.get())
    person = Person('Qazi', datetime.date(int(year_entry.get()),
                                          int(month_entry.get()),
                                          int(day_entry.get())))
    print(person.age())
    text_answer = tk.Text(master=window, height=20, width=30)
    text_answer.grid(column=1, row=5)
    answer_text = "{name} is {age} years old".format(name=person.name, age=person.age())
    text_answer.insert(tk.END, answer_text)


calculate_button = tk.Button(text="Calculate Now!", command=calculate_age)
calculate_button.grid(column=1, row=4)


class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        return age


image = Image.open('/Users/ChessTastic/Documents/Clever Programmer/Brand/Pictures/cp_website_coding.jpg')
image.thumbnail((100, 100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0)
# qazi = Person('Qazi', datetime.date(1940, 8, 20))
# print(qazi.name)
# print(qazi.birthdate)
# print(qazi.age())

window.mainloop()
