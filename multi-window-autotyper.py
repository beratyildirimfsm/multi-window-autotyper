import pyautogui
import pyperclip
from time import sleep

# HER PENCERENİN KOORDİNATINI BURAYA YAZ
chrome1 = (623, 24)
chrome2 = (1617, 19)
chrome3 = (2579, 26)

mesaj1 = "text1"
mesaj2 = "text2"
mesaj3 = "text3"

sleep(5)

for i in range(10):

    # --- 1. PENCERE ---
    pyautogui.click(chrome1)   # pencereyi seç
    pyperclip.copy(mesaj1)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    sleep(0.3)

    # --- 2. PENCERE ---
    pyautogui.click(chrome2)
    pyperclip.copy(mesaj2)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    sleep(0.3)

    # --- 3. PENCERE ---
    pyautogui.click(chrome3)
    pyperclip.copy(mesaj3)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    sleep(0.3)

