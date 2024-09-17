import tkinter as tk
import keyboard
import pyautogui
import pyperclip
import time
import json
import requests
import os
import sys

# Dictionary to match strings and corresponding replacements
URIpath = "https://github.com/Codexadi25/Acebot/blob/c24ef0e180aded47d5560296aaa5bfb7363d1e2a/acebotDictonary.json"
response = requests.get(URIpath)

if response.status_code == 200:
   replacement_dict = json.loads(response.text)
else:
   print("Error fetching Responses : ", response.status_code)


# List to hold current typed string
typed_string = []

def check_and_replace():
   global typed_string
   # Join the current typed characters into a string
   current_text = ''.join(typed_string)

   # Check if the current text matches any dictionary key
   if current_text in replacement_dict:
      # Calculate how many characters to backspace
      txtlen = len(current_text) + 1
      for _ in range(txtlen):
         pyautogui.press('backspace')   
      # Paste the dictionary value
      pyperclip.copy(replacement_dict[current_text])
      pyautogui.hotkey('ctrl', 'v')

      # Reset typed_string since the text has been replaced
      typed_string = []
   elif current_text == "lsdict":
      txtlen = len(current_text) + 1
      for _ in range(txtlen):
         pyautogui.press('backspace')
      with open("Dictonary.json", "w") as f:
         json.dump(replacement_dict, f, indent=4)  # indent for pretty formatting
      # Open the JSON file with the default application
      os.startfile("Dictonary.json")
      
def on_key_event(e):
   global typed_string
   # If the key is printable, add it to the current typed string
   if e.event_type == "down" and len(e.name) == 1:
      typed_string.append(e.name)
   # If backspace is pressed, remove the last character from typed string
   elif e.event_type == "down" and e.name == "backspace":
      if typed_string:
         typed_string.pop()
   # If space is pressed, check and replace, then clear the string
   elif e.event_type == "down" and e.name == "space":
      check_and_replace()
      typed_string = []
   # If enter is pressed, check and replace
   elif e.event_type == "down" and e.name == "enter":
      check_and_replace()
      typed_string = []

# Register a hook for all key events
keyboard.hook(on_key_event)

print("\t\tAcebot started listening for key presses...")
print("\tPlease minimise this window and keep working in background.")
print("\n\tType 'lsdict' to view complete dictonary.")
print("\n\n\n\t\tAditya Tech. & Devoops. - 2024")
# Keep the script running indefinitely
keyboard.wait()
