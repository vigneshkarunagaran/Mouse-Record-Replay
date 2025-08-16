# Mouse Recorder & Replayer (Tkinter + Python)

This project is a simple **Mouse Recorder and Replayer** built with **Python**, **Tkinter**, and **pynput + pyautogui**.  
It allows you to:

- **Record** mouse clicks  
- **Stop** recording anytime  
- **Replay** the recorded clicks with a progress bar and counter  

## Features
- Record all mouse click coordinates into a text file (`clicks.txt`)
- Stop recording whenever needed
- Replay clicks exactly at the same screen positions
- Progress bar + live counter (`current/total`)
- Popup after replay with **success message & replay count**
- Always-on-top floating window

## Requirements

Install required libraries:
```bash
pip install pyautogui pynput
```
