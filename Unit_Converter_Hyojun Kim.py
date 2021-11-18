from tkinter import *
import tkinter.messagebox

unit_dict = {"cm" : 0.01, "m" : 1.0, "km": 1000.0, "feet": 0.3048, "miles": 1609.344, "inches": 0.0254, "yard": 0.9144, "mm": 0.001}

lengths = ["km", "m", "cm", "mm", "miles", "yard", "feet", "inches"]

OPTIONS = ["select units", "km", "m", "cm", "mm", "miles", "yard", "feet", "inches"]

#Use the root function to make a outline
root = Tk()
root.geometry("500x300")
root.title("Unit Converter_Hyojun Kim")
root['bg'] = 'gray'

#Use the def function to make a code works well
def ok(): 
    try:
        inp = float(inputentry.get()) #Float number is available
    except:
        tkinter.messagebox.showerror("Error","Please enter interger only!") #If something that isn't Interger is input in input box, Error message will pop up
    
    inp_unit = inputopt.get()
    out_unit = outputopt.get()
    
    cons = [inp_unit in lengths and out_unit in lengths]
    
    if cons: 
        outputentry.delete(0, END)
        try:
            outputentry.insert(0, round(inp * unit_dict[inp_unit]/unit_dict[out_unit], 5))
        except:
            outputentry.insert(0, "ERROR")

    else: 
        outputentry.delete(0, END)


inputopt = StringVar()
inputopt.set(OPTIONS[0])

outputopt = StringVar()
outputopt.set(OPTIONS[0])

#Create the label
inputlabel = Label(root, text = "Input\n(Interger Only!)") #Let you know, only Interger shoulb be input
inputlabel.grid(row = 0, column = 0, pady = 20)

inputentry = Entry(root, justify = "center")
inputentry.grid(row = 1, column = 0, padx = 35, ipady = 5)

inputmenu = OptionMenu(root, inputopt, *OPTIONS)
inputmenu.grid(row = 1, column = 1)

outputlabel = Label(root, text = "Output")
outputlabel.grid(row = 2, column = 0, pady = 20)

outputentry = Entry(root, justify = "center")
outputentry.grid(row = 3, column = 0, padx = 35, ipady = 5)

outputmenu = OptionMenu(root, outputopt, *OPTIONS)
outputmenu.grid(row = 3, column = 1)

okbutton = Button(root, text = "OK", command = ok, padx = 80, pady = 2)
okbutton.grid(row = 4, column = 0, pady = 50)

root.mainloop()
