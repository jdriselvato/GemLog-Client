#!/usr/bin/env python3
import PySimpleGUI as sg

# Theme

sg.theme('DarkAmber')

# Constants

# Window init (Bebo's old header size)

window_width = 760
window_height = 375

layout = [
    [sg.Canvas(size=(window_width, window_height), key='canvas')],
    [
        sg.Button('Post'), # hint button
        sg.Text('', key='display_note_text'), # hint / tip text
        sg.Push(),
        sg.Text('', key='display_score', text_color="#2FF599"), # score text
    ],
]

# Create the Window

window = sg.Window('GemLog.blue Client', layout, return_keyboard_events=True, finalize=True)
window.maximize()


# Event Loop to process "events" and get the "values" of the inputs

while True:
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Post':
        print(event)
