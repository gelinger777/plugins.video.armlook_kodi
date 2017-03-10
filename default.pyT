#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import urlparse
import socket
import sys
import os
import re
import ssl
import requests
import xbmcplugin
import xbmcgui
import xbmcaddon
import json

addon = xbmcaddon.Addon()
socket.setdefaulttimeout(30)
pluginhandle = int(sys.argv[1])
addonID = addon.getAddonInfo('id')
translation = addon.getLocalizedString
addon_work_folder = xbmc.translatePath("special://profile/addon_data/"+addonID)
channelFavsFile = xbmc.translatePath("special://profile/addon_data/"+addonID+"/"+addonID+".favorites")
subFile = xbmc.translatePath("special://profile/addon_data/"+addonID+"/sub.srt")
baseUrl = "http://www.armlook.com"
defaultBackground = baseUrl+"/ZDFmediathek/img/fallback/946x532.jpg"

if not os.path.isdir(addon_work_folder):
    os.mkdir(addon_work_folder)

showSubtitles = addon.getSetting("showSubtitles") == "true"
forceViewMode = addon.getSetting("forceViewMode") == "true"
useThumbAsFanart = addon.getSetting("useThumbAsFanart") == "true"
viewMode = str(addon.getSetting("viewMode"))

minLength = addon.getSetting("minLength")
mins = [0, 5, 10, 20, 30]
minLength = mins[int(minLength)]


