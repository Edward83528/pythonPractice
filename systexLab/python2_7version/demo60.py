import Tkinter
import tkFont

def display(ev):
    label1.config(text=entry1.get())

if __name__ == '__main__':
    top = Tkinter.Tk()

    font2 = tkFont.Font(family="Noto Sans", size=30)
    label1 = Tkinter.Label(top, text="input something", font=font2)
    button1 = Tkinter.Button(top, text="button1", font=font2)
    entry1 = Tkinter.Entry(top, text="", font=font2)
    label1.pack()
    entry1.pack()
    button1.pack()
    entry1.bind('<Return>',display)
    button1.bind('<Button-1>', display)
    top.mainloop()
