import mss
import os
import datetime
import keyboard
import threading

downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

def take_screenshot():
    with mss.mss() as sct:
        filename = f"screenshot_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        file_path = os.path.join(downloads_folder, filename)
        sct.shot(output=file_path)
        print(f"Screenshot saved to {file_path}")

def listen_for_screenshot():
    while True:
        keyboard.wait("\\")
        take_screenshot()

thread = threading.Thread(target=listen_for_screenshot, daemon=True)
thread.start()

print("Screenshot program is running. Press '\\' to take a screenshot.")
thread.join()
