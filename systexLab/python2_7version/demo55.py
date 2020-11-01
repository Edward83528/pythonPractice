import Tkinter
import tkFont
counter = 0
def callback1():
    global counter
    label1.config(text='button clicked %d times' % counter)
    counter += 1
    # print 'button clicked!'#
def callback2():
    label2.config(text="button clicked %d times" % counter2.get())
    counter2.set(counter2.get() + 1)
    print 'button2 clicked!'
l1 = [0]
def callback3():
    l1[0]+=1
    label3.config(text='button clicked %d times'%l1[0])
    print 'button3 clicked!'

if __name__ == '__main__':
    top = Tkinter.Tk()
    counter2 = Tkinter.IntVar()
    font2 = tkFont.Font(family="Noto Sans", size=30)
    label1 = Tkinter.Label(top, text='status', font=font2, bg='#C0FFEE', padx=20, pady=20)
    label2 = Tkinter.Label(top, text='status2', font=font2, fg='#000066', bg='#C0FFEE', padx=20, pady=20)
    label3 = Tkinter.Label(top, text='status3', font=font2, fg='#006600', bg='#FFC0EE', padx=20, pady=20)
    button = Tkinter.Button(top, text='click me!', font=font2, command=callback1)
    button2 = Tkinter.Button(top, text='click me2!', font=font2, command=callback2, fg='#000066')
    button3 = Tkinter.Button(top, text='click me3!', font=font2, command=callback3, fg='#006600')
    button.pack()
    label1.pack()
    button2.pack()
    label2.pack()
    button3.pack()
    label3.pack()
    top.mainloop()
