import Tkinter
import tkFont


def motion(ev):
    message.config(text='move to [%d,%d]'%(ev.x, ev.y))


if __name__ == '__main__':
    top = Tkinter.Tk()
    font2 = tkFont.Font(family="Noto Sans", size=30)
    message = Tkinter.Message(top, text='status', font=font2, bg='#C0FFEE')
    message.pack()
    message.bind('<Motion>', motion)
    top.mainloop()
