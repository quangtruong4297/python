from socket import timeout
from tkinter import filedialog
from tkinter.ttk import Frame, Button, Label, Entry
from tkinter import DISABLED, Tk,X, LEFT, ttk
from ast import Delete
from xml.dom.expatbuilder import parseFragmentString
import serial
import time
import datetime
import os.path
import threading
import sys
import json
import pathlib

# strcommand = []
# id_node = []
# part_id = []

# Station_tinh = ""
# Station_name = ""
# Station_name = ""
# Station_name = ""

# baud_name = 0
# numbers_node = 0
# path = ""
# path_br = ""
root = Tk()
root.title("DLCORP")
root.geometry("300x300+300+300")
check_run = False
frequency = 5

root_Station = Frame(root)
root_Station_CT = Frame(root)
root_Statio_Tram = Frame(root)
root_NUM = Frame(root)
root_sensor = Frame(root)

root_FR = Frame(root)
root_PATH = Frame(root)
root_RUN = Frame(root)

list_ma_tinh = ["HN", "DN"]
list_ma_cong_trinhHN = ["QUANGMINH"]
list_ma_cont_trinhDN = ["NHONTRACH1", "NHONTRACH5"]
list_ma_tramQM = ["G1", "G2", "G3", "G4", "G5", "GII-6","G7-TT","G11-TT","GII-12","GII-13","GII-14","GII-15","GII-16","GII-17","QT-G7","QT-G11","QT-G16"]
list_ma_tramNT1 = ["H1", "H2A", "H3A", "H4A","DK", "45-1", "45-2","45-3A", "LK1A","LK2A", "LK3", "LK4","LK5A","B2","B3","B4A","C1","C2","C3","C4","C5","C6","C7","C8","QT1","QT2","QT3"]
list_ma_tramNT5 = ["KT1","KT2","KT3","KT4","KT5","KT-6","KT7","KT8","KT9","KT10","KT11","KT12","KT13","KT14","KT15","KT16","KT17","KT18","QS1","QS2","QS3","QS4"]

def main_Station_tinh():
    root_Station.pack(fill=X)
    frame_ma_tinh = Frame(root_Station)
    frame_ma_tinh.pack(fill=X)
    lb_ma_tinh = Label(frame_ma_tinh, text="Ma Tinh", width=10)
    lb_ma_tinh.pack(side=LEFT, padx=5, pady=5)
    spinner_tinh = ttk.Combobox(frame_ma_tinh, width = 27)
    spinner_tinh['values'] = list_ma_tinh
    spinner_tinh.pack(fill=X, padx=5, expand=True)

    frame_bt = Frame(root_Station)
    frame_bt.pack(fill=X)
    bt= Button(frame_bt, text="OK", command = lambda: click_Station(spinner_tinh.get()))
    bt.pack(padx = 5, pady = 5)
    def click_Station(data1):
        root_Station.destroy()
        time.sleep(0.2)
        main_Station_CT(data1)

def main_Station_CT(data):
    root_Station_CT.pack(fill=X)
    frame_ma_CT = Frame(root_Station_CT)
    frame_ma_CT.pack(fill=X)
    lb_ma_CT = Label(frame_ma_CT, text="Ma Cong Trinh", width=10)
    lb_ma_CT.pack(side=LEFT, padx=5, pady=5)
    spinner_CT = ttk.Combobox(frame_ma_CT, width = 27)
    if data == "HN":
        spinner_CT['values'] = list_ma_cong_trinhHN
        spinner_CT.pack(fill=X, padx=5, expand=True)
    elif data == "DN":
        spinner_CT['values'] = list_ma_cont_trinhDN
        spinner_CT.pack(fill=X, padx=5, expand=True)
    frame_bt_CT = Frame(root_Station_CT)
    frame_bt_CT.pack(fill=X)
    bt_OK= Button(frame_bt_CT, text="OK", command = lambda: click_OK(spinner_CT.get()))
    bt_OK.pack(padx = 5, pady = 5)
    def click_OK(data1):
        root_Station_CT.destroy()
        time.sleep(0.2)
        main_Station_Tram(data1)

def main_Station_Tram(data):
    root_Statio_Tram.pack(fill=X)
    frame_ma_Tram = Frame(root_Statio_Tram)
    frame_ma_Tram.pack(fill=X)
    lb_ma_Tram = Label(frame_ma_Tram, text= "Ma Tram", width=10 )
    lb_ma_Tram.pack(side=LEFT, padx=5, pady=5)
    spinner_Tram = ttk.Combobox(frame_ma_Tram, width = 27)
    if data == "QUANGMINH":
        spinner_Tram['values'] = list_ma_tramQM
        spinner_Tram.pack(fill=X, padx=5, expand=True)
    elif data == "NHONTRACH1":
        spinner_Tram['values'] = list_ma_tramNT1
        spinner_Tram.pack(fill=X, padx=5, expand=True)
    elif data == "NHONTRACH5":
        spinner_Tram['values'] = list_ma_tramNT5
        spinner_Tram.pack(fill=X, padx=5, expand=True)

    frame_bt_CT = Frame(root_Station_CT)
    frame_bt_CT.pack(fill=X)
    bt_OK= Button(frame_bt_CT, text="OK", command = lambda: click_OK(spinner_Tram.get()))
    bt_OK.pack(padx = 5, pady = 5)
    def click_OK(data1):
        root_Station_CT.destroy()
        time.sleep(0.2)
        main_Station_Tram(data1)

def main_number_sensor():
    root_NUM.pack(fill = X)
    frame_number = Frame(root_NUM)
    frame_number.pack(fill=X)
    lb_number = Label(frame_number, text="So sensor", width=10)
    lb_number.pack(side=LEFT, padx = 5, pady = 5)
    entry = Entry(frame_number)
    entry.pack(fill=X, padx=10, expand=True)

    frame_bt_number = Frame(root_ID)
    frame_bt_number.pack(fill=X)
    bt_OK= Button(frame_bt_number, text="OK", command = lambda: click_OK(entry.get()))
    bt_OK.pack(padx = 5, pady = 5)
    def click_OK(data1):
        root_NUM.destroy()
        time.sleep(0.2)
        main_Station_Tram(data1)

def main_sensor_info(data):
    root_sensor.pack(fill = X)
    frame_semsor = Frame(root_sensor)
    frame_semsor.pack(fill=X)
    lb_number = Label(frame_semsor, text="So sensor", width=10)
    lb_number.pack(side=LEFT, padx = 5, pady = 5)
    entry = Entry(frame_semsor)
    entry.pack(fill=X, padx=10, expand=True)


main_Station_tinh()
root.mainloop()