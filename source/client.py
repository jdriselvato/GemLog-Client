#!/usr/bin/env python3
import PySimpleGUI as sg
import webbrowser
import http.client
import traceback # error handling
import ssl
import base64 # icon image
from html import escape
from fake_useragent import UserAgent
import sys

# Constants

layout = [
    [
        sg.Text('title:', size =(15, 1), key='title'), sg.InputText(),
    ],
    [
        sg.Text('Post content* (text/gemini format):'), # hint / tip text
    ],
    [
        sg.Multiline(size=(120, 40), key='textbox'),
    ],
    [
        sg.Text('Username:', size =(9, 1), key='username'), sg.InputText("TestableClient"),
        sg.Text('Password:', size =(9, 1), key='password'), sg.InputText("tegdun-6fybca-gukMat", password_char='*'),
        sg.Button('Post'), # hint button
    ],
    [
        [sg.Text("Create your account at: https://gemlog.blue", tooltip="https://gemlog.blue", enable_events=True, key=f'URL {"https://gemlog.blue"}')],
        [sg.Text("Gemini spec: https://gemini.circumlunar.space/docs/specification.gmi", tooltip="https://gemini.circumlunar.space/docs/specification.gmi", enable_events=True, key=f'URL {"https://gemini.circumlunar.space/docs/specification.gmi"}')]
    ]
]

# Create the Window
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

window = sg.Window(
    'GemLog.blue Client - Add an entry to your gemlog', 
    layout, 
    icon=getIcon(),
    return_keyboard_events=True, 
    finalize=True
)
window.maximize()


# Helpers

def postNewContent(values):
    postTitle = escape(values[0]).encode('utf-8').decode('unicode-escape')
    postContent = escape(values['textbox']).encode('utf-8').decode('unicode-escape')
    username = values[1]
    password = values[2]
    print(event, postTitle, postContent, username, password)

    # user agent 
    ua = UserAgent()

    # Network call
    conn = http.client.HTTPSConnection("gemlog.blue", context = ssl._create_unverified_context())
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

    # Response
    res = conn.getresponse()

    if res.status == 200:
        clicked = sg.Popup(f'Success! View your post @ gemini://gemlog.blue/users/{username}', keep_on_top=True)
        if clicked == 'OK':
            webbrowser.open(f'https://portal.mozz.us/gemini/gemlog.blue/users/{username}')


# Event Loop to process "events" and get the "values" of the inputs
try:
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event.startswith("URL "):
                url = event.split(' ')[1]
                webbrowser.open(url)
        elif event == 'Post':
            postNewContent(values)
except Exception as e:
    print(e)
    sg.popup_error_with_traceback(f'An error happened.  Here is the info:', e)