def index():
 
   import urllib, json

   #addDir("ArmeniaLiveTVs", "1", 'listLiveChannels', baseUrl+"/uploads/images/channels/banners/armenia.jpg") 
   addDir("ArmeniaTV Archive", "1", 'listChannel', baseUrl+"/uploads/images/channels/banners/armenia.jpg")  
   addDir("ArmeniaTV LIVE", "armenia", 'listChannelLive', baseUrl+"/uploads/images/channels/banners/armenia.jpg")
   addDir("Kentron", "3", 'listChannel', baseUrl+"/uploads/images/channels/banners/img_522fc19eb4449.jpg")
   addDir("Yerkir Media", "5", 'listChannel', baseUrl+"/uploads/images/channels/banners/yerk.jpg")
   addDir("LaymTV", "20", 'listChannel', baseUrl+"/uploads/images/channels/thumbnails/laym.jpg")
   addDir("AR-TV", "22", 'listChannel', baseUrl+"/uploads/images/channels/thumbnails/artv.jpg")
   addDir("Dar21", "19", 'listChannel', baseUrl+"/uploads/images/channels/thumbnails/21.jpg")
   addDir("ShoghakatTV", "21", 'listChannel', baseUrl+"/uploads/images/channels/thumbnails/shogh-541.jpg")
   addDir("PanArmenianTV", "21", 'listChannel', baseUrl+"/uploads/images/channels/thumbnails/img_54d2f9a578d1b.jpg")
   addDir("ATV", "25", 'listChannel', baseUrl+"/uploads/images/channels/banners/img_548ea6775a962.jpg")
   addDir("ShantTV", "2", 'listChannel', baseUrl+"/uploads/images/channels/banners/shant-1_1601x600.jpg")
   addDir("H1", "6", 'listChannel', baseUrl+"/uploads/images/channels/banners/img_524a280b02277.jpg")
   addDir("Armnews", "4", 'listChannel', baseUrl+"/uploads/images/channels/banners/armnewsbanner.jpg")
   addDir("Megre 1 ","http://cdn1.seriadata.net/video/C7BsclZgxf2-6eidwhu6ZQ/1/9/1977/1/1.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 2 ","http://cdn1.seriadata.net/video/9HfI2DWuMXqcPJZ2_iHHCA/1/9/1977/1/2.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 3 ","http://cdn1.seriadata.net/video/EjjhWS1BJuHUqDU7HFTU-A/1/9/1977/1/3.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 4 ","http://cdn1.seriadata.net/video/Doo9iJZbUy9QWmMJpnP_Iw/1/9/1977/1/4.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 5 ","http://cdn1.seriadata.net/video/ZKXn7TnObN6YihI7I6W5Yw/1/9/1977/1/5.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 6 ","http://cdn1.seriadata.net/video/xA-h3jeYGdSIYrjWQgzHRg/1/9/1977/1/6.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 7 ","http://cdn1.seriadata.net/video/ocKx6M7_420uC3Bu4tv9RA/1/9/1977/1/7.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 8 ","http://cdn1.seriadata.net/video/xjYV4aFxba_hVj1eTsNcqw/1/9/1977/1/8.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 9 ","http://cdn1.seriadata.net/video/4fysDAOAhAWeK4ec2psvng/1/9/1977/1/9.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 10 ","http://cdn1.seriadata.net/video/ySn07KMmCPRAeXc8FcrxpA/1/9/1977/1/10.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 11 ","http://cdn1.seriadata.net/video/ZbyKS0QBiKJo-7Ds2N_Efw/1/9/1977/1/11.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 12 ","http://cdn1.seriadata.net/video/w6NmcpQMC1o-KfDHb0VoeQ/1/9/1977/1/12.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 13 ","http://cdn1.seriadata.net/video/Ixfyv5y0l80P1elCU5WUqA/1/9/1977/1/13.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 14 ","http://cdn1.seriadata.net/video/m0UgSzSMh4Q2KgeJN-3aoA/1/9/1977/1/14.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 15 ","http://cdn1.seriadata.net/video/svKZQ_PAp8xTs9ec9oxh_Q/1/9/1977/1/15.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 16 ","http://cdn1.seriadata.net/video/h5ZGBrMaraDO46_KwgGeFQ/1/9/1977/1/16.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 17 ","http://cdn1.seriadata.net/video/SrCJjoDT3Ykrraz1d_tAKg/1/9/1977/1/17.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 18 ","http://cdn1.seriadata.net/video/1lGvGYLnjuKOuV3qrungnQ/1/9/1977/1/18.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 19 ","http://cdn1.seriadata.net/video/cEhrL7KE207gLZC-KOMTgw/1/9/1977/1/19.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 20 ","http://cdn1.seriadata.net/video/2fdxR5052NLBofcrQXppeg/1/9/1977/1/20.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 21 ","http://cdn1.seriadata.net/video/wwIavckA42EtDPquI8HrWg/1/9/1977/1/21.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 22 ","http://cdn1.seriadata.net/video/A6npfIGw8amfbiUPxBgQoA/1/9/1977/1/22.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 23 ","http://cdn1.seriadata.net/video/Z8lKgKIBupk1ne5OyUSMIQ/1/9/1977/1/23.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 24 ","http://cdn1.seriadata.net/video/p5uxsvuIqugZyV7YIVQhTA/1/9/1977/1/24.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 25 ","http://cdn1.seriadata.net/video/-3xVh56PU-FjGRc6BIdrGA/1/9/1977/1/25.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 26 ","http://cdn1.seriadata.net/video/guTW-iYsirh1_9eUQ_638g/1/9/1977/1/26.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 27 ","http://cdn1.seriadata.net/video/7M2rg0lGrV0NwHRUcYQGNg/1/9/1977/1/27.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 28 ","http://cdn1.seriadata.net/video/4t0sJSBYe_1e8EANu-6vOQ/1/9/1977/1/28.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 29 ","http://cdn1.seriadata.net/video/Ti6CFWBo8L5JVi6LfJWm6Q/1/9/1977/1/29.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 30 ","http://cdn1.seriadata.net/video/op_6Y8l0ZFnXYE0RTULulw/1/9/1977/1/30.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 31 ","http://cdn1.seriadata.net/video/3v7lAkIKnO3MzHZHOMPOCw/1/9/1977/1/31.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 32 ","http://cdn1.seriadata.net/video/sxn9yMSrNKHlFpOk2QPE2Q/1/9/1977/1/32.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 33 ","http://cdn1.seriadata.net/video/cZ7cSxxCYHcNTck45olPew/1/9/1977/1/33.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 34 ","http://cdn1.seriadata.net/video/QI_-0ZWXnp_ZQpHsZep0gg/1/9/1977/1/34.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 35 ","http://cdn1.seriadata.net/video/7Y9A1fOCKKzpAs1VKUTSjg/1/9/1977/1/35.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 36 ","http://cdn1.seriadata.net/video/Yjk3VfVRlK1hWOjc5TQVbg/1/9/1977/1/36.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 37 ","http://cdn1.seriadata.net/video/PGfr377eKByGCmnRL7V7kw/1/9/1977/1/37.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 38 ","http://cdn1.seriadata.net/video/jDSx9mG2tLLghI3nnZ2c9A/1/9/1977/1/38.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 39 ","http://cdn1.seriadata.net/video/VrvbualNl8I9TSaTeuTwxg/1/9/1977/1/39.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 40 ","http://cdn1.seriadata.net/video/ympyLcwk7dG34YtkQlxaBQ/1/9/1977/1/40.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 41 ","http://cdn1.seriadata.net/video/jBLg0vm491yFiMj8rNDobw/1/9/1977/1/41.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 42 ","http://cdn1.seriadata.net/video/x3Ibfz24Tk4AYVNFVR4Wmg/1/9/1977/1/42.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 43 ","http://cdn1.seriadata.net/video/exxQEd_63W6PT8NABTwHxQ/1/9/1977/1/43.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 44 ","http://cdn1.seriadata.net/video/9vsAdQuY8T1clRHHu5smcw/1/9/1977/1/44.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 45 ","http://cdn1.seriadata.net/video/5bEXzuTpGJAGctHNAsC1BA/1/9/1977/1/45.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 46 ","http://cdn1.seriadata.net/video/DhY2iLLHa4JVslcW5yANTA/1/9/1977/1/46.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 47 ","http://cdn1.seriadata.net/video/kVMe3AsGIZoLHRx_8V9Htg/1/9/1977/1/47.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 48 ","http://cdn1.seriadata.net/video/5KWXJ-oUV0so_XcxtQletQ/1/9/1977/1/48.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 49 ","http://cdn1.seriadata.net/video/sPFcIb6OhQWPRVR34lY24g/1/9/1977/1/49.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 50 ","http://cdn1.seriadata.net/video/apyA_NbevD065PbAb3xIMw/1/9/1977/1/50.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 51 ","http://cdn1.seriadata.net/video/dfXMnpqtjWou4YRekBrbGQ/1/9/1977/1/51.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 52 ","http://cdn1.seriadata.net/video/Rs6TvdF-Fa4LX-adZQzKNg/1/9/1977/1/52.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 53 ","http://cdn1.seriadata.net/video/RRzJahU0LOtI9l6hmcPpuQ/1/9/1977/1/53.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 54 ","http://cdn1.seriadata.net/video/g2BOzwwOEuW8eHIbyq4bMg/1/9/1977/1/54.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 55 ","http://cdn1.seriadata.net/video/uReJt4ffrDkPdUDc4ajrxg/1/9/1977/1/55.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   addDir("Megre 56 ","http://cdn1.seriadata.net/video/LWXMJeXdIz8afGExLOhfCg/1/9/1977/1/56.mp4", "playPure","http://cdn0.seriadata.net/4/0/4000.jpg")
   xbmcplugin.endOfDirectory(pluginhandle)


def listShow(url):


        content="http://www.armlook.com/program/allEpisodes/"+url+"/limit/50/offset/0";
        print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        print content
        req = urllib2.Request(content)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:22.0) Gecko/20100101 Firefox/22.0')
        response = urllib2.urlopen(req)

        jsonObj=json.load(response)
        response.close()
        #print jsonObj

        for epi in jsonObj:
          print epi
          addDir(epi['d']+"."+epi['m']+")"+epi['e']+" "+epi['p'],epi['url'], 'playVideo',baseUrl+epi['bgb'])
        #addDir(translation(30007), baseUrl+"/ZDFmediathek/senderstartseite/sst2/1209114", 'listVideos', "")
        #addDir(translation(30006), baseUrl+"/ZDFmediathek/kanaluebersicht/aktuellste/857392", 'listVideos', "")
        #addDir(translation(30005), baseUrl+"/ZDFmediathek/senderstartseite/sst0/1209122", 'listVideos', "")
        #addDir(translation(30008), baseUrl+"/ZDFmediathek/senderstartseite/sst1/1209122", 'listShows', "")
        #addDir(translation(30007), baseUrl+"/ZDFmediathek/senderstartseite/sst2/1209122", 'listVideos', "")
        xbmcplugin.endOfDirectory(pluginhandle)




