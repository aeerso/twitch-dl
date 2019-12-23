import util
import sys
import re

#Arrays for video queue
match = []

print(util.bcolors.WARNING + "\ntwitch-dl ~ https://github.com/0xf77/twitch-dl" + util.bcolors.ENDC + "\n")

if len(sys.argv) < 2:
 	print(util.bcolors.FAIL + "[e] No URL to download, use: https://www.twitch.tv/videos/..." + util.bcolors.ENDC)
 	quit()

for videos in sys.argv:
	if re.findall(r'\d+', videos):
		match.append(re.findall(r'\d+', videos)[0])

print(util.bcolors.WARNING + "It could take some seconds to start the download!" + util.bcolors.ENDC)
for video_id in match:
	print(util.bcolors.OKGREEN + "Downloading: " + util.getVideoInfo(video_id)['title'] + " from " + util.getVideoInfo(video_id)['username'] + util.bcolors.ENDC)
	util.downloadVideo(video_id)

print(util.bcolors.FAIL + "Bye! ❤️" + util.bcolors.ENDC)
