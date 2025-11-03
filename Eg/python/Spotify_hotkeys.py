import keyboard
from pynput.keyboard import Key, Controller
import time
import sys

# --- SETTINGS ---
# Delay before executing the command (as requested, 1 second)
COMMAND_DELAY_SECONDS = 1 

# Create a keyboard controller object to simulate key presses
kb_controller = Controller()

def send_media_key(media_key):
    """
    Simulates pressing and releasing a multimedia key.
    
    :param media_key: Key from pynput.keyboard.Key (e.g., Key.media_play_pause)
    """
    print(f"Waiting {COMMAND_DELAY_SECONDS} sec before sending command...")
    time.sleep(COMMAND_DELAY_SECONDS) 
    
    try:
        # Press the key
        kb_controller.press(media_key)
        # Small delay for the OS to process the command
        time.sleep(0.05) 
        # Release the key
        kb_controller.release(media_key)
        print(f"-> SUCCESS: Command sent: {media_key}")
    except Exception as e:
        print(f"!!! ERROR: Failed to send command {media_key}: {e}")

# --- SPOTIFY CONTROL FUNCTIONS (Use your hotkeys) ---

def custom_play_pause():
    """Hotkey: Ctrl + Alt + Z. Toggles Play/Pause."""
    # Key.media_play_pause - standard multimedia Play/Pause key
    send_media_key(Key.media_play_pause)

def custom_next_track():
    """Hotkey: Ctrl + Alt + E. Switches to the next track."""
    # Key.media_next - standard multimedia Next Track key
    send_media_key(Key.media_next)

def custom_previous_track():
    """Hotkey: Ctrl + Alt + Q. Switches to the previous track."""
    # Key.media_previous - standard multimedia Previous Track key
    send_media_key(Key.media_previous)
    
def custom_volume_up():
    """New command: Increases volume."""
    # Key.media_volume_up - standard multimedia Volume Up key
    send_media_key(Key.media_volume_up)
    
def custom_volume_down():
    """New command: Decreases volume."""
    # Key.media_volume_down - standard multimedia Volume Down key
    send_media_key(Key.media_volume_down)

def custom_mute_toggle():
    """New command: Toggles Mute/Unmute."""
    # Key.media_mute - standard multimedia Mute key
    send_media_key(Key.media_mute)

# --- REGISTER GLOBAL HOTKEYS ---

# 1. Play/Pause (Keep your combination)
keyboard.add_hotkey('ctrl+alt+z', custom_play_pause)

# 2. Next Track (Keep your combination)
keyboard.add_hotkey('ctrl+alt+e', custom_next_track)

# 3. Previous Track (Keep your combination)
keyboard.add_hotkey('ctrl+alt+q', custom_previous_track)

# 4. Volume Up (New combination)
keyboard.add_hotkey('ctrl+alt+up', custom_volume_up)

# 5. Volume Down (New combination)
keyboard.add_hotkey('ctrl+alt+down', custom_volume_down)

# 6. Mute/Unmute (New combination)
keyboard.add_hotkey('ctrl+alt+m', custom_mute_toggle)


# --- START PROGRAM ---

print("="*60)
print("--- [Spotify Hotkeys Utility (API-less)] ---".center(60))
print("="*60)
print(f"Command delay: {COMMAND_DELAY_SECONDS} second(s).")
print("\n🔥 Hotkeys (work globally):")
print("-" * 30)
print("1. Play / Pause:         Ctrl + Alt + Z")
print("2. Next Track:           Ctrl + Alt + E")
print("3. Previous Track:       Ctrl + Alt + Q")
print("4. Volume Up:            Ctrl + Alt + UP ARROW")
print("5. Volume Down:          Ctrl + Alt + DOWN ARROW")
print("6. Mute/Unmute:          Ctrl + Alt + M")

print("-" * 30)
print("\nPress Ctrl + C in this console window to stop the program.")

