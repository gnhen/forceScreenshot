import mss
import os
import datetime
import keyboard  # To detect key presses
import threading  # To run in the background

# Path to your Downloads folder
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

def take_screenshot():
    with mss.mss() as sct:
        # Define file name with timestamp
        filename = f"screenshot_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        
        # Full path to save in Downloads
        file_path = os.path.join(downloads_folder, filename)
        
        # Capture the entire screen and save it
        sct.shot(output=file_path)
        print(f"Screenshot saved to {file_path}")

def listen_for_screenshot():
    while True:
        # Wait for the '\' key to be pressed
        keyboard.wait("\\")
        take_screenshot()

# Running the key listener in the background
thread = threading.Thread(target=listen_for_screenshot, daemon=True)
thread.start()

print("Screenshot program is running. Press '\\' to take a screenshot.")
# Keeps the main thread running in the background
thread.join()
