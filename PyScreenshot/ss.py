'''import pyautogui

def take_screenshot():
    # Take a screenshot and save it as "screenshot.png" in the current directory
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')
    print("Screenshot taken and saved as 'screenshot.png'.")

if __name__ == "__main__":
    take_screenshot()
'''

import pyscreenshot

def take_screenshot():
    # Capture the entire screen and save it as "screenshot.png"
    screenshot = pyscreenshot.grab()
    screenshot.save('screenshot.png')
    print("Screenshot taken and saved as 'screenshot.png'.")

if __name__ == "__main__":
    take_screenshot()
