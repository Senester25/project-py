from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from os import mkdir
from os.path import exists, join
import dbm


db_path = join('pledge/database/')
break_command = "stop"

def create_database(db_path): #สร้างที่เก็บข้อมูล
    if not exists(join(db_path)):
        mkdir(join(db_path))
        print("Database Created!")
    else:
        print('Database already exist!')


def csv_encoder(data): #แปลงdict เป็น str
    result = ''
    for i in data.keys():
        result += data[i] + ', '
    return result[:-2]


def csv_decoder(data): #แปลงstr เปน list
    data = str(data)[2:-1].split(', ')

    d_weight = '{0:,.2f}'.format(round(float(data[0]), 2)) + ' ' + 'g'

    d_type = data[1]

    d_value = '{0:,.2f}'.format(round(float(data[2]), 2)) + ' ' + 'Baht'

    result = {
        'Weight': d_weight,
        'Type': d_type,
        'Value': d_value
    }
    return result


def new_data(data_in):
    def new_data_command():
        serial_number = input('Serial Number: ')
        if serial_number == '':
            return print('database error')
        elif serial_number in db:
            print('Sorry! this name already taken!')
            temp1 = input('\nDo you wanna overwrite the exist one? (Y/N) : ')
            if temp1 != 'Y':
                return
            print('\nSure thing! Please enter the new one!\n')
        elif serial_number == break_command:
            return

        temp, in_data_command = [], ['Weight', 'Type', 'Value']
        for i in range(3):
            in_str = in_data_command[i] + ': '
            temp_in = input(in_str)
            if temp_in == break_command:
                return
            temp += [temp_in]

    serial_number, i_weight, i_type, i_value = data_in

    data = {
        'Weight': i_weight,
        'Type': i_type,
        'Value': i_value
    }

    global db
    db[serial_number] = csv_encoder(data)
    db['timestorage_'+serial_number] = 'none'
    sync_data()

    print('-'*15, serial_number, 'Added!', '-'*15)


def add_time(serial, time_in):
    current_time = csv_time_decoder(db['timestorage_'+serial])
    current_time.append(time_in)
    db['timestorage_'+serial] = csv_time_encoder(current_time)
    sync_data()
    print('Time Added')


def csv_time_encoder(data):
    result = ''
    for i in data:
        result += i + ', '
    return result[:-2]


def csv_time_decoder(data):
    if len(str(data)) == 1:
        return []
    data = str(data)[2:-1].split(', ')
    return data


def remove_data(key):
    del db[key]
    del db['timestorage_'+key]
    sync_data()
    print(key, 'deleted')


def sync_data():
    global db
    db.close()
    db = dbm.open(join(db_path, 'mydata'), 'c')


class openinp:

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
                               command=lambda: [self.show(), inp.destroy()]).grid(row=10, column=5, columnspan=2, pady=5)
        self.btclear = Button(inp, text="Clear", fg="black", font=200, bg="red",
                              command=self.clear).grid(row=11, column=5, columnspan=2, pady=5)


def gui_command(db):
    global get_txt
    root.columnconfigure(0, weight=1)  # หน้า root
    welcome = Label(root, text="Welcome to pledge program",
                    fg="black", font=200).grid(row=2, column=0, pady=5)
    btinput = Button(root, text="Input", fg="black", font=200,
                     bg="green", command=openinp).grid(row=3, column=0, pady=5)
    get_txt = StringVar()
    box_get = Entry(root, textvariable=get_txt).grid(row=4, column=0, pady=5)
    btopen = Button(root, text="OK", fg="black", font=200,
                    bg="blue", command=viewdata).grid(row=5, column=0, pady=5)
    while True:
        with dbm.open(join(db_path, 'mydata'), 'c') as db:
            root.mainloop()


class viewdata:
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

    def __init__(self):
        serial_input = get_txt.get()
        try:
            text_out = csv_decoder(db[serial_input])
        except KeyError:
            print('Key Not Found')
            return

        text_out = csv_decoder(db[serial_input])
        all_time = csv_time_decoder(db['timestorage_'+serial_input])

        inp = Tk()
        inp.title("View Data")

        self.interestleft = Label(inp, text='Interest Rate : ', fg="black",
                                  font=200).grid(row=0, column=1, pady=5)
        self.interestright = Label(inp, text=calc_interest(text_out['Value']), fg="black",
                                   font=200).grid(row=0, column=2, pady=5)
        self.serial_number_lb = Label(
            inp, text='Serial Number : ', fg="black", font=200).grid(row=2, column=1, pady=5)
        self.weight_lb = Label(inp, text='Weight : ', fg="black", font=200).grid(
            row=4, column=1, pady=5)
        self.type_lb = Label(inp, text='Type : ', fg="black",
                             font=200).grid(row=6, column=1, pady=5)
        self.value_lb = Label(inp, text='Value : ', fg="black", font=200).grid(
            row=8, column=1, pady=5)

        self.serial_number_ent = Label(inp, text=serial_input, fg="black",
                                       font=200)
        self.serial_number_ent.grid(row=2, column=2, pady=5)
        self.weight_ent = Label(inp, text=text_out['Weight'], fg="black",
                                font=200)
        self.weight_ent.grid(row=4, column=2, pady=5)
        self.type_ent = Label(inp, text=text_out['Type'], fg="black",
                              font=200)
        self.type_ent.grid(row=6, column=2, pady=5)
        self.value_ent = Label(inp, text=text_out['Value'], fg="black",
                               font=200)
        self.value_ent.grid(row=8, column=2, pady=5)
        btopen = Button(inp, text="Delete", fg="black", font=200,
                        bg="blue", command=lambda: [remove_data(serial_input), inp.destroy()]).grid(row=9, column=2, pady=5)

        self.timetitle = Label(inp, text='Last Time:', fg="black",
                               font=200)
        self.timetitle.grid(row=10, column=1, pady=5)
        self.timedata = Label(inp, text=all_time[-1], fg="black",
                              font=200)
        self.timedata.grid(row=10, column=2, pady=5)

        self.timetitle = Label(inp, text='Add Time:', fg="black",
                               font=200)
        self.timetitle.grid(row=11, column=1, pady=5)
        self.newtime_var = StringVar()
        self.newtime_ent = Entry(inp)
        self.newtime_ent.grid(row=11, column=2, pady=5)
        bttime = Button(inp, text="Add Time", fg="black", font=200,
                        bg="blue", command=lambda: [add_time(serial_input, self.newtime_ent.get()), inp.destroy()]).grid(row=12, column=2, pady=5)


def calc_interest(value):
    value = float(value.replace(' Baht', '').replace(',', ''))
    if value >= 10000:
        interest = value * 0.03
    else:
        interest = value * 0.02
    return '{0:,.2f}'.format(round(interest, 2)) + ' ' + 'Baht'


def run_gui():
    create_database(db_path)
    global db, root

    root = Tk()  # จอเริ่ม
    root.title("Pledge program")  # ชื่อหัวข้อ
    # root.geometry("700x500+100+100") #ขนาดจอ+x+y

    temp = True
    while temp:
        with dbm.open(join(db_path, 'mydata'), 'c') as db:
            gui_command(db)
