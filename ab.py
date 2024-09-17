import keyboard
import pyautogui
import pyperclip
import time

# Dictionary to match strings and corresponding replacements
replacement_dict = {
   "btw": "by the way",
   "omw": "on my way",
   "idk": "I don't know"
}

# List to hold current typed string
typed_string = []

def check_and_replace():
   global typed_string
   # Join the current typed characters into a string
   current_text = ''.join(typed_string)

   # Check if the current text matches any dictionary key
   if current_text in replacement_dict:
      # Calculate how many characters to backspace
      for _ in range(len(current_text)):
         pyautogui.press('backspace')

      # Paste the dictionary value
      pyperclip.copy(replacement_dict[current_text])
      pyautogui.hotkey('ctrl', 'v')
      # Reset typed_string since the text has been replaced
      typed_string = []

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

print("Listening for key presses...")

# Keep the script running indefinitely
keyboard.wait()
