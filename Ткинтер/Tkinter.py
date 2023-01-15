from tkinter import *
win = Tk()
win.title("База данных")
win.geometry("640x600")
Label(win,text="Стоимость бала").grid(row=0, column=0, sticky=E)
Label(win,text="Повышающий коэффициент").grid(row=1, column=0, sticky=E)
Label(win,text="Граница  ").grid(row=2, column=0, sticky=E)
s2 = Entry(win, width=15, font="Arial 18")
s2.grid(row=0, column=1)
s1 = Entry(win, width=15,font="Arial 18")
s1.grid(row=1, column=1)
gra = Entry(win, width=15,font="Arial 18")
gra.grid(row=2, column=1)
def werr():
    f = open("list.text", "r")
    gran=float(gra.get())
    s=float(s2.get())
    k=float(s1.get())/100+1
    def rasch(zapis,gran,s,k):
            x = float(zapis.split()[-1])
            if x > gran:
                return x * s * k + float(zapis.split()[-2])
            else:
                return 0
    f.readline()
    file = open("list1.text", "w")
    import datetime
    d = str(datetime.date.today()).split("-")

    file.write('''ООО "Название фирмы" 
    Ведомость начисления заработной платы с учетом премиальных выплат.
    №_____ от «'''+d[2]+"» _____"+d[1]+"_____"+d[0]+''''г.
    № Фамилия Имя Отчество    Оклад    Размер премии    Итоговая зарплата \n''')

    nomer = 1
    sum = 0

    for i in f.readlines():
        raz = rasch(i,gran,s,k)
        if raz != 0:
            file.write(str(nomer)+"."+" ".join(i.split()[1:-2])+"\t\t"+i.split()[-2]+"\t\t"+str(raz)+"\t\t"+str(
            float(i.split()[-2]) + raz) + "\n")
        nomer += 1
        sum += raz
    file.write("\t\t\t\t\t\tИтог : "+str(sum ) +"p.")
    file.close()


but = Button(win, text = "Отправить", width=20, font="Arial 18",command=werr)
but.grid(row=3, columnspan=2)

win.mainloop()