#_____________________________________________

#Created By Houman Hafez, Digital Clock 1.0

#_____________________________________________
#Imports (Tkinter for the GUI, Time for the Digital Clock and PIL for the Favicon)
from tkinter import *
import tkinter as tk
import time
import os


#Creates a Frame with a title, geometry and makes it resizable
app_window = Tk() 
app_window.title("Digital Clock") 
app_window.geometry("420x150") 
app_window.resizable(False, False)

#Makes a universal path for the favicon and then applies it to the application
script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, 'icon\icon.ico')
app_window.iconbitmap(icon_path)


#Font, Size and Boldiness is defined here
text_font= ("Boulder", 68, 'bold')
#Changes the background to a red color
background = "#f6546a"
#Changes the Text Color to a Light Blue and gives the border a width
foreground= "#cccccc"
border_width = 25

#The whole package above gets added to a Label and then gets a grid layout
label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)
label.pack()

#A function for the Time in Hours, Minutes and Seconds
def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, digital_clock)
   

#The Function gets called here with the GUI Window
digital_clock()
app_window.mainloop()

    