def listChannel(url):


        url="http://www.armlook.com/channel/allPrograms/"+url+"/limit/40/offset/0";
        
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:22.0) Gecko/20100101 Firefox/22.0')
        response = urllib2.urlopen(req)

        jsonObj=json.load(response)
        response.close()
        #print jsonObj
        
        for show in jsonObj:
          print show 
          url=show['id']
          addDir(show['p'], url, 'listShow', "")
        #addDir(translation(30007), baseUrl+"/ZDFmediathek/senderstartseite/sst2/1209114", 'listVideos', "")
        #addDir(translation(30006), baseUrl+"/ZDFmediathek/kanaluebersicht/aktuellste/857392", 'listVideos', "")
        #addDir(translation(30005), baseUrl+"/ZDFmediathek/senderstartseite/sst0/1209122", 'listVideos', "")
        #addDir(translation(30008), baseUrl+"/ZDFmediathek/senderstartseite/sst1/1209122", 'listShows', "")
        #addDir(translation(30007), baseUrl+"/ZDFmediathek/senderstartseite/sst2/1209122", 'listVideos', "")
        xbmcplugin.endOfDirectory(pluginhandle)



def listChannelLive(url):


        url="http://gisher.org/services/armtv.html?tv="+url+"";
       # req = urllib2.Request(url)
       # req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:22.0) Gecko/20100101 Firefox/22.0')
        #response = urllib2.urlopen(req)
        #print response  
        content="http://www.armlook.com/episode/armenia-tv/full-house-3/episode-7-anons/4747"
         
        contik=getUrl(content)
        print contik
        response = requests.get(content)
        print (response.status_code)
        print (response.content)
        url="https://lola.gisher.org/tv/armeniatv.m3u8?st=88XsRblriknTuEvCKmcjLA&e=1489107793"
           
        addDir("Play Stream"+url, url, 'playPure', "")
        xbmcplugin.endOfDirectory(pluginhandle)


