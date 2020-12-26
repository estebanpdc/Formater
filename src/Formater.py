import tkinter
from tkinter import *
from functools import partial

def parse(output, data):
    
    output.config(text=data.get())
    return



winMain = PanedWindow(orient=VERTICAL);
winMain.pack(fill=BOTH,expand=1)

winInput = PanedWindow(winMain, orient=HORIZONTAL);
winInput.pack(fill=Y,expand=1)

winOutput = PanedWindow(winMain);
winOutput.pack(fill=BOTH,expand=1)


label2 = Label(winOutput, text = "Result", bd=5)
winOutput.add(label2)

label1 = Label(winInput, text = "Data to parse")
winInput.add(label1)

data = StringVar()

entryData = Entry(winInput, textvariable=data)
winInput.add(entryData)

func = partial(parse, label2, data)
button1 = Button(winInput, text="Parse", command=func)
winInput.add(button1)

winMain.add(winInput)
winMain.add(winOutput)

mainloop()

