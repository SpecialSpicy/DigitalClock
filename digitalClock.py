#Imports (Tkinter fuer GUI und Time fuer die Zeit)
from tkinter import *
import time

#Erstellen einer Window mit ein Titel, Size und Resizability
app_window = Tk() 
app_window.title("Digital Clock") 
app_window.geometry("420x150") 
app_window.resizable(1,1)

#Schrift, Hintergrundfarbe, Textfarbe und die Grenzenbreite
text_font= ("Boulder", 68, 'bold')
#Eine Populaere Farbe beim Color Hex (Weinrot)
background = "#420420"
#Eine Populaere Farbe beim Color Hex (Sehr helles Blau)
foreground= "#c0d6e4"
border_width = 25

#Das ganze fuegt man in einer Label und es bekommt ein gridlayout
label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

#Eine Funktion fuer die Digital Uhr mit ein label und Zeit in Stunden, Minuten und Sekunden
def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, digital_clock)

#Hier wird der Funktion gerufen und die GUI looped(muss immer sein sonst funktioniert der GUI in Tkinter nicht)
digital_clock()
app_window.mainloop()
