import pyperclip
import tkinter as tk
from tkinter import messagebox, ttk
from pynput import mouse
import pyautogui
import threading
import time
import os


recording = False
file_path = "clicks.txt"
listener = None
replay_count = 0  

links = ["a", "b"]
def on_click(x, y, button, pressed):
    global file_path
    if recording and pressed:
        with open(file_path, "a") as f:
            f.write(f"{x},{y}\n")
        print(f"Recorded: {x}, {y}")


def start_recording():
    global recording, listener, file_path
    if os.path.exists(file_path):
        os.remove(file_path)
    recording = True
    listener = mouse.Listener(on_click=on_click)
    listener.start()
    print(f"Recording started... Saving to {file_path}")


def stop_recording():
    global recording, listener
    recording = False
    if listener:
        listener.stop()
    print("Recording stopped.")


def replay_clicks():
    global replay_count
    if not file_path or not os.path.exists(file_path):
        print("No recorded file found.")
        return

    with open(file_path, "r") as f:
        lines = f.readlines()

    if not lines:
        print("No clicks to replay.")
        return

    print("Replaying clicks...")
    replay_count += 1

    progress_bar["maximum"] = len(links)
    progress_bar["value"] = 0
    progress_label.config(text=f"0 / {len(links)}")

    for i, line in enumerate(links, start=1):
        pyperclip.copy(line)
        click1 = (1704, 16)
        x, y = map(int, click1)
        pyautogui.click(x, y)   #new tab
        time.sleep(1)

        pyautogui.hotkey("ctrl", "v") 
        pyautogui.press("enter")
        time.sleep(3)

        click2 = (1269, 161)
        x, y = map(int, click2)
        pyautogui.click(x, y) #get link
        time.sleep(2)

        click3 = (430, 469)
        pyautogui.hotkey("ctrl", "c") 
        retrivedTest = pyperclip.paste()
        print(retrivedTest)

        progress_bar["value"] = i
        progress_label.config(text=f"{i} / {len(lines)}")
        root.update_idletasks()


    
    # for i, line in enumerate(lines, start=1):
    #     x, y = map(int, line.strip().split(","))
    #     pyautogui.click(x, y)
    #     time.sleep(0.2)

    #     progress_bar["value"] = i
    #     progress_label.config(text=f"{i} / {len(lines)}")
    #     root.update_idletasks()

    print("Replay finished.")
    messagebox.showinfo("Replay", f"Success ✅\nReplay count: {replay_count}")


root = tk.Tk()
root.title("☠️")
root.attributes("-topmost", True)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="📸", command=lambda: threading.Thread(target=start_recording).start(), width=15).pack(side="left", padx=5)
tk.Button(button_frame, text="⛔", command=stop_recording, width=15).pack(side="left", padx=5)
tk.Button(button_frame, text="▶️", command=lambda: threading.Thread(target=replay_clicks).start(), width=15).pack(side="left", padx=5)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=5)

progress_label = tk.Label(root, text="0 / 0")
progress_label.pack()

root.mainloop()
