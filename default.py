#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import urlparse
import socket
import sys
import os
import re
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
   addDir("ArmeniaTV", "1", 'listChannel', baseUrl+"/uploads/images/channels/banners/armenia.jpg")
  # addDir("ATV", "25", 'listChannel', baseUrl+"/uploads/images/channels/banners/img_548ea6775a962.jpg")
   addDir("ShantTV", "2", 'listChannel', baseUrl+"/uploads/images/channels/banners/shant-1_1601x600.jpg")
   #addDir("H1", "6", 'listChannel', baseUrl+"/uploads/images/channels/banners/img_524a280b02277.jpg")
   #addDir("Armnews", "4", 'listChannel', baseUrl+"/uploads/images/channels/banners/armnewsbanner.jpg")
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
    content = getUrl(baseUrl+"/ZDFmediathek/100sec")
    match = re.compile('assetID : (.+?),', re.DOTALL).findall(content)
    playVideo(match[0])






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
        
       li = xbmcgui.ListItem(label="Pizdec", iconImage="http://www.armlook.com/images/logo.png", path=match[0])
       li.setInfo(type='Video', infoLabels={ "Title": "pizdec" })
       li.setProperty('IsPlayable', 'true')
       xbmc.Player().play(item=match[1], listitem=li)
    else:
            print"mta list stugman"
            match3 = re.compile('width="853" height="480" src="//(.+?)"', re.DOTALL).findall(content)
            print match3[0]      
            url2="http://"+match3[0]     
            content2 = getUrl(url2)
            print content2
            match4 = re.compile('<link rel="canonical" href="(.+?)"', re.DOTALL).findall(content2)
            video_link=match4[0]

            url_data = urlparse.urlparse(video_link)
            query = urlparse.parse_qs(url_data.query)
            video_id = query["v"][0]

            #video_id = match4[0]
            print "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuh"+video_id
            playback_url = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % video_id
             #item = xbmcgui.ListItem(path=playback_url)
             #xbmcplugin.setResolvedUrl(pluginhandle, True, item)
            xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(playback_url)

                 





#xbmcplugin.setResolvedUrl(pluginhandle, True, listitem)
































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
