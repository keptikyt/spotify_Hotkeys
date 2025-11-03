# 🎧 Global Hotkeys for Spotify Control (API-less)

This is a simple Python script that allows you to control playback, track switching, and volume in **Spotify** (or any media player that supports standard multimedia keys) using global hotkey combinations.

The script uses the `keyboard` and `pynput` libraries to emulate standard media key presses from the operating system, triggered by your custom `Ctrl + Alt + [Key]` combinations.

## ✨ Features

  * **Global Scope:** Hotkeys work regardless of which application window is currently active.
  * **Media Key Emulation:** Control is achieved by simulating standard operating system media keys ($Key.media\_play\_pause$, $Key.media\_next$, $Key.media\_volume\_up$, etc.).
  * **Configurable Delay:** Includes a 1-second delay before sending the command (`COMMAND_DELAY_SECONDS`), which can improve stability.

## 🚀 Setup and Running

### 1\. Prerequisites

The following Python libraries are required for the script to run:

```bash
pip install keyboard pynput
```

### 2\. Running the Script

1.  Save the code as `Spotify_hotkeys.py`.
2.  Run the script from your console:

<!-- end list -->

```bash
python Spotify_hotkeys.py
```

3.  The script will start in the background, listening for the hotkey events.
4.  To stop the script, press **Ctrl + C** in the console window.

## 🎹 Hotkeys

| Action | Hotkey Combination | Function in Code |
| :--- | :--- | :--- |
| **Play / Pause** | `Ctrl` + `Alt` + `Z` | `custom_play_pause()` |
| **Next Track** | `Ctrl` + `Alt` + `E` | `custom_next_track()` |
| **Previous Track** | `Ctrl` + `Alt` + `Q` | `custom_previous_track()` |
## ⚙️ Configuration

You can easily adjust the command delay within the `Spotify_hotkeys.py` file:

```python
# --- SETTINGS ---
# Delay before executing the command (as you requested, 1 second)
COMMAND_DELAY_SECONDS = 1 
```
