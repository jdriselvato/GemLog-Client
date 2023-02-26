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

### MacOS

`./source/build.sh`

# Screenshot

<img width="881" alt="Screen Shot 2023-02-26 at 09 55 18" src="https://user-images.githubusercontent.com/950825/221418162-6cfbc8a7-1d6b-455e-8217-2a3dd72035b8.png">

# About Gemini

- [https://gemini.circumlunar.space/docs/specification.gmi](https://gemini.circumlunar.space/docs/specification.gmi)

# Special thanks

- Q for introducing me to Gemini and app icon
- Whoever made gemlog.blue
- My wife for letting me working on this during the late hours of 02/24/2023