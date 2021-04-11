'''
Created on 2 Jan 2021
Macintosh HD > Applications > Python3.6 folder (or whatever version of python you're using) 

double click on "Install Certificates.command" file

@author: rapha
'''

from pytube import YouTube
import math


def load(link):
    return YouTube(link)

def overview(yt, full=False):
    print('Title: ', yt.title)
    if full is True: print('Number of views: ', yt.views) 
    print('Length of video: ', math.floor(yt.length/60), 'minutes and', yt.length % 60, 'seconds')
    if full is True: print('Description: ', yt.description)
    if full is True: print('Ratings: ', yt.rating)
    print()

def streams(yt, audioOnly=False):
    if audioOnly is False:
        return yt.streams.get_highest_resolution()
    else:
        return yt.streams.filter(only_audio=audioOnly)[0]

def title(yt):
    return yt.title


def download(yt, path):
    yt.download(path)



# youtubeLink = 'https://www.youtube.com/watch?v=KzARx0EuDgc'
# yt = load(youtubeLink)
# overview(yt, True)
# st = streams(yt, True)







