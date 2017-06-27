
#переменная значения калькулятора
value=0

#функция вывода состояния на экран
def print_state():
    global value
    print("\nРезультат: ",value,'\n')
    
#функция ввода операндов с клавиатуры
def input_operand():
    t=input("Введите операнд:")
    
    try:
        t=float(t)
    except ValueError:
        print("Ошибка! Операнд не число!")
        t=None
    return t
    

print("Калькулятор")

#флаг выхода из программы
exit=False
while(not exit):
    print_state()
    print("'q'-выход, 'i'-ввод операнда, 'r'-сброс")
    print("'+'-сложение, '-'-вычитание, '*'-умножение, '/'-деление\n")
    action=input("Выберете действие:")
    
    if(action=='q'):
        exit=True
        continue
        
    if(action=='r'):
        value=0
        continue
    
    if(action=='i'):
        t=input_operand()
        if(t!=None):
            value=t
        continue
        
    if(action=='+'):
        t=input_operand()
        if(t!=None):
            value+=t
        continue
        
    if(action=='-'):
        t=input_operand()
        if(t!=None):
            value-=t
        continue
    
    if(action=='*'):
        t=input_operand()
        if(t!=None):
            value*=t
        continue
   
    if(action=="/"):
        t=input_operand()
        if(t!=None):
            value/=t
        continue
    
    print("Неизвестное действие!")


