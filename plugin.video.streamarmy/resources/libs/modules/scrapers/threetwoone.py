import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,datetime,hashlibimport base64import HTMLParserimport osfrom resources.libs.modules import satoolsaddon_id        = 'plugin.video.streamarmy'AddonTitle      = "[COLOR red][B]STREAM ARMY[/B][/COLOR]"fanart          = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))fanarts         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))icon            = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))dialog          = xbmcgui.Dialog()dp              = xbmcgui.DialogProgress()def SCRAPE_321MOVIES_CONTENT(url):    issearch = 0    try:        url,term = url.split("|SPLIT|")        issearch = 1    except: pass        namelist     = []    urllist      = []    iconlist     = []    fanartlist   = []    combinedlist = []        url_check = url    link = satools.open_url(url)    match = re.compile('<div class="image">(.+?)</p>').findall(link)    for links in match:        url1 = re.compile('<a href="(.+?)"').findall(links)[0]        icon = re.compile('<img src="(.+?)"').findall(links)[0]        title = re.compile('alt="(.+?)"').findall(links)[0].replace('Watch ', '').replace('For Free', '')        rating = re.compile('<span class="rating">(.+?)</span>').findall(links)[0]        namelist.append(title)        urllist.append(url1)        iconlist.append(icon)        combinedlist = list(zip(namelist,urllist,iconlist))    for title,url1,icon in combinedlist:            if issearch == 0:             satools.addDir("[COLOR silver]" + title + "  " + "[COLOR yellow]" + rating + "[/COLOR]",url1,35,icon,fanart,'')        else:            if ' ' in term:                notfound = 0                checks = term.split(" ")                for check in checks:                    if not check.lower() in title.lower():                        notfound = 1                if notfound == 0:                     satools.addDir("[COLOR silver]" + title + "  " + "[COLOR yellow]" + rating + "[/COLOR]",url1,35,icon,fanart,'')            else:                if term.lower() in title.lower():                     satools.addDir("[COLOR silver]" + title + "  " + "[COLOR yellow]" + rating + "[/COLOR]",url1,35,icon,fanart,'')                     def SCRAPE_321MOVIES_LINKS(url):    link = satools.open_url(url)    match = re.compile('class="play-box-iframe fixidtab">(.+?)</div>').findall(link)    satools.addLink("[COLOR red]First Link Is A Trailer[/COLOR]",'url','2',icon,fanart,'')    for links in match:        url = re.compile('src="(.+?)"').findall(links)[0]        if 'youtube' in url:            title = 'Trailer'        else:            title = 'Play Movie'                satools.addLink("[COLOR silver]" + title + "[/COLOR]",url,2,icon,fanart,'')