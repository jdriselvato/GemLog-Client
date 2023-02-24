#!/usr/bin/env python3
import PySimpleGUI as sg
import webbrowser

# Theme

# sg.theme('DarkAmber')

# Constants

layout = [
    [
        sg.Text('title:', size =(15, 1), key='username'), sg.InputText(),
    ],
    [
        sg.Text('Post content* (text/gemini format):'), # hint / tip text
    ],
    [
        sg.Multiline(size=(120, 40), key='textbox'),
    ],
    [
        sg.Text('Username:', size =(9, 1), key='username'), sg.InputText(),
        sg.Text('Password:', size =(9, 1), key='password'), sg.InputText(),
        sg.Button('Post'), # hint button
    ],
    [
        sg.Text("Read more here: https://gemlog.blue", tooltip="https://gemlog.blue", enable_events=True, key=f'URL {"https://gemlog.blue"}')
    ]
]

# Create the Window

window = sg.Window('GemLog.blue Client - Add an entry to your gemlog', layout, return_keyboard_events=True, finalize=True)
window.maximize()


# Event Loop to process "events" and get the "values" of the inputs

while True:
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED:
        break
    elif event.startswith("URL "):
            url = event.split(' ')[1]
            webbrowser.open(url)
    elif event == 'Post':
        postTitle = values['title']
        postContent = values['textbox']
        password = values['username']
        password = values['password']
        print(event, postContent, username, password)
