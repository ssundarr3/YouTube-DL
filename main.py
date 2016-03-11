from bs4 import BeautifulSoup
import requests 
import urllib.request, urllib.parse, urllib.error

def playlist(url, quality, start):
    replace_string = "><*?|\/" 
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    for link in soup.findAll('a', {'class': 'pl-video-title-link yt-uix-tile-link yt-uix-sessionlink  spf-link '}):
        if(start > 1):
            start-=1
            continue
        file_name = link.text.replace("  ", "").replace("\n", "")
        for i in replace_string:
            file_name = file_name.replace(i, "")
        youtub("https://www.youtube.com" + link.get("href"), quality, file_name)

def youtub(youtube_url, quality, name):
    soup = BeautifulSoup(requests.get(youtube_url.replace("youtube", "youmagictube")).text, "html.parser")
    for link in soup.findAll('a', {}):
        href = link.get("href")
        if(quality == ".mp3" and "DownloadFile" in href):
            savvid(href, ".mp3", name)
            break
        elif(quality in href):
            savvid(href, quality, name)
            break


def savvid(url, quality, name):
    soup = BeautifulSoup(requests.get("http://www.save-video.com/" + url).text, "html.parser")
    if(quality == ".mp3"):
        quality=".flv"
    for link in soup.findAll('a', {}):
        href = link.get("href")
        if("google" in href):
            size = href.index(' ') -1
            href = href[:size]
            urllib.request.urlretrieve(href, str(name + quality))


q="q"
while(q != "quit"):
    c1 = input("playlist or single video?\nEnter 1 for playlist 2 for single video... ")
    if(c1.isdigit()):
        c1 = int (c1)
    else:
        continue
    if(c1 == 1):
        c2_url = input("\nEnter the playlist page's url ")
        c2_quality = input("Enter the quality eg  .mp4, .flv, .web ")
        c2_start = input("\nEnter the video to start from (Enter 1 to start downloading from the beginning... ")
        c2_start = int(c2_start)
        playlist(c2_url, c2_quality, c2_start)
    elif(c1 == 2):
        c3_url = input("\nEnter the YouTube page's url ")
        c3_quality = input("Enter the quality eg  .mp4, .flv, .web ")
        c3_name = input("\nEnter the the name of the file you would like to save as... ")
        youtub(c3_url, c3_quality, c3_name)
    else:
        print("That's not a valid option... Please try again ")
    q = input("\nWould you like to quit?Enter 'quit' to do so... ")


   
