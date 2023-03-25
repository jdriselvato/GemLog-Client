import Agunua # communicate to gemini protocol (Agunua) - https://framagit.org/bortzmeyer/agunua
import Agunua.status # debugging status for Agunua
import random # for browsing
import ssl # Required for POST
from html import escape # safe POST
from fake_useragent import UserAgent # to fake user agent dynamically
import webbrowser # Redirect user to HTML web browser
import http.client # POST
import PySimpleGUI as sg # GUI

# Helpers

def postNewContent(progress_bar, values):
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

def openGeminiUri(uri):
    u = Agunua.GeminiUri(
            uri, 
            accept_expired=True, 
            insecure=True,
            parse_content=True
        )
    if u.network_success:
        if u.status_code == "20":
            if u.links is not None and u.links != []:
                return u.links
        else:
            sg.Popup("Status code is %s" % Agunua.status.codes[u.status_code], keep_on_top=True)

def contentFromGeminiUri(uri):
    u = Agunua.GeminiUri(
            uri, 
            accept_expired=True, 
            insecure=True,
            parse_content=True
        )
    if u.network_success:
        if u.status_code == "20":
            return u.payload
        else:
            sg.Popup("Status code is %s" % Agunua.status.codes[u.status_code], keep_on_top=True)

def getLatestPost(values):
    username = values[1]
    uri = f'gemini://gemlog.blue/users/{username}/'
    sublinks = openGeminiUri(uri)
    payload = contentFromGeminiUri(sublinks[0])
    return payload

def getRandomPost(values):
    username = values[1]
    uri = f'gemini://gemlog.blue/users/{username}/'
    sublinks = openGeminiUri(uri)
    payload = contentFromGeminiUri(random.choice(sublinks))
    return payload