try:
    # Block the program to listen for key events
    keyboard.wait()
except KeyboardInterrupt:
    print("\nProgram stopped by the user.")
    sys.exit(0)
    import keyboard
from pynput.keyboard import Key, Controller
import time
import sys

# --- SETTINGS ---
# Delay before executing the command (as requested, 1 second)
COMMAND_DELAY_SECONDS = 1 

# Create a keyboard controller object to simulate key presses
kb_controller = Controller()

def send_media_key(media_key):
    """
    Simulates pressing and releasing a multimedia key.
    
    :param media_key: Key from pynput.keyboard.Key (e.g., Key.media_play_pause)
    """
    print(f"Waiting {COMMAND_DELAY_SECONDS} sec before sending command...")
    time.sleep(COMMAND_DELAY_SECONDS) 
    
    try:
        # Press the key
        kb_controller.press(media_key)
        # Small delay for the OS to process the command
        time.sleep(0.05) 
        # Release the key
        kb_controller.release(media_key)
        print(f"-> SUCCESS: Command sent: {media_key}")
    except Exception as e:
        print(f"!!! ERROR: Failed to send command {media_key}: {e}")

# --- SPOTIFY CONTROL FUNCTIONS (Use your hotkeys) ---

def custom_play_pause():
    """Hotkey: Ctrl + Alt + Z. Toggles Play/Pause."""
    # Key.media_play_pause - standard multimedia Play/Pause key
    send_media_key(Key.media_play_pause)

def custom_next_track():
    """Hotkey: Ctrl + Alt + E. Switches to the next track."""
    # Key.media_next - standard multimedia Next Track key
    send_media_key(Key.media_next)

def custom_previous_track():
    """Hotkey: Ctrl + Alt + Q. Switches to the previous track."""
    # Key.media_previous - standard multimedia Previous Track key
    send_media_key(Key.media_previous)
    
def custom_volume_up():
    """New command: Increases volume."""
    # Key.media_volume_up - standard multimedia Volume Up key
    send_media_key(Key.media_volume_up)
    
def custom_volume_down():
    """New command: Decreases volume."""
    # Key.media_volume_down - standard multimedia Volume Down key
    send_media_key(Key.media_volume_down)

def custom_mute_toggle():
    """New command: Toggles Mute/Unmute."""
    # Key.media_mute - standard multimedia Mute key
    send_media_key(Key.media_mute)

# --- REGISTER GLOBAL HOTKEYS ---

# 1. Play/Pause (Keep your combination)
keyboard.add_hotkey('ctrl+alt+z', custom_play_pause)

# 2. Next Track (Keep your combination)
keyboard.add_hotkey('ctrl+alt+e', custom_next_track)

# 3. Previous Track (Keep your combination)
keyboard.add_hotkey('ctrl+alt+q', custom_previous_track)

# 4. Volume Up (New combination)
keyboard.add_hotkey('ctrl+alt+up', custom_volume_up)

# 5. Volume Down (New combination)
keyboard.add_hotkey('ctrl+alt+down', custom_volume_down)

# 6. Mute/Unmute (New combination)
keyboard.add_hotkey('ctrl+alt+m', custom_mute_toggle)


# --- START PROGRAM ---

print("="*60)
print("--- [Spotify Hotkeys Utility (API-less)] ---".center(60))
print("="*60)
print(f"Command delay: {COMMAND_DELAY_SECONDS} second(s).")
print("\n🔥 Hotkeys (work globally):")
print("-" * 30)
print("1. Play / Pause:         Ctrl + Alt + Z")
print("2. Next Track:           Ctrl + Alt + E")
print("3. Previous Track:       Ctrl + Alt + Q")

print("-" * 30)
print("\nPress Ctrl + C in this console window to stop the program.")

try:
    # Block the program to listen for key events
    keyboard.wait()
except KeyboardInterrupt:
    print("\nProgram stopped by the user.")
    sys.exit(0)