import pygame
from moviepy.editor import *
import os, random
import json


# initialize screen
screenWidth = 2000
screenHeight = 1000



def countVideosPlayed(videosPlayed):
    lenOfVideosPlayed = 0
    for c in videosPlayed:
        if (c=='}'):
            lenOfVideosPlayed+=1

    return lenOfVideosPlayed

def getVideo():
    # get information on videos
    videoFolder = "videos/"
    listOfVideos = os.listdir(videoFolder)
    numberOfVideos = len(listOfVideos)
    randomVideoDir = random.choice(os.listdir(videoFolder))

    # initialize videos played
    videosPlayed = {}
    fileName = 'videosPlayed.txt'
    with open(fileName, 'r') as data:
        videosPlayed = data.read()
    numOfvideosPlayed = countVideosPlayed(videosPlayed)

    videoFound = False
    while (not videoFound):
        if numOfvideosPlayed == numberOfVideos:
            print("all videos have been played")
            with open(fileName, 'w'): pass
            break
        elif randomVideoDir in videosPlayed:
            print("video is found")
            randomVideoDir = random.choice(os.listdir(videoFolder))
        else:
            videoFound = True
            d = {}
            d[randomVideoDir] = 1
            with open(fileName, "a") as f:
                json.dump(d,f)
            print("added " + randomVideoDir)

    return randomVideoDir

def main():
    win = pygame.display.set_mode((screenWidth,screenHeight))

    randomVideo = getVideo()

    pygame.display.set_caption("Memory Generator")
    clip = VideoFileClip('videos/' + randomVideo)
    clip.resize(width = 1000, height = 600)
    clip.preview()

    pygame.quit()



if __name__ == "__main__":
    main()