
from tkinter.ttk import Frame, Button, Label, Entry
from tkinter import DISABLED, Tk,X, LEFT
from ast import Delete
import serial
import time
import datetime
import os.path


strcommand = []
id_node = []
part_id = []

COM_name = ""
baud_name = 0
numbers_node = 0
path = ""


i_page = 0
check_run = False
root = Tk()
root.title("DLCORP")
root.geometry("300x300+300+300")
# quitButton = Button(root, text="Quit", command = click_ok)
# quitButton.place(x=120, y=80)
root_COM = Frame(root)
root_NUM = Frame(root)
root_ID = Frame(root)
root_PATH = Frame(root)
root_RUN = Frame(root)

n = 0
count_send = 0

def main_serial():
    root_COM.pack(fill=X)

    frame_serial = Frame(root_COM)
    frame_serial.pack(fill=X)
    lb_serial = Label(frame_serial, text="SERIAL", width=10)
    lb_serial.pack(side=LEFT, padx=5, pady=5)
    entry_serial = Entry(frame_serial)
    entry_serial.pack(fill=X, padx=5, expand=True)

    frame_baud = Frame(root_COM)
    frame_baud.pack(fill=X)
    lb_baud = Label(frame_baud, text="Baudrate", width=10)
    lb_baud.pack(side=LEFT, padx=5, pady=5)
    entry_baud = Entry(frame_baud)
    entry_baud.pack(fill=X, padx=5, expand=True)

    frame_bt_com = Frame(root_COM)
    frame_bt_com.pack(fill=X)
    bt= Button(frame_bt_com, text="OK", command = lambda: click_COM(entry_serial.get(), entry_baud.get()))
    bt.pack(padx = 5, pady = 5)

    def click_COM(data1, data2):
        global COM_name
        global baud_name
        print("data1" + str(data1))
        print("data2" + str(data2))
        COM_name = data1
        baud_name = data2
        root_COM.destroy()
        main_number_node()

def main_number_node():
    root_NUM.pack(fill=X)
    frame_number_node = Frame(root_NUM)
    frame_number_node.pack(fill=X)
    lbl = Label(frame_number_node, text="Number of node", width=15)
    lbl.pack(side=LEFT, padx=10, pady=5)
    entry = Entry(frame_number_node)
    entry.pack(fill=X, padx=10, expand=True)

    frame_bt_number_node = Frame(root_NUM)
    frame_bt_number_node.pack(fill=X)
    bt = Button(frame_bt_number_node, text="OK", command = lambda: click_NUM(entry.get()))
    bt.pack(padx = 5, pady = 5)

    def click_NUM(x):
        print("so node : " + str(x))
        global numbers_node
        numbers_node = int(x)
        root_NUM.destroy()
        main_id_node(x)
        # main_serial()


def main_id_node(id): 
    global n
    root_ID.pack(fill=X)
    for widget in root_ID.winfo_children():
        widget.destroy()

    frame_number_node = Frame(root_ID)
    frame_number_node.pack(fill=X)
    lbl = Label(frame_number_node, text="ID node " + str(n+1), width=10)
    lbl.pack(side=LEFT, padx=10, pady=5)
    entry = Entry(frame_number_node)
    entry.pack(fill=X, padx=10, expand=True)

    frame_bt_id_node = Frame(root_ID)
    frame_bt_id_node.pack(fill=X)
    # bt_next = Button(frame_bt_number_node, text="NEXT", command = lambda: click_next(entry.get()))
    # bt_next.pack(padx = 5, pady = 5)

    if n >= (int(id) - 1):
        bt_next = Button(frame_bt_id_node, text="NEXT", state= DISABLED)
        bt = Button(frame_bt_id_node, text="OK", command = lambda: click_ID(entry.get()))
        bt.pack(padx = 5, pady = 5)
    else:
        bt_next = Button(frame_bt_id_node, text="NEXT", command = lambda: click_next(entry.get()))
        bt_next.pack(padx = 5, pady = 5)
        bt = Button(frame_bt_id_node, text="OK", state= DISABLED)

    def click_next(id):
        global n  
        n = n+1
        print("n:" + str(n))
        print("id:" + str(id))
        id_node.append(id)
        main_id_node(numbers_node)
    
    def click_ID(id):
        id_node.append(id)
        print("id:" + str(id))
        root_ID.destroy()
        main_path()
  

