import requests
import urllib.parse
import os

#Util class for twitch-dl

#Fancy!
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Declaring the headers just one time
def getHeaders():
    headers = {
        #Seems that this Client-ID is specific for the not-logged user?
    	'Client-ID': 'kimne78kx3ncx6brgo4mv6wki5h1ko'
	}
    return headers

#Returns a JSON object for printing and naming the output file
def getVideoInfo(video_id):
    response = requests.get('https://api.twitch.tv/helix/videos?id=' + video_id, headers=getHeaders())
    if (response.status_code != 200):
        return quit(bcolors.FAIL + "Error! Video id or url not found" + bcolors.ENDC)
    #Creating the object
    return {"username": response.json()['data'][0]['user_name'],
            "title": response.json()['data'][0]['title']}

#Returns a JSON object for token and sig key, used to create the playlist url
def getAccessToken(video_id):
    #unique_id can be anything 16 char long. Using this instead of random
    cookies = {'unique_id': '123456789012345'}
    response = requests.get('https://api.twitch.tv/api/vods/' + video_id + '/access_token', headers=getHeaders(), cookies=cookies)
    if (response.status_code != 200):
        return quit(bcolors.FAIL + "Error! Can't get an access token for this video" + bcolors.ENDC)
    return {"token": response.json()['token'], "sig": response.json()['sig']}

#Formatting the download url
def getDownloadUrl(video_id):
    video_tokens = getAccessToken(video_id)
    download_url = "https://usher.ttvnw.net/vod/" + video_id + ".m3u8" + \
					"?allow_source=true" + \
					"&p=5760802" + \
					"&player_backend=mediaplayer" + \
					"&playlist_include_framerate=true" + \
					"&reassignments_supported=true" + \
					"&sig=" + video_tokens['sig'] + \
					"&token=" + urllib.parse.quote(video_tokens['token']) + \
					"&cdm=wv"
    return download_url

def downloadVideo(video_id):
    video_infos = getVideoInfo(video_id)
    video_title = "'" + video_infos['username'] + " - " + video_infos['title'] + "'"
    command = "ffmpeg -i '"+ getDownloadUrl(video_id) +"' -v quiet -stats -acodec copy -vcodec copy " + str(video_title) + ".mp4"
    os.system(command)
