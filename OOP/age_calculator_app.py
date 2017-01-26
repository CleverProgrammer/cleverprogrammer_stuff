from PIL import Image, ImageTk
import datetime  # we will use this for date objects
import tkinter as tk

window = tk.Tk()
window.title("Age Calculator APP")

window.geometry('400x400')


class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        return age


year_label = tk.Label(text="Year")
year_label.grid(column=0, row=1)

month_label = tk.Label(text="Month")
month_label.grid(column=0, row=2)

day_label = tk.Label(text="Day")
day_label.grid(column=0, row=3)

birth_year = tk.Entry(master=window)
birth_year.grid(column=1, row=1)

birth_month = tk.Entry(master=window)
birth_month.grid(column=1, row=2)

birth_day = tk.Entry(master=window)
birth_day.grid(column=1, row=3)


def calculate_age():
    print(birth_year.get())
    print(birth_month.get())
    print(birth_day.get())
    qazi = Person('Qazi', datetime.date(int(birth_year.get()),
                                        int(birth_month.get()),
                                        int(birth_day.get())))
    print(qazi.age())
    text_answer = tk.Text(master=window, height=20, width=30)
    text_answer.grid(column=1, row=5)
    answer_text = "You are {age} years old!".format(age=qazi.age())
    text_answer.insert(tk.END, answer_text)
    text_answer.tag_configure('bold_italics', font=('Helvetica', 12, 'bold', 'italic'))


button1 = tk.Button(text="Calculate Now!", command=calculate_age)
button1.grid(column=1, row=4)

image = Image.open('/Users/ChessTastic/Documents/Clever Programmer/Brand/Pictures/cp_website_coding.jpg')
image.thumbnail((100, 100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0)

window.mainloop()
