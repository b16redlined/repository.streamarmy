import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,datetime,hashlib,timeimport base64import HTMLParserimport osfrom resources.libs.modules import satoolsaddon_id        = 'plugin.video.streamarmy'AddonTitle      = "[COLOR red][B]STREAM ARMY[/B][/COLOR]"fanart          = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))fanarts         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))icon            = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))dialog          = xbmcgui.Dialog()dp              = xbmcgui.DialogProgress()def SCRAPE_WEBCAM_CATS():     url = 'https://www.skylinewebcams.com/en/webcam.html'    link = satools.open_url(url)    match = re.compile('<i class="icon-angle-down">(.+?)<i class="icon-angle-down">').findall(link)[0].replace('<strong>', '').replace('&nbsp;', '')    grab = re.compile ('<a href="(.+?)" class="menu-item">(.+?)<span class="ccnt">(.+?)</span>').findall(match)    for link,title,number in grab:        if 'http' not in link:            url = 'https://www.skylinewebcams.com' + link            icon = 'http://i.imgur.com/zz73Uks.png'            satools.addDir("[COLOR silver]" + title + "[/COLOR]",url,47,icon,fanarts,'')            def SCRAPE_WEBCAM_LINKS(url):    link = satools.open_url(url)    match = re.compile('<li class="webcam">(.+?)</span>').findall(link)    for links in match:        try:            img = re.compile ('data-original="(.+?)"').findall(links)[0]            if not 'http' in img:                icon = 'http:' + img                title = re.compile ('alt="(.+?)"').findall(links)[0]                wronglink = re.compile ('<a href="(.+?)">').findall(links)[0]                if not 'http:' in wronglink:                    url = 'https://www.skylinewebcams.com' + wronglink                    satools.addDir("[COLOR silver]" + title + "[/COLOR]",url,48,icon,fanarts,'')        except: pass    def SCRAPE_WEBCAM_PLAYLINKS(name,url,iconimage):    link = satools.open_url(url)    try:        dp.create(AddonTitle,"[COLOR yellow]Generating link...[/COLOR]",'[COLOR red]Please wait...[/COLOR]','')           dp.update(0)        time.sleep(1)        match = re.compile('<script type="text/javascript">(.+?)</script>').findall(link)[1]        url = re.compile ("url:'(.+?)'}").findall(match)[0]        liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)        xbmc.Player ().play(url, liz, False)    except:pass    quit(0)