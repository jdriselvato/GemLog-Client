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

<img width="517" alt="Screen Shot 2023-02-26 at 09 55 38" src="https://user-images.githubusercontent.com/950825/221418186-aec67d59-36bb-492c-bf3d-9a419f64492e.png">

# About Gemini

- [https://gemini.circumlunar.space/docs/specification.gmi](https://gemini.circumlunar.space/docs/specification.gmi)

# Special thanks

- Q for introducing me to Gemini and app icon
- Whoever made gemlog.blue
- My wife for letting me working on this during the late hours of 02/24/2023