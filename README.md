# 📹 Twitch Downloader
### A basic CLI tool for downloading videos from twitch.tv
It is still in a very alpha stage, a complete description and features coming soon.
It is written with python3 and uses ffmpeg for downloading and encoding, also no login required.

#### How to use:
Install dependencies: <code>pip install -r requirements.txt</code>

Run twitch-dl: <code>python3 twitch-dl.py [one or multiple video-id or twitch video urls]</code>

#### TODO:
- Support for multiple quality (default: best quality)
- ~~Support for multiple links/videos~~ (commit [63e8fa2](
https://github.com/0xf77/twitch-dl/commit/63e8fa228bc0a7cb92f0d0dd597683b1bd2c7eef))
- Support for pausing/resuming
- ~~Support for custom filenames (default: out.mp4)~~ (commit [39bbf02](https://github.com/0xf77/twitch-dl/commit/39bbf023a4e68283d9a14d7783370e5e9111a55e))
- ~~Rework the code (It is mostly a dirty hack)~~ (commit [e32e72d](https://github.com/0xf77/twitch-dl/commit/e32e72dc6370ab06e0138337e1be246c922a4c89))
