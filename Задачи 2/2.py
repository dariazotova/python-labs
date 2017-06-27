
class Main:

    def start(self):
        a=input("Введите число, к которому нужно найти квадратный корень:")
        try:
            a=float(a)
        except ValueError:
            print("Вы ввели не число!")
            exit()

        res=0
        nres=1
        i=0

        while(nres!=res):
            res=nres
            nres=(1/2)*(res+(a/res))
            print(i,": ",nres)
            i+=1
            
        print((res*res))
        print("\nКвадратный корень от", a,"=", res)


m = Main()
m.start()
