# README

A simple client to post to gemlog.blue

Test directory: [gemini://gemlog.blue/users/TestableClient/](gemini://gemlog.blue/users/TestableClient/)

# Python3 Requirements

```
import PySimpleGUI as sg
import webbrowser
import http.client
import traceback # error handling
import ssl
import base64 # app icon
from html import escape
```

I found running `python3 -m pip install` works the best on MacOS


# Building app

Building a stand alone app took a minute but I found pyinstaller was the easiest

`pyinstaller -i ./source/appIcon.png --windowed ./source/client.py`

# About Gemini

- [https://gemini.circumlunar.space/docs/specification.gmi](https://gemini.circumlunar.space/docs/specification.gmi)

# Special thanks

- Q for introducing me to Gemini and app icon
- Whoever made gemlog.blue
- My wife for letting me working on this during the late hours of 02/24/2023