#!/usr/bin/env python3
import PySimpleGUI as sg # GUI
import webbrowser # Redirect user to HTML web browser
import http.client # POST
import traceback # error handling
import ssl # Required for POST
import base64 # converting icon image
from html import escape # safe POST
from fake_useragent import UserAgent # to fake user agent dynamically
import sys # for icon / file load at OS level
import darkdetect # OS level dark mode / light mode detection for theming

# Darkmode/light mode

color="#272727"

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
            size=(0, 1), 
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
        sg.Button('Post', expand_x=True)
    ],
    [
        [sg.Text("Create your account at: https://gemlog.blue", 
            background_color=color, 
            tooltip="https://gemlog.blue", 
            enable_events=True, 
            key=f'URL {"https://gemlog.blue"}')
        ],
        [sg.Text("Gemini spec: https://gemini.circumlunar.space/docs/specification.gmi", 
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

# Helpers

def postNewContent(values):
    # progress bar
    progress_bar = window['progress']
    progress_bar.update(visible=True)
    progress_bar.UpdateBar(0, 5)

    # Content
    postTitle = escape(values[0]).encode('utf-8').decode('unicode-escape')
    postContent = escape(values['textbox']).encode('utf-8').decode('unicode-escape')
    username = values[1]
    password = values[2]
    progress_bar.UpdateBar(1, 5)

    # user agent 
    ua = UserAgent()

    # Network call
    conn = http.client.HTTPSConnection("gemlog.blue", context = ssl._create_unverified_context())
    progress_bar.UpdateBar(2, 5)
    payload = f'title={postTitle}&post={postContent}&gemloguser={username}&pw={password}'
    headers = {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Origin': 'https://gemlog.blue',
      'Content-Length': '2993',
      'Accept-Language': 'en-US,en;q=0.9',
      'Host': 'gemlog.blue',
      'User-Agent': f'{ua.random}',
      'Referer': 'https://gemlog.blue/post.php',
      'Accept-Encoding': 'gzip, deflate, br',
      'Connection': 'keep-alive'
    }
    conn.request("POST", "/post.php", payload, headers)
    progress_bar.UpdateBar(3, 5)

    # Response
    res = conn.getresponse()
    progress_bar.UpdateBar(4, 5)

    if res.status == 200:
        progress_bar.UpdateBar(5, 5)
        progress_bar.update(visible=False)
        clicked = sg.Popup(f'Success! View your post @ gemini://gemlog.blue/users/{username}', keep_on_top=True)
        if clicked == 'OK':
            webbrowser.open(f'https://portal.mozz.us/gemini/gemlog.blue/users/{username}')

# Event Loop to process "events" and get the "values" of the inputs
try:
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break
        elif event.startswith("URL "): # inline urls open the native web browser
                url = event.split(' ')[1]
                webbrowser.open(url)
        elif event == 'Post': # POST to gemlog.blue
            postNewContent(values)
except Exception as e: # Crash handling
    print(e)
    sg.popup_error_with_traceback(f'An error happened.  Here is the info:', e)
