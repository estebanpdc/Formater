import tkinter
import tkinter.font as tkFont
from TLV import TLV
from tkinter import *
from functools import partial

def clean(data):
    return re.sub(r'\s+', '', data)


OPTIONS = [
    "TLV",
    "APDU",
    "16 Block"] 


def addSpaces(data):
    result = ''
    isFirst = False
    for ch in data:
        result = result + ch + ('' if not isFirst else ' ')
        isFirst = not isFirst
    return result

def blockAlignment(data, size):
    data = clean(data)
    offset = 0;
    output = ""
    while(offset < len(data)):
        blockSize = min(size*2,len(data) - offset)
        output += addSpaces(data[offset:offset+blockSize]) + "\n"
        offset+=blockSize
    return output

def apduAligment(data):
    data = clean(data)
    header = data[:5*2]
    data = blockAlignment(data[5*2:],16)
    return addSpaces(header) + "\n" + data  
    

def parse(output, option, data):
    if(option.get() == OPTIONS[0]):
        data = str(TLV(data.get()))
    elif(option.get() == OPTIONS[1]):
        data = apduAligment(data.get())
    elif(option.get() == OPTIONS[2]):
        data = blockAlignment(data.get(), 16)
    output.delete("1.0", "end")
    output.insert(INSERT,data)
    return

def initPanedWindos():
    winMain = PanedWindow(orient=VERTICAL);
    winMain.pack(fill=BOTH,expand=1)
    
    winInput = PanedWindow(winMain, orient=HORIZONTAL);
    winInput.pack(fill=Y,expand=1)
    
    winOutput = PanedWindow(winMain, orient=HORIZONTAL,);
    winOutput.pack(fill=Y, expand=1)
    
    helv36 = tkFont.Font(family="Helvetica",size=10,weight="bold")
    outEntry = Text(winOutput, font=helv36)
    outEntry.insert(INSERT,"")
    winOutput.add(outEntry)
    
    label1 = Label(winInput, justify = LEFT, text = "Data to parse")
    winInput.add(label1)
    
    data = StringVar()
    
    entryData = Entry(winInput, textvariable=data)
    winInput.add(entryData)
    
    variable = StringVar()
    variable.set(OPTIONS[0]) # default value
    optionMenu = OptionMenu(winInput, variable, *OPTIONS)
    winInput.add(optionMenu)
    
    func = partial(parse, outEntry, variable, data)
    button1 = Button(winInput, text="Parse", command=func)
    winInput.add(button1)
    
    winMain.add(winInput)
    winMain.add(winOutput)
    
def main():
    initPanedWindos()
    mainloop()
    
    
main()

