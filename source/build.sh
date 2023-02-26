
# MacOS build
pyinstaller -i ./appIcon.png --add-data="appIcon.png:." --windowed ./client.py --distpath ../releases/macOS/ --workpath ./tmp --collect-data fake_useragent;