import tkinter as ktt
import random
s = ktt.Tk()
secrast = random.randint(1,10)
def RandomNumber():
    global secrast
    num = int(entry.get())
    if num < secrast:
        lable["text"] = "замало більше"
    elif num > secrast:
        lable["text"] = "забагато менше"
    else:
        lable["text"] = " ви перемогли , нове число"
        secrast = random.randint(1,10)
        return secrast
entry = ktt.Entry(s)
lable = ktt.Label(s,text="1 до 10",font=("Arial",18))
button = ktt.Button(s,text="перевірити",font=("Arial",18),command=RandomNumber)
lable.pack()
entry.pack()
button.pack()
s.mainloop()
