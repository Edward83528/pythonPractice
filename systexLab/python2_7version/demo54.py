import Tkinter
import tkFont
top=Tkinter.Tk()
for font in tkFont.families():
    print font

font1 = tkFont.Font(family='Broadway', size=30)
font2 = tkFont.Font(family="Noto Sans", size=30)
label1 = Tkinter.Label(top, text='Hello Tk', fg='#000000', bg='#C0FFEE', padx=20, pady=20, font=font1)
label2 = Tkinter.Label(top, text="www.uuu.com.tw", fg='#FFFFFF', bg='#440000', padx=10, pady=30, font=font2)
label2.pack()
label1.pack()

top.mainloop()

