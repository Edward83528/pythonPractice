import Tkinter
import tkFont
def func1(ev):
    label1.config(text='enter')
def func2(ev):
    label1.config(text='leave')
def func3(ev):
    label1.config(text='left single')
def func4(ev):
    label1.config(text="middle double")
def func5(ev):
    label1.config(text='right move')
if __name__ == '__main__':

    top=Tkinter.Tk()

    font2 = tkFont.Font(family="Noto Sans", size=30)
    label1 = Tkinter.Label(top, text="label1", font=font2, padx=10, pady=10, bg='#FFEEC0')
    button1 = Tkinter.Button(top, text="button1", padx=20, pady=20, bg='#C0FFEE', font=font2)
    label1.pack()
    button1.pack()
    button1.bind('<Enter>', func1)
    button1.bind('<Leave>', func2)
    button1.bind('<Button-1>', func3)
    button1.bind('<Double-2>', func4)
    button1.bind('<B3-Motion>', func5)
    top.mainloop()
