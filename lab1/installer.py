import wmi
import tkinter as tk
from tkinter import messagebox

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Установщик Randomizer")
        self.root.geometry('320x100')

        photo = tk.PhotoImage(file="./kolobki_hello.gif")
        label = tk.Label(image=photo)
        label.pack()

        button = tk.Button(self.root,
                           text='Установить программу',
                           command=self.messageBox,
                           )
        button.pack()

        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.wm_geometry("+%d+%d" % (x, y))
        self.root.mainloop()

    def quit(self):
        self.root.destroy()

    def messageBox(self):
        c = wmi.WMI()
        for item in c.Win32_PhysicalMedia():
            with open('license.key', 'w') as f:
                f.write(item.SerialNumber)

        msgBox = messagebox.showinfo('Установка', 'Установка была успешна произведена')
        if msgBox == 'ok':
            self.quit()

app = App()