import json 
from rich.prompt import Prompt

class StreamDL:
    def __init__(self, url, name, path, format, color, lib):
        self.url = url
        self.name = name
        self.path = path
        self.format = format
        self.color = color
        self.lib = lib



def siteProcess(stropt):
    global config
    global url

    url = stropt

    with open('./Config/config.json', 'r') as data:
        config = json.load(data)

    verifySite()



def siteBuild():

    from ytdlpProcess import ytdlpProcess, scYtdlpProcess, ytdlpDefault
    from spotdlProcess import spotdlProcess

    siteCategory = config["sites-data"][f"{siteName}"]["category"]
    siteColor = config["sites-data"][f"{siteName}"]["color"]
    siteLib = config["sites-data"][f"{siteName}"]["lib"]

    if (siteCategory == "default"):
        sitePath = config["path"]["default"]
        request = StreamDL(url, siteName, sitePath, "wyla?", siteColor, siteLib)
        if (request.lib == "ytdlp"):
            ytdlpDefault(request)

    if (siteCategory == "video"):
        sitePath = config["path"]["video"]
        request = StreamDL(url, siteName, sitePath, "mp4", siteColor, siteLib)
        if (request.lib == "ytdlp"):
            ytdlpProcess(request)
        if (request.lib == "ytdlp-sc"):
            scYtdlpProcess(request)

    if (siteCategory == "music"):
        sitePath = config["path"]["music"]
        request = StreamDL(url, siteName, sitePath, "mp3", siteColor, siteLib)
        if (request.lib == "ytdlp"):
            ytdlpProcess(request)
        if (request.lib == "ytdlp-sc"):
            scYtdlpProcess(request)
        if (request.lib == "spotdl"):
            spotdlProcess(request)


    if (siteCategory == "social"):
        sitePath = config["path"]["social"]
        request = StreamDL(url, siteName, sitePath, "mp4", siteColor, siteLib)
        if (request.lib == "ytdlp"):
            ytdlpProcess(request)



def verifySite(): 

        knownSites = config['registred-sites']

        if (getSiteName(default=False) in knownSites):
            siteBuild()
        
        else: 
            uknUrlChoice = Prompt.ask(f"\n[red][[/red][bold white]![/bold white][red]][/red] Site URL not registred, try to proceed? (y/n)")

            if (uknUrlChoice in ["y", "yes"]):
                getSiteName(default=True)

            else:
                from StreamingDL import main_menu  
                main_menu()



def getSiteName(default):
    global url
    global siteName

    if (not default):

        import urllib.parse

        parsed_url = urllib.parse.urlsplit(url)
        siteName = parsed_url.netloc

        siteName = siteName.replace("www.", "")
        siteName = siteName.replace(".com", "")
        siteName = siteName.replace(".tv", "")
        siteName = siteName.replace(".fr", "")

        if ("." in siteName): 
            siteName = siteName.replace(".", "") # ex : https://youtu.be/---------
        
        siteName = siteName.split(':')[0]

        # Exception #    
        if (siteName == "soundcloud"):
            url = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path
            url = url.replace("popular-", "") # popular-tracks url cause DL-Error

        if "spotify" in siteName:
            url = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path
            siteName = "spotify" # open.spotify.com
        # --------- #

        return siteName

    else:
        siteName = "default"
        siteBuild()