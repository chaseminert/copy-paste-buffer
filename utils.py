# grabs data from clipboard and puts it into one of nine slots

import pyautogui
import time

# copying text or pasting text

CTRL_KEY = "ctrlleft"
C_KEY = "c"
V_KEY = "v"


class ClipboardUtils:
    @staticmethod
    def copy_from_screen():
        time.sleep(0.6)
        pyautogui.hotkey("ctrl", "c")

    @staticmethod
    def paste_to_screen():
        pyautogui.hotkey("ctrl", "v")
