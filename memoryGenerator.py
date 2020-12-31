import pyglet
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



# size configurations
window = pyglet.window.Window(resizable=True)  
window.set_size(1000,800)  
window.set_caption('Memory Generator') 

randomVideo = getVideo()

# get video
vidPath = 'videos/' + randomVideo
player = pyglet.media.Player()
source = pyglet.media.StreamingSource()
MediaLoad = pyglet.media.load(vidPath)
player.queue(MediaLoad)
myWidth = player.source.video_format.width*0.7 
myHeight = player.source.video_format.height*0.7

player.play()


@window.event
def on_draw():
    if player.source and player.source.video_format:
        player.get_texture().blit(100,100,width=myWidth,height=myHeight)


pyglet.app.run()
