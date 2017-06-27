#!/usr/bin/python3

from tkinter import *
from tkinter.tix import *

#Класс записи
class Record:
    mail = ""
    def __init__(self,mail):
        self.spam = list()
        self.average_spam = 0
        self.mail = mail
        self.mail_count = 0

#Открытие исходного файла
file = open('mbox.txt')
log = file.read()

#разбор исходного файла
index = 0
mail_list = {}
average_spam=0
mail_count = 0
while index<len(log):
    index = log.find("From: ",index)
    eindex = log.find("\n",index+6)

    if index < 0:
        break

    email = log[index+6:eindex]

    spamindex = log.find("X-DSPAM-Confidence: ", index)
    espamindex = log.find("\n",spamindex+20)
    spam = log[spamindex+20:espamindex]
    
    if spamindex>0:
        index=spamindex
    
    #Заполнение словаря полученными значениями
    rec=mail_list.setdefault(email,Record(email))
    rec.spam.append(spam)
    rec.average_spam += float(spam)
    rec.mail_count += 1
    average_spam+=float(spam)
    mail_count+=1

#Сбор статистических данных
average_spam=average_spam/mail_count
print("Среднее значение спама:",average_spam)
max_mail_sent_count=0
lmmsc = 0;
max_mail_sent_email=""
max_average_spammer=email
for mail in mail_list:
    o = mail_list[mail]
    o.average_spam = o.average_spam / len(o.spam)
    max_mail_sent_count = max(o.mail_count,max_mail_sent_count)
    if lmmsc != max_mail_sent_count:
        max_mail_sent_email=mail
        lmmsc = max_mail_sent_count
    #print(mail,o.average_spam, o.mail_count)
    if o.average_spam > mail_list[max_average_spammer].average_spam:
        max_average_spammer=mail

print("Больше всех отправил писем: ",max_mail_sent_email," | ",max_mail_sent_count)
print("Максимальное среднее значение спама: "+max_average_spammer+" |",mail_list[max_average_spammer].average_spam)

#Рисуем гистограму
master = Tk()
frame = Frame(width="500",height="500")
frame.pack()
swin = ScrolledWindow(frame, width=500, height=550)
swin.pack()
w = Canvas(swin.window, width=500, height=(len(mail_list)*35))
w.pack()

i=0
for email in mail_list:
    mcount = mail_list[email].mail_count
    bsize = int( 460 * mcount / max_mail_sent_count )
    w.create_text(20,i*35+10,text=email+" | "+str(mcount)+" | "+str(mail_list[email].average_spam),anchor="nw")
    w.create_rectangle(20,i*35+25,bsize+20,i*35+35,fill="blue")
    i+=1    

mainloop()
