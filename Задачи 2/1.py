
class Main:

    #переменная значения калькулятора
    value=0

    #функция вывода состояния на экран
    def print_state(self):
        global value
        print("\nРезультат: ",self.value,'\n')
        
    #функция ввода операндов с клавиатуры
    def input_operand(self):
        t=input("Введите операнд:")
        
        try:
            t=float(t)
        except ValueError:
            print("Ошибка! Операнд не число!")
            t=None
        return t
        
    def start(self):
        print("Калькулятор")

        #флаг выхода из программы
        exit=False
        while(not exit):
            self.print_state()
            print("'q'-выход, 'i'-ввод операнда, 'r'-сброс")
            print("'+'-сложение, '-'-вычитание, '*'-умножение, '/'-деление\n")
            action=input("Выберете действие:")
            
            if(action=='q'):
                exit=True
                continue
                
            if(action=='r'):
                self.value=0
                continue
            
            if(action=='i'):
                t=self.input_operand()
                if(t!=None):
                    self.value=t
                continue
                
            if(action=='+'):
                t=self.input_operand()
                if(t!=None):
                    self.value+=t
                continue
                
            if(action=='-'):
                t=self.input_operand()
                if(t!=None):
                    self.value-=t
                continue
            
            if(action=='*'):
                t=self.input_operand()
                if(t!=None):
                    self.value*=t
                continue
           
            if(action=="/"):
                t=self.input_operand()
                if(t!=None):
                    self.value/=t
                continue
            
            print("Неизвестное действие!")

Main.start(Main())
