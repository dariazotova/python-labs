#!/usr/bin/python3

from tkinter import *

class Main:

    def start(self):
        values=list()

        width=int(input("Введите ширину окна:"))
        height=int(input("Введите высоту окна:"))

        print("Введите значения по одному, ничего не вводите чтобы прекратить ввод")

        #Ввод значений
        i=1
        while True:
            val = input("Значение №"+str(i)+":")
            i+=1
            if val == '':
                break
            values.append(float(val))

        minval = min(values)
        maxval = max(values)
        dif = maxval - minval

        #Вычисление скользящей средней
        avr = list()
        i=0
        for v in values:
            if i==0:
                i+=1
                continue
            if i+1 > len(values)-1:
                break
            val = (values[i-1] + values[i] + values[i+1]) / 3
            avr.append(val)
            i+=1

        #Создание окна
        master = Tk()
        w = Canvas(master, width=width, height=height)
        w.pack()

        w.create_line(20,0,20,height-20)
        w.create_line(20,height-20,width,height-20)
        w.create_text(15,height-20,text=minval)
        w.create_text(15,20,text=maxval)
        w.create_text(15,height/2,text=((maxval+minval)/2))

        i=0
        iteration_size = (width-40)/(len(values)-1)
        lasth=0
        if minval<0:
            sy=((height-40)*abs(minval))/dif
        else:
            sy=0

        #рисование графика
        for v in values:
            
            w.create_text(20+i*iteration_size,height-10,text=(i+1))
            h=((height-40)*v)/dif
            if i==0:
                lasth=h
            w.create_line(20+i*iteration_size,height-h-20-sy,20+(i-1)*iteration_size,height-lasth-20-sy)
            i+=1
            lasth=h
        #рисование средней скользящей
        iteration_size = (width-40)/(len(avr)-1)
        i=0
        for v in avr:
            h=((height-40)*v)/dif
            if i==0:
                lasth=h
            w.create_line(20+i*iteration_size,height-h-20-sy,20+(i-1)*iteration_size,height-lasth-20-sy,fill="blue")
            i+=1
            lasth=h
        mainloop()

m = Main()
m.start()
