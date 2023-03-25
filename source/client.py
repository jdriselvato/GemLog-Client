#!/usr/bin/env python3
import gem_module
import PySimpleGUI as sg # GUI
import traceback # error handling
import base64 # converting icon image
import sys # for icon / file load at OS level
import darkdetect # OS level dark mode / light mode detection for theming

# Darkmode/light mode

color="#272727" # MTHU black
secondaryColor="#329033" # a mint green

def setupTheme(arg):
    global color
    if arg == "Dark":
        sg.theme('Black')
        color="#272727"
    else:
        sg.theme('GrayGrayGray')
        color="#d8d8d8"

setupTheme(darkdetect.theme())

# Application Icon

def getIcon():
    if getattr(sys, 'frozen', False):
        icon = os.path.join(sys._MEIPASS, "appIcon.png")
        return base64.b64encode(
            open(icon, 'rb').read()
        )
    else:
        return base64.b64encode(
            open("appIcon.png", 'rb').read()
        )

layout = [
    [
        sg.Text('Title:', # title
            key='title', 
            background_color=color,
        ), sg.InputText(),
        sg.ProgressBar(1, orientation='h', size=(20, 20), key='progress', expand_x=True, visible=False)
    ],
    [
        sg.Text('Post content* (text/gemini format):', background_color=color), # hint / tip text
    ],
    [
        sg.Multiline(
            size=(0, 20), 
            key='textbox',
            expand_x=True,
            expand_y=True
        ),
    ],
    [
        sg.Text('Username:', key='username', background_color=color), sg.InputText("TestableClient"),
        sg.Text('Password:', key='password', background_color=color), sg.InputText("tegdun-6fybca-gukMat", password_char='*'),
        sg.Button('Post', expand_x=True, size=(10, 1))
    ],
    [sg.Sizer(0, 10)],
    [sg.HorizontalSeparator(color=secondaryColor)],
    [sg.Sizer(0, 10)],
    [
        [
            sg.Column(
                [
                    [sg.Text("Mini-browser", background_color=color)],
                    [sg.Button("Latest", key="-BROWSER-", size=(10, 1))],
                    [sg.Button("Random", key="-RANDOM-",  size=(10, 1))]
                ],
                element_justification="center",
                background_color=color
            ),
            sg.Multiline(
                key="-BROWSER_CONTENT-",
                expand_x=True,
                expand_y=True,
                disabled=True
            )
        ],
        [sg.Text("Create your account at: https://gemlog.blue", 
            background_color=color, 
            tooltip="https://gemlog.blue", 
            enable_events=True, 
            key=f'URL {"https://gemlog.blue"}'),
        sg.Text("Gemini spec: https://gemini.circumlunar.space/docs/specification.gmi", 
            background_color=color, 
            tooltip="https://gemini.circumlunar.space/docs/specification.gmi", 
            enable_events=True, 
            key=f'URL {"https://gemini.circumlunar.space/docs/specification.gmi"}')
        ]
    ]
]

# Create the Window
window = sg.Window(
    'GemLog.blue Client - Add an entry to your gemlog', 
    layout, 
    icon=getIcon(),
    return_keyboard_events=True, 
    resizable=True,
    finalize=True,
    background_color=color
)

# Event Loop to process "events" and get the "values" of the inputs
try:
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event.startswith("URL "): # in line urls open the native web browser
                url = event.split(' ')[1]
                webbrowser.open(url)
        elif event == 'Post': # POST to gemlog.blue
            # progress bar
            progress_bar = window['progress']
            progress_bar.update(visible=True)
            progress_bar.UpdateBar(0, 5)
            # Post content 
            gem_module.postNewContent(progress_bar, values)
            payload = gem_module.getLatestPost(values)
            window["-BROWSER_CONTENT-"].update(f"{payload}")
        elif event == '-BROWSER-': # print last post
            payload = gem_module.getLatestPost(values)
            window["-BROWSER_CONTENT-"].update(f"{payload}")
        elif event == '-RANDOM-':
            payload = gem_module.getRandomPost(values)
            window["-BROWSER_CONTENT-"].update(f"{payload}")

except Exception as e: # Crash handling
    print(e)
    sg.popup_error_with_traceback(f'An error happened.  Here is the info:', e)
