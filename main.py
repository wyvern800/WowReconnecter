from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con
import threading
from utils import *

global GAME_REGION
global found

is_reconnecting = False
is_selecting_char = False

global action 

'''
    The main application
'''

def main():
    found = None
    lastAction = ''
    action = ''
    print('App is running...')

    is_game_open = checkIfProcessRunning('WowClassic.exe') == True

    try:
        while is_game_open:
            # Check if is game is open
            reconnect_button = pyautogui.locateOnScreen("reconnect.png", confidence=0.5)
            enter_world = pyautogui.locateOnScreen("enter_world.png", confidence=0.5)
            cancel = pyautogui.locateOnScreen("cancel.png", confidence=0.5)
            
            # Reconnect
            if reconnect_button is not None:
                if found is None: 
                    found = reconnect_button
                    action = 'RECONNECTING'
                    print('Reconnect button found')           

            # Enter world
            elif enter_world is not None:
                if found is None:
                    found = enter_world
                    action = 'ENTERING_WORLD'
                    print('Enter world found')
                            
            # Executes the action only if it was the first time
            if lastAction is not action:
                print('Action: ', action)
                pyautogui.click(found)
                lastAction = action
                
            time.sleep(2)           
   
    except KeyboardInterrupt:
        # Close program if subthread issues KeyboardInterrupt
        os._exit(0)

main()