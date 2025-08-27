from pypresence import Presence
import time
import sys

DISCORD_CLIENT_ID = ""  # Replace with your actual Discord App ID

rpc = None
current_song = None

def init_rpc():
    global rpc
    if not DISCORD_CLIENT_ID:
        print("[ERROR] No Discord Client ID set in rpc_handler.py", file=sys.stderr)
        return False
    try:
        rpc = Presence(DISCORD_CLIENT_ID)
        rpc.connect()
        print("[INFO] Connected to Discord RPC")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to connect to Discord RPC: {e}", file=sys.stderr)
        rpc = None
        return False

def update_presence(title, artist):
    global current_song, rpc

    if rpc is None and not init_rpc():
        return  # Skip if RPC can't connect

    song_key = f"{title}-{artist}"
    if song_key == current_song:
        return  # Skip updating if same song

    current_song = song_key

    try:
        rpc.clear()
        rpc.update(
            details=f"Song: {title}",
            state=f"Artist: {artist}",
            large_image="music",
            large_text="Playing YouTube Music through phone",
            start=time.time()
        )
        print(f"[INFO] Updated presence: {title} - {artist}")
    except Exception as e:
        print(f"[ERROR] Failed to update presence: {e}", file=sys.stderr)
