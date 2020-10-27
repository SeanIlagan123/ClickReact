import pyautogui
from PIL import ImageGrab

try:
    print("Press CTRL+C While in Terminal to STOP!")
    while(True):
        currentMouseX, currentMouseY = pyautogui.position()
        image = ImageGrab.grab() 
        if image.getpixel((currentMouseX, currentMouseY)) == (75, 219, 106):
            print("WOW! INHUMAN REACTIONS")
            pyautogui.click()
except KeyboardInterrupt:
    print("FORCE QUIT")
    pass