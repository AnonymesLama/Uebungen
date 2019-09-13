from tkinter import*

def forward_action():
    f2.mainloop()

fo = Tk() #Fenster
fo.title('Menü')
forward_button = Button(fo,text='Forward',command=forward_action)
quit_button = Button(fo,text='Quit', command=fo.quit)
main_label = Label(fo,text='Das hier ist die erste Seite.')
new_label = Label(f2,text='Seite 2')
new_label.grid(row=0,column=0,pady=30)
forward_button.grid(row=1,column=0)
quit_button.grid(row=1,column=1, pady=20)
main_label.grid(row=0,column=0, padx=40)
f2 = Tk()
f2.title('Seite 2')

fo.mainloop()