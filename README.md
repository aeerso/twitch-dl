# 📹 Twitch Downloader
### A basic CLI tool for downloading videos from twitch.tv
It is still in a very alpha stage, a complete description and features coming soon.
It is written with python3 and uses ffmpeg for downloading and encoding, also no login required.

#### How to use:
Basic usage: <code>python3 twitch-dl.py [video-id or https://www.twitch.tv/videos/xxxxxx]</code>

#### TODO:
- Support for multiple quality (default: best quality)
- ~~Support for multiple links/videos~~ (commit [63e8fa2](
https://github.com/0xf77/twitch-dl/commit/63e8fa228bc0a7cb92f0d0dd597683b1bd2c7eef))
- Support for pausing/resuming
- Support for custom filenames (default: out.mp4)
- Rework the code (It is mostly a dirty hack)
