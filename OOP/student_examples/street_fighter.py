""""
Street Fighter: Ryu punches Ken.
By David, 2017
Rafeh Qazi made it work ;)
"""

import tkinter as tk


class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    # function for one fighter to attack another
    def attack(self, other_guy):
        # print(dir(event))
        other_guy.health -= self.damage
        print("{} attacks {} for {} damage, ouch that's gotta hurt!".format(self.name, other_guy.name, self.damage))


ryu = Fighter('Ryu')
ken = Fighter('Ken')

window = tk.Tk()
window.geometry("500x500")
window.bind("<Button-1>", )

ryu_label = tk.Label(text="Ryu")
ryu_label.grid(column=0, row=0)


def button1_callback(event=None):
    ryu.attack(ken)


ryu_attack_button = tk.Button(text="Attack", command=button1_callback)
ryu_attack_button.grid(column=0, row=1)

# *** shortkeyys are binded to FRAMES and NOT buttons. ***
window.bind("<Return>", button1_callback)

ken_label = tk.Label(text="Ken")
ken_label.grid(column=2, row=0)

window.mainloop()
