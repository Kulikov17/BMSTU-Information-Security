import wmi
import tkinter as tk
from tkinter import messagebox
from random import randint

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.checkLicense()
        self.root.deiconify()
        self.root.title("Randomizer")
        self.root.geometry('350x200')

        photo = tk.PhotoImage(file="./kolobki_hello.gif")
        label = tk.Label(image=photo)
        label.place(x=90, y=10)

        labelMin = tk.Label(text="Результат:")
        labelMin.place(x=160, y=10)

        self.labelResult = tk.Label(text="", font='Times 20')
        self.labelResult.place(x=160, y=30)

        labelMin = tk.Label(text="Min:")
        labelMin.place(x=90, y=70)

        self.minVal = tk.IntVar(value=0)
        self.minSpinBox = tk.Spinbox(self.root, from_=-10000, to=10000, textvar=self.minVal)
        self.minSpinBox.place(x=125, y=70)


        labelMax = tk.Label(text="Max:")
        labelMax.place(x=90, y=100)

        self.maxVal = tk.IntVar(value=100)
        self.maxSpinBox = tk.Spinbox(self.root, from_=-10000, to=10000, textvar=self.maxVal)
        self.maxSpinBox.place(x=125, y=100)


        button = tk.Button(self.root,
                           text='Сгенерировать число',
                           command=self.generate,
                           )
        button.place(x=90, y=130, width=170)

        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.wm_geometry("+%d+%d" % (x, y))
        self.root.mainloop()

    def generate(self):
        if self.minVal.get() >= self.maxVal.get():
            self.maxVal.set(self.minVal.get() + 1)
        self.labelResult.config(text=str(randint(self.minVal.get(), self.maxVal.get())))


    def quit(self):
        self.root.destroy()

    def checkLicense(self):
        self.root.withdraw()  # Спрятать окно
        try:
            with open('license.key', 'r') as f:
                key = f.read()
                c = wmi.WMI()
                for system in c.Win32_PhysicalMedia():
                    if key != system.SerialNumber:
                        msgBox = messagebox.showerror('Ошибка',
                                'Некорректный лицензионный ключ! Переустановите с помощью installer.py')
                        if msgBox == 'ok':
                            self.quit()
        except:
            msgBox = messagebox.showerror('Ошибка',
                                'Нет лицензионного ключа! Выполните установку с помощью installer.py')
            if msgBox == 'ok':
                self.quit()


try:
    app = App()
except:
    pass