def main_path():
    root_PATH.pack(fill=X)
    frame_path = Frame(root_PATH)
    frame_path.pack(fill=X)
    lbl = Label(frame_path, text="Save path", width=15)
    lbl.pack(side=LEFT, padx=10, pady=5)
    entry = Entry(frame_path)
    entry.pack(fill=X, padx=10, expand=True)

    frame_bt_path = Frame(root_PATH)
    frame_bt_path.pack(fill=X)
    bt = Button(frame_bt_path, text="OK", command = lambda: click_path(entry.get()))
    bt.pack(padx = 5, pady = 5)

    def click_path(_path):
        global part_id
        root_PATH.destroy()
        for c in id_node:
            part_id.append(_path +"\\Id"+ c +".csv")
            print("path" + str(c) +":" + _path +"\\Id"+ c +".csv")
        main_run()



def main_run():
    root_RUN.pack(fill=X)
    frame_bt_run = Frame(root_RUN)
    frame_bt_run.pack(fill=X)
    bt_run = Button(frame_bt_run, text="Run", command = lambda: run())
    bt_run.pack(padx = 5, pady = 5)

    # frame_bt_exit = Frame(root_RUN)
    # frame_bt_exit.pack(fill=X)
    # bt_exit = Button(frame_bt_exit, text="Exit", command = quit)
    # bt_exit.pack(padx = 5, pady = 5)

    def run():
        root_RUN.pack(fill=X)
        frame_lb = Frame(root_RUN)
        frame_lb.pack(fill=X)
        lbl = Label(frame_lb, text="Running" )
        lbl.pack(side="top", padx=10, pady=5)
        run_main()

def run_main():

    global count_send
    arduino  = serial.Serial(COM_name, baud_name, timeout = 1)
    def read_serial():
        time.sleep(1)
        data = arduino.readline()
        encoding = "utf-8"
        data =  data.decode(encoding).strip()
        data_send = data
        if len(data) == 0:
            return
        cmd =""
        for c in data:
            if c == "*":
                break
            if c == "!":
                continue
            cmd +=c
        strcommand = cmd.split(",")
        data_save = read_time()

        print(data_send) # printing the value
        save = False
        for c in strcommand:
            print (c)
            if save:
                data_save += ","
                data_save += c
            if c == "Temp" or c == "Humi" or c == "Pm25" or c == "Pm10":
                save = True
            else:   save = False
        data_save = "\n" + data_save
        print(data_save) # printing the value
        for c in id_node:
            if c == strcommand[0]:
                path = read_path(c)
                file = open(path,mode  = "a", encoding="utf-8-sig")
                file.write(data_save)
                file.close()
        
        Delete(data)
        Delete(data_save)
        strcommand.clear()

    def send_read_value(x):

        cmd_send = "#" + id_node[int(x)] + "D*"
        write_serial(cmd_send)
        print(cmd_send)

        return
    def write_serial(x):
        arduino.write(bytes(x, 'utf-8')) 
        return
    def read_time():
        x = datetime.datetime.now()
        time_now = x.strftime("%x") + "," +  x.strftime("%X") 
        return time_now
    def read_path(x):
        n = id_node.index(x)
        path_value = part_id[n]
        return path_value
    
    for c in id_node:
        path = read_path(c)
        if os.path.isfile(path):
            print ("File exist")
        else:
            print ("File not exist")
            file = open(path,mode  = "a", encoding="utf-8-sig")
            file.write("Date,Time,Temperature,Humidity,Pm25,Pm10")
            file.close()
        
    
    while True:
    # num = input("Enter a number: ") # Taking input from user
        
        send_read_value(count_send)
        read_serial()
        time.sleep(4)
        count_send +=1
        if count_send >= int(numbers_node):
            count_send = 0
        
        


main_serial()
root.mainloop()



# frame1 = Frame(root)
# frame1.pack(fill=X)
# lbl1 = Label(frame1, text="Title", width=6)
# entry1 = Entry(frame1)
# entry1.pack(fill=X, padx=5, expand=True)





