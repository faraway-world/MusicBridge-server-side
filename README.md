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
```

### Configuration
1. Open rpc_handler.py and set your Discord App Client ID:
DISCORD_CLIENT_ID = "YOUR_DISCORD_APP_ID"
You can create a new Discord app here: Discord Developer Portal.

2. (Optional) Replace the large_image key with your own uploaded asset in the Developer Portal.

### Running
Start the server:
./run_rpc.sh

Your phone app can now send JSON POST requests like:
{
  "title": "Song Name",
  "artist": "Artist Name"
}
to http://YOUR_PC_IP:5000/update.

### Example
curl -X POST http://127.0.0.1:5000/update \
  -H "Content-Type: application/json" \
  -d '{"title": "Luv(sic)", "artist": "Nujabes"}'

Discord will then show:

Song: Luv(sic)
Artist: Nujabes

### Notes
Tested with YouTube Music on Android.
Works only while Discord desktop app is running.
If using linux, use .deb version or the version from the AUR if Arch. Don't use Flatpak

### This requires a companion Android app (not included in this repo)
