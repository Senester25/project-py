from tkinter import *
from __init__ import *

root = Tk()  # จอเริ่ม
root.title("Pledge program")  # ชื่อหัวข้อ
# root.geometry("700x500+100+100") #ขนาดจอ+x+y


class openinp:

    def __init__(self):
        inp = Tk()
        inp.title("Input")

        self.list = []
        self.serial_number_lb = Label(
            inp, text="Serial-number:", fg="black", font=200).grid(row=2, column=1, pady=5)
        self.weight_lb = Label(inp, text="Weight:", fg="black", font=200).grid(
            row=4, column=1, pady=5)
        self.type_lb = Label(inp, text="Type:", fg="black",
                             font=200).grid(row=6, column=1, pady=5)
        self.value_lb = Label(inp, text="value:", fg="black", font=200).grid(
            row=8, column=1, pady=5)

        self.serial_number_var = StringVar()
        self.serial_number_ent = Entry(inp)
        self.serial_number_ent.grid(row=2, column=2, pady=5)
        self.weight_var = StringVar()
        self.weight_ent = Entry(inp)
        self.weight_ent.grid(row=4, column=2, pady=5)
        self.type_var = StringVar()
        self.type_ent = Entry(inp)
        self.type_ent.grid(row=6, column=2, pady=5)
        self.value_var = StringVar()
        self.value_ent = Entry(inp)
        self.value_ent.grid(row=8, column=2, pady=5)

        self.btfinish = Button(inp, text="Finish", fg="black", font=200, bg="yellow",
                               command=self.show).grid(row=10, column=5, columnspan=2, pady=5)
        self.btclear = Button(inp, text="Clear", fg="black", font=200, bg="red",
                              command=self.clear).grid(row=11, column=5, columnspan=2, pady=5)

    def show(self):  # แสดงค่าในpython
        self.serial_number_var = self.serial_number_ent.get()
        self.weight_var = self.weight_ent.get()
        self.type_var = self.type_ent.get()
        self.value_var = self.value_ent.get()

        data_in = [self.serial_number_var,
                   self.weight_var, self.type_var, self.value_var]
        new_data(data_in)

    def clear(self):  # ลบค่าในตาราง
        self.serial_number_ent.delete(0, END)
        self.weight_ent.delete(0, END)
        self.type_ent.delete(0, END)
        self.value_ent.delete(0, END)
        self.list.clear()


root.columnconfigure(0, weight=1)  # หน้า root
welcome = Label(root, text="Welcome to pledge program",
                fg="black", font=200).grid(row=2, column=0, pady=5)
btinput = Button(root, text="Input", fg="black", font=200,
                 bg="green", command=openinp).grid(row=3, column=0, pady=5)
get_txt = StringVar()
box_get = Entry(root, textvariable=get_txt).grid(row=4, column=0, pady=5)
btopen = Button(root, text="OK", fg="black", font=200,
                bg="blue").grid(row=5, column=0, pady=5)



