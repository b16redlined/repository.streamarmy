import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,datetime,hashlibimport base64import HTMLParserimport osfrom resources.libs.modules import satoolsaddon_id        = 'plugin.video.streamarmy'AddonTitle      = "[COLOR red][B]STREAM ARMY[/B][/COLOR]"fanart          = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))fanarts         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))icon            = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))dialog          = xbmcgui.Dialog()dp              = xbmcgui.DialogProgress()def SCRAPE_IPTV_CONTENT():    url = 'http://iptvsatlinks.com/category/uk-channels/'    link = satools.open_url(url)    match = re.compile('<figure class="mh-loop-thumb">(.+?)</figure>').findall(link)    icon1 = 'http://i.imgur.com/dSlI9s8.png'    satools.addDir("[COLOR red]" + "These are Random Playlists, If One Doesn't Work, Try Another" + "[/COLOR]",'url','95',icon1,fanarts,'')    for links in match:        url = re.compile ('<a href="(.+?)">').findall(links)[0]        icon = re.compile ('src="(.+?)"').findall(links)[0]        satools.addDir("[COLOR silver]" + 'Random List' + "[/COLOR]",url,22,icon,fanarts,'')                def SCRAPE_IPTV_PLAY(url):    link = satools.open_url(url)    match = re.compile('EXTINF:(.+?)#').findall(link)    for links in match:        try:            chan = re.compile (',(.+?)http').findall(links)[0]            links = re.compile ('http(.+?).ts').findall(links)[0]            if 'http' not in links:                link2 = 'http' + links + '.ts'                satools.addLink("[COLOR silver]" + chan + "[/COLOR]",link2,2,icon,fanarts,'')        except: pass