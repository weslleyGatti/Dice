from tkinter import *
import classes as cl
import random
main = cl.App()

def getNumber(d):
    if d == '\u2680':
        return 1
    elif d == '\u2681':
        return 2
    elif d == '\u2682':
        return 3
    elif d == '\u2683':
        return 4
    elif d == '\u2684':
        return 5
    elif d == '\u2685':
        return 6

def Roll():
    d1 = random.choice(mdice)
    d2 = random.choice(mdice)

    nd1 = getNumber(d1)
    nd2 = getNumber(d2)

    lbld1.config(text = d1)
    lbld2.config(text = d2)
    lbl1.config(text = nd1)
    lbl2.config(text = nd2)

    lbl3.config(text = f'Total: {nd1 + nd2}')

mdice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']

mF = Frame(main)
mF.pack(pady=20)

lbld1 = Label(mF, text=mdice[0], font = ('Helvetica', 50), fg = 'black')
lbld1.grid(row = 0, column = 0, padx = 5)

lbl1 = Label(mF, text='1')
lbl1.grid(row=1, column=0)

lbld2 = Label(mF, text=mdice[0], font = ('Helvetica', 50), fg = 'black')
lbld2.grid(row = 0, column = 1, padx = 5)

lbl2 = Label(mF, text='1')
lbl2.grid(row=1, column=1)

btn1 = Button(main, text='Roll Dice', command = Roll, font=('Helvetica', 24))
btn1.pack(pady=20)

lbl3 = Label(main, text = 'Valor Total', font = ('Helvetica', 24), fg = 'grey')
lbl3.pack(pady=40)

#LOOP#
if __name__ == '__main__':
    main.mainloop()