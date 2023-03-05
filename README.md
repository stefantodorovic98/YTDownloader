# YTDownloader

YTDownloader is an application for downloading videos from YouTube in MP3 and MP4 format. 

## Prerequisites

Project is written in python-3.10.10-amd64 ([link](https://www.python.org/ftp/python/3.10.10/python-3.10.10-amd64.exe)).

Tkinter is a standard library in Python which is used for GUI.

```bash
pip install tk
```

yt-dlp is a command-line tool that allows you to download videos from YouTube. Version can be found in requirements.txt file.


```bash
pip install yt-dlp
```

Additional, in project is used FFmpeg. You should download FFmpeg version 6.0 from [link](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z). Put FFmpeg folder in C directory (like C:\FFmpeg\bin\), and update the Path environment variable.

## Making Executable Application

Go to project directory and run:
```bash
pyinstaller.exe --onefile --paths=./venv/Lib main.py
```
Download the application from [link](https://www.4shared.com/s/ffE70n0T_jq).

### Important Note

The application takes more time to download MP3 than MP4.

Downloading MP3 consists of two phases:
1. MP4 is downloaded
2. MP3 is extracted from downloaded MP4 (Extraction process is time consuming)

## Warning

This project is written for educational purposes!
