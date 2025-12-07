# Multi-Window Automation with PyAutoGUI

This project demonstrates how to automate typing and sending messages across multiple Chrome windows using Python, PyAutoGUI, and Pyperclip.

## 🚀 Features
- Automatically switches between 3 different Chrome windows.
- Pastes predefined Arabic messages into each window.
- Sends the messages multiple times using a loop.
- Uses PyAutoGUI for keyboard/mouse automation and Pyperclip for Unicode text handling.

## 🧰 Technologies Used
- Python 3
- PyAutoGUI
- Pyperclip
- Time module (sleep)

## 📌 How It Works
Before the script starts, you have 5 seconds to focus on your desktop.  
The script:
1. Clicks on each Chrome window (using screen coordinates)
2. Pastes the message
3. Sends it with **Enter**
4. Moves to the next window and repeats

You must update the `(x, y)` coordinates of your Chrome windows before running the script.

## ⚠️ Important
This project is for **educational purposes only**.  
It demonstrates how automation works and should not be used on platforms where automation or spam is against the terms of service.

## ▶️ Running the Script
Install dependencies:

```bash
pip install pyautogui pyperclip
