import pyautogui
import pyperclip
from time import sleep

# HER PENCERENİN KOORDİNATINI BURAYA YAZ
chrome1 = (623, 24)
chrome2 = (1617, 19)
chrome3 = (2579, 26)

mesaj1 = "@yousefalmalta  @hamzayildirim2011 @bera.tmanxd❤️ اللهماستغفر الله العظيم وأتوب إليه ﷺ ❤️"
mesaj2 = "@yousefalmalta  @malektayfur @bera.tmanxd❤️ اللهم ارزقنا حبك وحب من يحبك"
mesaj3 = "❤️@hamzayildirim2011  @yousefalmalta @malektayfur اللهم اجعل القرآن ربيع قلوبنا"

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
