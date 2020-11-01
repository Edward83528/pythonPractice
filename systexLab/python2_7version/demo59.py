import Tkinter
import tkFont


def func1(ev):
    label1.config(text=message % int(ev))


message = 'current value=%d'
if __name__ == '__main__':
    top = Tkinter.Tk()

    font2 = tkFont.Font(family="Noto Sans", size=30)
    label1 = Tkinter.Label(top, text=message % 0, font=font2)
    scale1 = Tkinter.Scale(top, label='vol', orient='h', from_=0, to=100, font=font2, command=func1)
    label1.pack()
    scale1.pack()
    top.minsize(350, 200)
    top.maxsize(350, 200)
    top.mainloop()
