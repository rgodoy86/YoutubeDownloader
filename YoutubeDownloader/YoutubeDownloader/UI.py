'''
Created on 2 Jan 2021

@author: rapha
'''
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from YoutubeDownloader.Downloader import *



def setPath():
    return filedialog.askdirectory()


def DownloadPressed(l, a, path='', ):
    messagebox.showinfo('Save As...', 'Select a folder to save your Video/Audio')
    link = l.get()
    audio = a.get()


    pathToSave = setPath()


    if pathToSave != '':
        messagebox.showinfo('Download starting',
                            '''Downloading starting...\
                            \nIt might take some seconds, please wait.''')

         
        yt = load(link)
        st = streams(yt, audio)

        download(st, pathToSave)

        titleString = title(yt)
        messageString = f'''File \
                            \n{titleString} \
                            \nwas successfully download. \
                            \nPress enter to continue.'''

        messagebox.showinfo(titleString, messageString)


def main():

    root = Tk()
    root.title('Youtube Downloader')
    audioFlag = BooleanVar()
    linkString = StringVar()

    Label(root, text="YouTube Link:").grid(row=0, column=0, sticky=W)
    Label(root, text="Audio Only?").grid(row=1, column=0, sticky=W)

    linkEntry = Entry(root,
                      textvariable=linkString,
                      width=40).grid(row=0, column=1)

    audioOnlyCheck = Checkbutton(root,
                                 text="Yes",
                                 variable=audioFlag,
                                 onvalue=True, offvalue=False).grid(row=1, column=1, sticky=W)

    downloadButton = Button(root,
                            text="DOWNLOAD",
                            command= lambda: DownloadPressed(linkString, audioFlag)).grid(row=2, column=1, sticky=E)

    root.mainloop()
    #print(setPath() != '')


if __name__ == '__main__':
    main()