def listVideos(url):



    content="http://www.armlook.com/episode/armenia-tv/full-house-3/episode-7-anons/4747"

    req = urllib2.Request(content)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:22.0) Gecko/20100101 Firefox/22.0')
    response = urllib2.urlopen(req)

    jsonObj=json.read(response)
    response.close()


    #print jsonObj



    addLink(title, url, 'playVideo', thumb, length)


    xbmcplugin.endOfDirectory(pluginhandle)
    if forceViewMode:
        xbmc.executebuiltin('Container.SetViewMode('+viewMode+')')


def play100sec():
     playback_url = 'plugin://plugin.video.dailymotion_com/?mode=playVideo&url=x3b4rij'
     xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(playback_url)




def get_yt_video_id(url):
    """Returns Video_ID extracting from the given url of Youtube
    
    Examples of URLs:
      Valid:
        'http://youtu.be/_lOT2p_FCvA',
        'www.youtube.com/watch?v=_lOT2p_FCvA&feature=feedu',
        'http://www.youtube.com/embed/_lOT2p_FCvA',
        'http://www.youtube.com/v/_lOT2p_FCvA?version=3&amp;hl=en_US',
        'https://www.youtube.com/watch?v=rTHlyTphWP0&index=6&list=PLjeDyYvG6-40qawYNR4juzvSOg-ezZ2a6',
        'youtube.com/watch?v=_lOT2p_FCvA',
      
      Invalid:
        'youtu.be/watch?v=_lOT2p_FCvA',
    """

    from urlparse import urlparse, parse_qs

    if url.startswith(('youtu', 'www')):
        url = 'http://' + url
        
    query = urlparse(url)
    
    if 'youtube' in query.hostname:
        if query.path == '/watch':
            return parse_qs(query.query)['v'][0]
        elif query.path.startswith(('/embed/', '/v/')):
            return query.path.split('/')[2]
    elif 'youtu.be' in query.hostname:
        return query.path[1:]
    else:
        raise ValueError


