from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from threading import Thread
import yt_dlp


def ui_generator():
    root = Tk()
    root.geometry('500x300')
    root.resizable(0, 0)
    root.title("YTDownloader")

    Label(root, text='YouTube Downloader', font='arial 20 bold').pack()

    link = StringVar()

    Label(root, text='YouTube video URL link:', font='arial 15 bold').place(x=130, y=60)
    Entry(root, width=70, textvariable=link).place(x=32, y=90)

    radio_value = StringVar()

    R1 = Radiobutton(root, text="MP3", variable=radio_value, value="mp3")
    R1.place(x=190, y=120)
    R1.select()
    R2 = Radiobutton(root, text="MP4", variable=radio_value, value="mp4")
    R2.place(x=250, y=120)
    R2.deselect()

    button2 = Button(root, text='Choose location', font='arial 15 bold', bg='burlywood2', padx=2)
    button2.place(x=160, y=200)
    Label(root, text='Download location:', font='arial 10 bold').place(x=30, y=250)
    label2 = Label(root, text="", font='arial 10')
    label2.place(x=160, y=250)
    button2.configure(command=lambda: location(root, label2))

    button = Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2)
    button.place(x=180, y=150)
    button.configure(command=lambda: downloader(link, button, radio_value, button2, label2))
    return root


def location(root, label2):
    dir_name = filedialog.askdirectory(parent=root, initialdir="/", title='Please select a directory')
    label2.configure(text=dir_name)


def downloader(link, button, radiovalue, button2, label2):
    if label2.cget("text") != "":
        if radiovalue.get() == 'mp3':
            t1 = Thread(target=mp3_download, args=(link, button, button2, label2))
            t1.start()
        else:
            t2 = Thread(target=mp4_download, args=(link, button, button2, label2))
            t2.start()
    else:
        messagebox.showwarning("Warning", "You must specify download location!")


def mp3_download(link, button, button2, label2):
    path = label2.cget("text") + "/%(title)s.%(ext)s"
    ydl_opts = {
        'outtmpl': path,
        'format': 'mp3/bestaudio/best',
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }
    download(link, button, button2, ydl_opts, "MP3")


def mp4_download(link, button, button2, label2):
    path = label2.cget("text") + "/%(title)s.%(ext)s"
    ydl_opts = {
        'outtmpl': path,
        'format': 'mp4'
    }
    download(link, button, button2, ydl_opts, "MP4")


def download(link, button, button2, ydl_opts, type):
    button.config(state="disabled")
    button2.config(state="disabled")
    URLS = [str(link.get())]
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(URLS)
        messagebox.showinfo("Info", type + " is downloaded!")
        button.config(state="normal")
        button2.config(state="normal")
    except:
        messagebox.showwarning("Warning", "Bad link!")
        button.config(state="normal")
        button2.config(state="normal")


def run():
    window = ui_generator()
    window.mainloop()


if __name__ == '__main__':
    run()
