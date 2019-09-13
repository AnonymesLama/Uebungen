from tkinter import*
from tkinter import messagebox
from datetime import datetime
# import pytz

def button_action():
    aim_label.config(text="Nochmal!")
def ok_action():
    name = nameentry.get()
    if (name == " "):
        welcome_label.config(text="Versuche es nochmal.")
    else:
        welcome_label.config(text="Willkommen " + str(name) + " :)")
def get_help():
    m_text = f"\n\
******************\n\
Autor: Ich\n\
Datum: {t}\n\
******************"
    messagebox.showinfo(message=m_text,title = "Brauchst du Hilfe?")
fmenue = Tk() #Fenster
fmenue.title('Menü')
welcome_label = Label(fmenue,text='Willkommen! :) \n Wie heißt du?')
mleiste = Menu(fmenue) #Menü
datei_menue = Menu(mleiste,tearoff=0)
help_menue = Menu(mleiste,tearoff=0)

datei_menue.add_command(label='Hier klicken',command=button_action)
datei_menue.add_separator()
help_menue.add_command(label='?',command=get_help)
help_menue.add_command(label='Exit',command=fmenue.quit)

mleiste.add_cascade(label='Datei', menu=datei_menue)
mleiste.add_cascade(label='Help', menu=help_menue)

t = datetime.now 
# 'messagebox.showinfo(message="Infotext", title = "Box-Titel")'
nameentry = Entry(fmenue,bd=5,width=40)
aim_label = Label(fmenue,text="Klicke auf den Knopf für eine Überraschung!")
aim_button = Button(fmenue,text='Klick hier.',command=button_action)
exit_label = Label(fmenue,text='Wenn du aufgeben willst, klicke auf den Schließen-Knopf.')
exit_button = Button(fmenue,text='Schließen', command=fmenue.quit)
ok_button = Button(fmenue,text='Ok.', command=ok_action)

#Grids
welcome_label.grid(row=0, column=1)
nameentry.grid(row=0, column=2)
ok_button.grid(row=0,column=3)
aim_label.grid(row=2, column=2, padx=20)
aim_button.grid(row=2, column=3,)
exit_label.grid(row=3, column=2, padx=20)
exit_button.grid(row=3, column=3)

fmenue.config(menu=mleiste)
fmenue.mainloop()