def playPure(url):


       li = xbmcgui.ListItem(label="Armlook Stream", iconImage="http://www.armlook.com/images/logo.png", path="zzzz")
       li.setInfo(type='Video', infoLabels={ "Title": "Armlook Video" })
       li.setProperty('IsPlayable', 'true')
       xbmc.Player().play(item=url, listitem=li)


def playVideo(url):


    url=baseUrl+url
    print url
    content = getUrl(url)
   # print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"+content
    match = re.compile('"mp4": "(.+?)"', re.DOTALL).findall(content)
    #print match[0]
    #listitem = xbmcgui.ListItem(path=match[0][0] + match[0][1] + " swfUrl=http://www.arte.tv/flash/mediaplayer/mediaplayer.swf live=1 swfVfy=1")
    #xbmcplugin.setResolvedUrl(pluginhandle, True, listitem)
    #listitem = xbmcgui.ListItem(match[1])
    

    print match
    if len(match)!=0:
        
       li = xbmcgui.ListItem(label="Armlook Stream", iconImage="http://www.armlook.com/images/logo.png", path=match[0])
       li.setInfo(type='Video', infoLabels={ "Title": "Armlook Video" })
       li.setProperty('IsPlayable', 'true')
       xbmc.Player().play(item=match[1], listitem=li)
    else:
            print"mta list stugman"
            match3 = re.compile('<iframe width="(.+?)" height="(.+?)" src="//www.youtube.com/embed/(.+?)"', re.DOTALL).findall(content)
            print match3[0][2]      
            url2="https://www.youtube.com/embed/"+match3[0][2]     
            content2 = getUrl(url2)
            print content2
            match4 = re.compile('<link rel="canonical" href="http://www.youtube.com/watch\?v=(.+?)"', re.DOTALL).findall(content2)
            print match4
            video_id=match4[0]
            
            #video_id = match4[0]
            print "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuh"+video_id
            playback_url = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % video_id
             #item = xbmcgui.ListItem(path=playback_url)
             #xbmcplugin.setResolvedUrl(pluginhandle, True, item)
            xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(playback_url)

                 


def playLiveVideo(url):

    #PRINT "ayoooooooooooooooo"
    #url=url
    print url
    #content = getUrl(url)
    #print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"+content
    #match = re.compile('file: "(.+?)",stretching:"', re.DOTALL).findall(content)
    #print match[0]
    #listitem = xbmcgui.ListItem(path=match[0][0] + match[0][1] + " swfUrl=http://www.arte.tv/flash/mediaplayer/mediaplayer.swf live=1 swfVfy=1")
    #xbmcplugin.setResolvedUrl(pluginhandle, True, listitem)
    #listitem = xbmcgui.ListItem(match[1])
    

   # print match
   # if len(match)!=0:
        
#       li = xbmcgui.ListItem(label="Armlook Stream", iconImage="http://www.armlook.com/images/logo.png", path=match[0])
 #      li.setInfo(type='Video', infoLabels={ "Title": "Armlook Video" })
  #     li.setProperty('IsPlayable', 'true')





