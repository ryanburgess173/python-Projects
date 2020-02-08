from tkinter import *

root = Tk()
label = Label(root, text="Hello Tkinter!")
button = Button(root, text="click me")

label.pack()
button.pack()

button['text'] = "press Me"
button.config(text = "push Me")

print(button.config())

root.mainloop()