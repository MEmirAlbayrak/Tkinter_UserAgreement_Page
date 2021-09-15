
# Importing required modules
from tkinter import *   
import tkinter as tk
import tkinter.scrolledtext as st
  
# Creating tkinter window
win = tk.Tk()

win.attributes('-fullscreen', True)
win.attributes('-topmost', True)

win.title("User Agreement")
  
# Title Label
tk.Label(win, 
         text = "User Agreement", 
         font = ("Times New Roman", 25), 
         foreground = "black").grid(column = 0,
                                    row = 0,pady = 50)
  
# Creating scrolled text area
# widget with Read only by
# disabling the state
text_area = st.ScrolledText(win,
                            width = 150, 
                            height = 25, 
                            font = ("Times New Roman",
                                    15))

text_area.grid(column = 0, pady = 80, padx = 500)

text = ""
filename = 'agreement.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    text += line

# print(text)

text_area.insert(tk.INSERT,text, ("centered",))
text_area.tag_configure("centered", justify="center")

b1 = tk.Button(win, text='Okudum onaylıyorum.', width=20, height=3, command=quit)
b1.grid()

# Making the text read only
text_area.configure(state ='disabled')
win.mainloop()