def playVideo2(id):
    content = getUrl(baseUrl+"/ZDFmediathek/xmlservice/web/beitragsDetails?id="+id)
    match0 = re.compile('<formitaet basetype="h264_aac_mp4_rtmp_zdfmeta_http" isDownload="false">.+?<quality>hd</quality>.+?<url>(.+?)</url>', re.DOTALL).findall(content)
    match1 = re.compile('<formitaet basetype="h264_aac_mp4_rtmp_zdfmeta_http" isDownload="false">.+?<quality>veryhigh</quality>.+?<url>(.+?)</url>', re.DOTALL).findall(content)
    match2 = re.compile('<formitaet basetype="h264_aac_mp4_rtmp_zdfmeta_http" isDownload="false">.+?<quality>high</quality>.+?<url>(.+?)</url>', re.DOTALL).findall(content)
    match3 = re.compile('<formitaet basetype="h264_aac_ts_http_m3u8_http" isDownload="false">.+?<quality>high</quality>.+?<url>(.+?)</url>', re.DOTALL).findall(content)
    matchUT = re.compile('<caption>.+?<url>(.+?)</url>', re.DOTALL).findall(content)
    url = ""
    if content.find("<type>livevideo</type>") >= 0:
        if match3:
            url = match3[0]
    elif content.find("<type>video</type>") >= 0:
        if match0:
            url = match0[0]
        elif match1:
            url = match1[0]
        elif match2:
            url = match2[1]
        if "http://" in url:
            content = getUrl(url)
            match = re.compile('<default-stream-url>(.+?)</default-stream-url>', re.DOTALL).findall(content)
            url = match[0]
    listitem = xbmcgui.ListItem(path=url)
    xbmcplugin.setResolvedUrl(pluginhandle, True, listitem)
    if showSubtitles and matchUT:
        setSubtitle(matchUT[0])


def setSubtitle(url):
    if os.path.exists(subFile):
        os.remove(subFile)
    try:
        content = getUrl(url)
    except:
        content = ""
    if content:
        matchLine = re.compile('<p begin="(.+?)" end="(.+?)".+?>(.+?)</p>', re.DOTALL).findall(content)
        fh = open(subFile, 'a')
        count = 1
        for begin, end, line in matchLine:
            begin = float(begin)
            beginS = str(round(begin%60, 1)).replace(".",",")
            if len(beginS.split(",")[0])==1:
                beginS = "0"+beginS
            beginM = str(int(begin)/60)
            if len(beginM)==1:
                beginM = "0"+beginM
            beginH = str(int(begin)/60/60)
            if len(beginH)==1:
                beginH = "0"+beginH
            begin = beginH+":"+beginM+":"+beginS
            end = float(end)
            endS = str(round(end%60, 1)).replace(".",",")
            if len(endS.split(",")[0])==1:
                endS = "0"+endS
            endM = str(int(end)/60)
            if len(endM)==1:
                endM = "0"+endM
            endH = str(int(end)/60/60)
            if len(endH)==1:
                endH = "0"+endH
            end = endH+":"+endM+":"+endS
            match = re.compile('<span(.+?)>', re.DOTALL).findall(line)
            for span in match:
                line = line.replace("<span"+span+">","")
            line = line.replace("<br />","\n").replace("</span>","").strip()
            fh.write(str(count)+"\n"+begin+" --> "+end+"\n"+cleanTitle(line)+"\n\n")
            count+=1
        fh.close()
        xbmc.sleep(1000)
        xbmc.Player().setSubtitles(subFile)


def queueVideo(url, name):
    playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    listitem = xbmcgui.ListItem(name)
    playlist.add(url, listitem)


def search():
    keyboard = xbmc.Keyboard('', translation(30002))
    keyboard.doModal()
    if keyboard.isConfirmed() and keyboard.getText():
        search_string = keyboard.getText().replace(" ", "+")
        listVideos(baseUrl+"/ZDFmediathek/suche?sucheText="+search_string)


