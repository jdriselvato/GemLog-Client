
# Linux build
pyinstaller -i ./appIcon.png --add-data="appIcon.png:." --onefile ./client.py --distpath ../releases/linux/ --workpath ./tmp --collect-data fake_useragent;
