#!/usr/bin/env python3
import PySimpleGUI as sg
import webbrowser
import http.client
import traceback # error handling
import ssl
from html import escape

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
        sg.Text('Password:', size =(9, 1), key='password'), sg.InputText("tegdun-6fybca-gukMat"),
        sg.Button('Post'), # hint button
    ],
    [
        sg.Text("Read more here: https://gemlog.blue", tooltip="https://gemlog.blue", enable_events=True, key=f'URL {"https://gemlog.blue"}')
    ],
    [
        sg.Text("Gemini spec: https://gemini.circumlunar.space/docs/specification.gmi", tooltip="https://gemini.circumlunar.space/docs/specification.gmi", enable_events=True, key=f'URL {"https://gemini.circumlunar.space/docs/specification.gmi"}')
    ]
]

# Create the Window

window = sg.Window(
    'GemLog.blue Client - Add an entry to your gemlog', 
    layout, 
    icon=base64.b64encode(open('./appIcon.png', 'rb').read()),
    return_keyboard_events=True, 
    finalize=True
)
window.maximize()


# Helpers

def postNewContent(values):
    print(values)
    postTitle = escape(values[0])
    postContent = escape(values['textbox'])
    username = values[1]
    password = values[2]

    print(event, postTitle, postContent, username, password)

    conn = http.client.HTTPSConnection("gemlog.blue", context = ssl._create_unverified_context())
    payload = f'title={postTitle}&post={postContent}&gemloguser={username}&pw={password}'
    headers = {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Origin': 'https://gemlog.blue',
      'Content-Length': '2993',
      'Accept-Language': 'en-US,en;q=0.9',
      'Host': 'gemlog.blue',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15',
      'Referer': 'https://gemlog.blue/post.php',
      'Accept-Encoding': 'gzip, deflate, br',
      'Connection': 'keep-alive'
    }
    conn.request("POST", "/post.php", payload, headers)
    res = conn.getresponse()

    if res.status == 200:
        clicked = sg.Popup(f'Success! View your post @ gemini://gemlog.blue/users/{username}', keep_on_top=True)
        if clicked == 'OK':
            webbrowser.open(f'https://portal.mozz.us/gemini/gemlog.blue/users/{username}')


# Event Loop to process "events" and get the "values" of the inputs
try:
    while True:
        event, values = window.read()
        print(event)
        if event == sg.WIN_CLOSED:
            break
        elif event.startswith("URL "):
                url = event.split(' ')[1]
                webbrowser.open(url)
        elif event == 'Post':
            postNewContent(values)
except Exception as e:
    sg.popup_error_with_traceback(f'An error happened.  Here is the info:', e)