def listAZ():
    addDir("ABC", baseUrl+"/ZDFmediathek/hauptnavigation/sendung-a-bis-z/saz0", 'listShows', "")
    addDir("DEF", baseUrl+"/ZDFmediathek/hauptnavigation/sendung-a-bis-z/saz1", 'listShows', "")
    addDir("GHI", baseUrl+"/ZDFmediathek/hauptnavigation/sendung-a-bis-z/saz2", 'listShows', "")
    addDir("JKL", baseUrl+"/ZDFmediathek/hauptnavigation/sendung-a-bis-z/saz3", 'listShows', "")
    addDir("MNO", baseUrl+"/ZDFmediathek/hauptnavigation/sendung-a-bis-z/saz4", 'listShows', "")
    addDir("PQRS", baseUrl+"/ZDFmediathek/hauptnavigation/sendung-a-bis-z/saz5", 'listShows', "")
    addDir("TUV", baseUrl+"/ZDFmediathek/hauptnavigation/sendung-a-bis-z/saz6", 'listShows', "")
    addDir("WXYZ", baseUrl+"/ZDFmediathek/hauptnavigation/sendung-a-bis-z/saz7", 'listShows', "")
    addDir("0-9", baseUrl+"/ZDFmediathek/hauptnavigation/sendung-a-bis-z/saz8", 'listShows', "")
    xbmcplugin.endOfDirectory(pluginhandle)


def cleanTitle(title):
    title = title.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&").replace("&#039;", "\\").replace("&quot;", "\"").replace("&szlig;", "ß").replace("&ndash;", "-")
    title = title.replace("&Auml;", "Ä").replace("&Uuml;", "Ü").replace("&Ouml;", "Ö").replace("&auml;", "ä").replace("&uuml;", "ü").replace("&ouml;", "ö").replace("&eacute;", "é").replace("&egrave;", "è")
    title = title.replace("&#x00c4","Ä").replace("&#x00e4","ä").replace("&#x00d6","Ö").replace("&#x00f6","ö").replace("&#x00dc","Ü").replace("&#x00fc","ü").replace("&#x00df","ß").strip()
    title = title.replace("&apos;","'").strip()
    return title


def favs(param):
    mode = param[param.find("###MODE###=")+11:]
    mode = mode[:mode.find("###")]
    channelEntry = param[param.find("###TITLE###="):]
    if mode == "ADD":
        if os.path.exists(channelFavsFile):
            fh = open(channelFavsFile, 'r')
            content = fh.read()
            fh.close()
            if content.find(channelEntry) == -1:
                fh = open(channelFavsFile, 'a')
                fh.write(channelEntry+"\n")
                fh.close()
        else:
            fh = open(channelFavsFile, 'a')
            fh.write(channelEntry+"\n")
            fh.close()
    elif mode == "REMOVE":
        refresh = param[param.find("###REFRESH###=")+14:]
        refresh = refresh[:refresh.find("#")]
        fh = open(channelFavsFile, 'r')
        content = fh.read()
        fh.close()
        entry = content[content.find(channelEntry):]
        fh = open(channelFavsFile, 'w')
        fh.write(content.replace(channelEntry+"\n", ""))
        fh.close()
        if refresh == "TRUE":
            xbmc.executebuiltin("Container.Refresh")



def getUrl(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:22.0) Gecko/20100101 Firefox/22.0')
    response = urllib2.urlopen(req)
    link = response.read()
    response.close()
    


    return link


def parameters_string_to_dict(parameters):
    paramDict = {}
    if parameters:
        paramPairs = parameters[1:].split("&")
        for paramsPair in paramPairs:
            paramSplits = paramsPair.split('=')
            if (len(paramSplits)) == 2:
                paramDict[paramSplits[0]] = paramSplits[1]
    return paramDict


def addLink(name, url, mode, iconimage, duration=""):
    u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": name, "Duration": duration})
    liz.setProperty('IsPlayable', 'true')
    if useThumbAsFanart:
        if not iconimage:
            iconimage = defaultBackground
        liz.setProperty("fanart_image", iconimage)
    else:
        liz.setProperty("fanart_image", defaultBackground)
    liz.addContextMenuItems([(translation(30012), 'RunPlugin(plugin://'+addonID+'/?mode=queueVideo&url='+urllib.quote_plus(u)+'&name='+urllib.quote_plus(name)+')',)])
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz)
    return ok


