import tkinter as ktt
import random
import time as ti
s = ktt.Tk()
secrast = random.randint(1,10)
def hjrdbjhxgtjhvsdfgtjtgfjdmhjsktjukimgurdktuysksri():
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
button = ktt.Button(s,text="перевірити",font=("Arial",18),command=hjrdbjhxgtjhvsdfgtjtgfjdmhjsktjukimgurdktuysksri)
lable.pack()
entry.pack()
button.pack()
s.mainloop()