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
from html import escape
```


# Building app

Building a stand alone app took a minute but I found pyinstaller was the easiest

`pyinstaller --windowed client.py `

# About Gemini

- [https://gemini.circumlunar.space/docs/specification.gmi](https://gemini.circumlunar.space/docs/specification.gmi)

# Special thanks

- Q for introducing me to Gemini
- Whoever made gemlog.blue
- My wife for letting me working on this during the late hours of 02/24/2023