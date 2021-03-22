import pandas as pd
import tkinter as tk
from tkinter import *
import tkinter.font as tf
import time
import random
import xlrd
import csv
from tkinter.filedialog import *

def window_init():
    w=tk.Tk()
    w.title("抓阄")
    w.geometry("250x120")
    return w
def random_start(w,mate,text):
    for i in mate:
        text.set(i)
        name=Label(w, font=ft, textvariable=text)
        #name.pack() pack一次就加上去一次
        w.update()#tk刷新
        time.sleep(0.04)
    l=len(mate)
    i=random.randint(0,l-1)
    text.set(mate[i])

def read_mate():
    return pd.read_csv('mate.csv')

def init_csv():
    epath = askopenfilename(title="选择excel")#放到第二列
    data = xlrd.open_workbook(epath)
    table = data.sheet_by_name('Sheet1')
    coln = table.col_values(0)
    print(coln) 
    print(coln[1:])
    f = open('mate.csv', 'w', encoding='utf-8')
    csv_writer = csv.writer(f)
    csv_writer.writerow(['name'])
    for i in coln[0:]:
        i = [i]
        csv_writer.writerow(i)  # writerow 支持的是列表！！！
    f.close()
if __name__=='__main__':
    w=window_init()
    init_csv()
    mate=read_mate()
    print(mate)
    mate=mate['name']
    ft = tf.Font(family='微软雅黑', size=40, weight=tf.BOLD)  # 设置字体
    text = StringVar()
    text.set(mate[0])
    name = Label(w,font=ft,textvariable=text)
    name.pack()
    start =Button(w, text="开始", width=7, command=lambda:random_start(w,mate,text))
    start.pack()
    w.mainloop()
