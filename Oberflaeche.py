from tkinter import*

def forward_action():
    x = 0
    f2 = Tk()
    f2.title('Seite 2')
    new_label = Label(f2,text='Seite 2')
    new_label.grid(row=0,column=0,pady=30)
    back_button = Button(f2,text='Back',command=back_action())
    back_button.grid(row=1,column=0)
    if(x==1):
        f2.quit
    f2.mainloop()

def back_action():
    x = 1

fo = Tk() #Fenster
fo.title('Menü')

forward_button = Button(fo,text='Forward',command=forward_action)
quit_button = Button(fo,text='Quit', command=fo.quit)
main_label = Label(fo,text='Das hier ist die erste Seite.')

forward_button.grid(row=1,column=1)
quit_button.grid(row=1,column=0, pady=20)
main_label.grid(row=0,column=0, padx=40)

fo.mainloop()