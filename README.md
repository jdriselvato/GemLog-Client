# README

A simple client to post to gemlog.blue

Test directory: [gemini://gemlog.blue/users/TestableClient/](https://portal.mozz.us/gemini/gemlog.blue/users/TestableClient/)

# Python3 Requirements

I found running `python3 -m pip install` works the best on MacOS

```
python3 -m pip install pyinstaller
python3 -m pip install fake_useragent
python3 -m pip install PySimpleGUI
python3 -m pip install darkdetect # dark mode detection
python3 -m pip install install darkdetect[macos-listener] # MacOS only
```


# Building app

### On MacOS

run `./source/build.sh`


### On Linux (Alpine)

```
apk add python3
apk add py3-pip
apk add python3-tkinter # pip3 wouldn't install properly
```

run `./source/build_linux.sh` 

# Screenshot

<img width="881" alt="GemLogBlue client v0.61" src="https://github.com/jdriselvato/GemLog-Client/blob/main/Screenshots/v0.61.png">

# Features

- Posting to gem.blue with your own account (via HTTP)
- Browsing the latest post in the built in mini-browser (native)
- Browsing random posts from current `username`
- HTTP browser viewing support via https://portal.mozz.us/gemini/
- Light/Dark mode support (MacOS/Linux/Window)

# About Gemini

- [https://gemini.circumlunar.space/docs/specification.gmi](https://gemini.circumlunar.space/docs/specification.gmi)

# Special thanks

- Q for introducing me to Gemini and app icon
- Whoever made gemlog.blue
- My wife for letting me working on this during the late hours of 02/24/2023