#!/usr/bin/python3

import sys

class Main:

    def exit_error(self):
        print("Пример использования:")
        print(sys.argv[0]+" --poly=1,2,3,4,5")
        exit()

    def start(self):
        #Получаем первый агрумент
        try:
            argument=sys.argv[1]
        except:
            #Если не удалось, то выходим
            self.exit_error()
            
        #разбор параметра
        if(not argument.startswith("--poly=")):
            exit_error()
        row=argument[7:].split(',')

        #вычисление суммы ряда
        res=0;
        for i in row:
            try:
                k=int(i)
            except ValueError:
                self.exit_error()
            res=(1/k)*3
            
        print("Сумма ряда:",res)

m = Main()
m.start()
