import Tkinter
import tkFont

def func1():
    label1.config(text='iphoneXS MAX')
def func2():
    label1.config(text='pixel3 XL')
def funcX():
    if sel.get()==1:
        label1.config(text='iphoneXS MAX')
    elif sel.get()==2:
        label1.config(text='pixel3 XL')


if __name__ == '__main__':
    top = Tkinter.Tk()
    sel = Tkinter.IntVar()
    sel.set(0)
    font2 = tkFont.Font(family="Noto Sans", size=30)
    label1 = Tkinter.Label(top, text="status", font=font2, bg='#C0FFEE', padx=20, pady=20)
    button1 = Tkinter.Radiobutton(top, text='iOS', font=font2, bg='#FFEEC0', value=1, variable=sel, padx=10,command=funcX)
    button2 = Tkinter.Radiobutton(top, text='android', font=font2, bg='#FFEEC0', value=2, variable=sel, padx=10,command=funcX)
    label1.pack()
    button1.pack()
    button2.pack()
    top.mainloop()
