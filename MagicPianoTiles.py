# IMPORT LIBS
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


# CO-ORDINATES
#Tile 1 Position: 512 Y:  600 RGB: (160, 165, 232)
#Tile 1 Position: 628 Y:  600 RGB: (155, 161, 231)
#Tile 1 Position: 721 Y:  600 RGB: (253,  18,   1)
#Tile 1 Position: 828 Y:  600 RGB: (164, 169, 232)


# DECLARE
play_toggle = False
fullSize = False
clr_loc1 = 0
clr_loc2 = 0
temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0
temp5 = 0
temp6 = 0

startx = 512        #Tile Starts At
tileWidth = 110

startx_FS = 732     #Fullscreen Tile Starts At
tileWidth_FS = 150

tile1x = startx
tile2x = startx+tileWidth
tile3x = startx+tileWidth*2
tile4x = startx+tileWidth*3

tile1x_FS = startx_FS
tile2x_FS = startx_FS+tileWidth_FS
tile3x_FS = startx_FS+tileWidth_FS*2
tile4x_FS = startx_FS+tileWidth_FS*3


# FUNCTIONS
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)   #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def fullscreen():
    global fullSize
    fullSize = not fullSize
    if pyautogui.pixel(90, 910)[0] == 54:
        click(90, 910)

def google_FS():
    global fullSize
    if pyautogui.pixel(1837, 19)[0] == 0 and pyautogui.pixel(1839,19) == 0:
        fullSize = True
        print(fullSize)
    else:
        x = 0
        y = 0
        for x in range(0, 1920, 606):
            for y in range(0, 1080, 52):
                if pyautogui.pixel(x, y)[0] == 0:
                    y=clr_loc1
                    while pyautogui.pixel(x, y)[0] != 0:
                        y
                else:
                    break
                
def checkClrEndAt(loc_x=None, loc_y=None, direction=None, rgb_check=None):
    r = temp1
    g = temp2
    b = temp3
    if rgb_check == r:
        temp4 = 0
        colorStored = pyautogui.pixel(loc_x,loc_y)[0]
    elif rgb_check == g:
        temp = 1
        colorStored = pyautogui.pixel(loc_x,loc_y)[1]
    elif rgb_check == b:
        temp4 = 2
        colorStored = pyautogui.pixel(loc_x,loc_y)[2]
    while colorStored == pyautogui.pixel(loc_x,loc_y)[temp4]:

    

def play_toggle():
    global play_toggle
    play_toggle = not play_toggle
    if play_toggle:
        print("\nBot is on")
        time.sleep(0.4)
        while keyboard.is_pressed('q') == False:
            print("\nLoading..")
            if fullSize == True:
                if pyautogui.pixel(tile1x_FS, 600)[0] == 0:
                    click(tile1x_FS, 600)
                if pyautogui.pixel(tile2x_FS, 600)[0] == 0:
                    click(tile2x_FS, 600)
                if pyautogui.pixel(tile3x_FS, 600)[0] == 0:
                    click(tile3x_FS, 600)
                if pyautogui.pixel(tile4x_FS, 600)[0] == 0:
                    click(tile4x_FS, 600)
            else:
                if pyautogui.pixel(tile1x, 600)[0] == 0:
                    click(tile1x, 600)
                if pyautogui.pixel(tile2x, 600)[0] == 0:
                    click(tile2x, 600)
                if pyautogui.pixel(tile3x, 600)[0] == 0:
                    click(tile3x, 600)
                if pyautogui.pixel(tile4x, 600)[0] == 0:
                    click(tile4x, 600)
    else:
        print("\nBot is off")
        time.sleep(0.4)

def automatic():



keyboard.add_hotkey('Q', play_toggle)        # HOTKEY
keyboard.add_hotkey('F', fullscreen)
print("Press Q/F to toggle")
keyboard.wait()