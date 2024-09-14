"""
A simple PySimpleGUI application that creates a window with various UI elements.

This application demonstrates how to set up a basic PySimpleGUI window with:
- Text elements
- A spin control
- Buttons
- An input field

The application remains open until the user closes the window.

Usage:
    Run this script to see a basic window with interactive elements.
"""

import PySimpleGUI as sg

# Define the layout of the window (each element is a row of its own)
layout = [
    [sg.Text('Text'), sg.Spin(['item 1', 'item 2'])],
    [sg.Button('Click')],
    [sg.Input()],
    [sg.Text('Test'), sg.Button('Test Button')]
]

# Create the window with the title 'Converter' and the defined layout
window = sg.Window('Converter', layout)

# Event loop to process events and update the window
while True:
    event, values = window.read()  # Read the events and values from the window

    # If the window close button is clicked, exit the loop
    if event == sg.WIN_CLOSED:
        break
    # Additional event handling code can be added here

# Close the window after exiting the event loop
window.close()
