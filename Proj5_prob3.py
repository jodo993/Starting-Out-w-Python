# Joseph Do
# Project 5
# Celsius to Fahrenheit
# This program will convert Celsius to Fahrenheit and vice versa

import tkinter
import tkinter.messagebox

class MyGUI():
    def __init__(self):
        # Create main window
        self.main_window = tkinter.Tk()

        # Create label frame, result frame, button frame
        self.label_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()

        # Create and pack widget for label
        self.input_label = tkinter.Label(self.label_frame,
                                        text="Enter degree:")
        self.temperature_entry = tkinter.Entry(self.label_frame,
                                         width=10)
        self.input_label.pack(side='left')
        self.temperature_entry.pack(side='left')

        # Create and pack widget for result
        self.result_label = tkinter.Label(self.result_frame,
                                          text="Converted temperature is:")
        self.newT = tkinter.StringVar()
        self.newResult_label = tkinter.Label(self.result_frame,
                                           textvariable=self.newT)
        self.result_label.pack(side='left')
        self.newResult_label.pack(side='left')

        # Create and pack button widgets
        self.calculate_buttonF = tkinter.Button(self.button_frame,
                                               text='Convert to Fahrenheit',
                                               command=self.convertToFahrenheit)
        self.calculate_buttonC = tkinter.Button(self.button_frame,
                                               text='Convert to Celsius',
                                               command=self.convertToCelsius)
        self.calculate_buttonF.pack(side='left')
        self.calculate_buttonC.pack(side='left')

        # Pack frames
        self.label_frame.pack()
        self.result_frame.pack()
        self.button_frame.pack()

        # Start the mainloop
        tkinter.mainloop()

    # Convert celsius to fahrenheit
    def convertToFahrenheit(self):

        # Get the temperature
        temp = float(self.temperature_entry.get())

        # Convert
        fahrenheit = (9/5)*temp + 32

        # Update label
        self.newT.set(fahrenheit)

    # Convert fahrenheit to celsius
    def convertToCelsius(self):

        # Get the temperature
        temp = float(self.temperature_entry.get())

        # Convert
        celsius = (temp - 32) * (5/9)

        # Update label
        self.newT.set(celsius)

# Create instance of class
my_gui = MyGUI()