def addShowLink(name, url, mode, iconimage, duration=""):
    u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": name, "Duration": duration})
    liz.setProperty('IsPlayable', 'true')
    if useThumbAsFanart:
        if not iconimage:
            iconimage = defaultBackground
        liz.setProperty("fanart_image", iconimage)
    else:
        liz.setProperty("fanart_image", defaultBackground)
    playListInfos = "###MODE###=ADD###TITLE###="+name+"###URL###="+urllib.quote_plus(url)+"###THUMB###="+iconimage+"###END###"
    liz.addContextMenuItems([(translation(30028), 'RunPlugin(plugin://'+addonID+'/?mode=favs&url='+urllib.quote_plus(playListInfos)+')',)])
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz)
    return ok


def addShowFavLink(name, url, mode, iconimage, duration=""):
    u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": name, "Duration": duration})
    liz.setProperty('IsPlayable', 'true')
    if useThumbAsFanart:
        if not iconimage:
            iconimage = defaultBackground
        liz.setProperty("fanart_image", iconimage)
    else:
        liz.setProperty("fanart_image", defaultBackground)
    playListInfos = "###MODE###=REMOVE###REFRESH###=TRUE###TITLE###="+name+"###URL###="+urllib.quote_plus(url)+"###THUMB###="+iconimage+"###END###"
    liz.addContextMenuItems([(translation(30029), 'RunPlugin(plugin://'+addonID+'/?mode=favs&url='+urllib.quote_plus(playListInfos)+')',)])
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz)
    return ok


def addDir(name, url, mode, iconimage):
    u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": name})
    liz.setProperty("fanart_image", defaultBackground)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
    return ok


def addTopicDir(name, url, mode, iconimage):
    u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": name})
    liz.setProperty("fanart_image", defaultBackground)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
    return ok


def addShowDir(name, url, mode, iconimage):
    u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": name})
    if useThumbAsFanart:
        if not iconimage:
            iconimage = defaultBackground
        liz.setProperty("fanart_image", iconimage)
    else:
        liz.setProperty("fanart_image", defaultBackground)
    playListInfos = "###MODE###=ADD###TITLE###="+name+"###URL###="+urllib.quote_plus(url)+"###THUMB###="+iconimage+"###END###"
    liz.addContextMenuItems([(translation(30028), 'RunPlugin(plugin://'+addonID+'/?mode=favs&url='+urllib.quote_plus(playListInfos)+')',)])
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
    return ok


def addShowFavDir(name, url, mode, iconimage):
    u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": name})
    if useThumbAsFanart:
        if not iconimage:
            iconimage = defaultBackground
        liz.setProperty("fanart_image", iconimage)
    else:
        liz.setProperty("fanart_image", defaultBackground)
    playListInfos = "###MODE###=REMOVE###REFRESH###=TRUE###TITLE###="+name+"###URL###="+urllib.quote_plus(url)+"###THUMB###="+iconimage+"###END###"
    liz.addContextMenuItems([(translation(30029), 'RunPlugin(plugin://'+addonID+'/?mode=favs&url='+urllib.quote_plus(playListInfos)+')',)])
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
    return ok

params = parameters_string_to_dict(sys.argv[2])
mode = urllib.unquote_plus(params.get('mode', ''))
url = urllib.unquote_plus(params.get('url', ''))
name = urllib.unquote_plus(params.get('name', ''))

if mode == 'listChannel':
    listChannel(url)
elif mode == 'listChannelLive':
    listChannelLive(url)
elif mode == 'listVideos':
    listVideos(url)
elif mode == 'listShow':
    listShow(url)
elif mode == 'listThemen':
    listShows(url, False)
elif mode == 'listVerpasst':
    listVerpasst(url)
elif mode == 'playVideo':
    playVideo(url)
elif mode == 'playLiveVideo':
    playLiveVideo(url)
elif mode == 'playPure':
   playPure(url)
elif mode == 'play100sec':
    play100sec()
elif mode == 'queueVideo':
    queueVideo(url, name)
elif mode == 'search':
    search()
elif mode == 'listAZ':
    listAZ()
elif mode == 'favs':
    favs(url)
elif mode == 'listShowsFavs':
    listShowsFavs()
else:
    index()

