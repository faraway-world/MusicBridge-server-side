# MusicBridge Discord RPC

A simple bridge that sends music info from your **Android phone** (via a companion Kotlin app) to a **Flask server** on your PC, and updates your **Discord Rich Presence** with the currently playing track.

## Features
- Shows current song and artist on Discord.
- Works with YouTube Music (or any player that pushes media notifications).
- Lightweight Flask server backend.
- Uses [pypresence](https://qwertyquerty.github.io/pypresence/html/index.html) for Discord RPC.

## How it works
1. The Kotlin app on your phone reads notification data (title, artist) from the music player.
2. It sends this data via HTTP POST to the Flask server (`server.py`) on your PC.
3. The server calls `rpc_handler.py` to update your Discord Rich Presence in real-time.

## Setup
### Prerequisites
- Python 3.10+  
- Discord desktop app running  

### Installation
```bash
git clone https://github.com/YOUR_USERNAME/musicbridge-discord-rpc.git
cd musicbridge-discord-rpc
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
