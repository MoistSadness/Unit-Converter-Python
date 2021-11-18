'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 
#       A quick GUI application that converts 
#       values between different unit conversions
#
#   https://www.dummies.com/programming/python/using-tkinter-widgets-in-python/
#
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

from tkinter import *


class Converter:
    def __init__(self, master):
        # Configure the window here
        self.master = master
        master.title("Converter")
        master.geometry("900x300")

        # Frames here
        self.topFrame = Frame(master)
        self.botFrame = Frame(master)

        self.metricTuple = ("Milimeters", "Centimeters", "Meters", "Kilometers")
        self.imperialTuple = ("Inches", "Feet", "Yards", "Miles")

        # Widgets here
        self.inputValue = "\t"
        self.inputValueWidget = Entry(self.topFrame, text = self.inputValue)

        '''
        self.originalUnit = StringVar("\t")
        self.originalDefault = "\t"
        self.originalUnitWidget = OptionMenu(self.topFrame, )
        '''

        self.to = Label(self.topFrame, text = "\tTO\t")

        '''
        self.newUnit = StringVar("\t")
        self.newDefault = "\t"
        self.newUnitWidget = OptionMenu(self.topFrame, )
        '''

        self.calculateButton = Button(self.botFrame, text = "CALCULATE")

        self.result = "\t"
        self.resultWidget = Label(self.botFrame, text = self.result)

        # Render Widgets here
        self.topFrame.grid(row = 0, column = 0)
        self.botFrame.grid(row = 1, column = 0)

        self.inputValueWidget.grid(row = 0, column = 0)
        #self.originalUnitWidget.grid(row = 0, column = 1)
        self.to.grid(row = 0, column = 2)
        #self.newUnitWidget.grid(row = 0, column = 3

        self.calculateButton.grid(row = 0, column = 0)
        self.resultWidget.grid(row = 1, column = 0)

        


root = Tk()
application = Converter(root)
root.mainloop()