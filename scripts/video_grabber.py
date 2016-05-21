import urllib
from urllib import request
import os


if not os.path.exists("videos"):
    os.makedirs("videos")


    
def get_video(url):
    global pat2
    url = url
    path = url.split("/")
    path = path[-1]
    pat2 = path
    print (path)
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    resp = resp.read()
    file = open("videos/"+str(path),"wb")
    file.write(resp)
    file.close()


def keeping_track(curr):
    file = open ("tracking","wt")
    file.write(str(curr))
    file.close()
    
def loading_tracked():
    num = []
    file = open("tracking","rt")
    for lines in file:
        num.append(lines)
    file.close()
    return int(num[0])
    

starting = 1

if os.path.exists("tracking"):
    starting = loading_tracked()
    
for i in range (starting,153):
    print ("Downloading")
    keeping_track(i)
    if i > 9 and i < 100:
        get_video("http://107.155.78.122/~saiyanwatch2/Dragon%20Ball/0"+str(i)+".mp4")
    if i > 99:
        get_video("http://107.155.78.122/~saiyanwatch2/Dragon%20Ball/"+str(i)+".mp4")
    if i <= 9:
        get_video("http://107.155.78.122/~saiyanwatch2/Dragon%20Ball/00"+str(i)+".mp4")
        
    print ("Downloaded")
input()