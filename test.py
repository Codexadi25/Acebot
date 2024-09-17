import keyboard  # pip install keyboard
import requests
import json
import time

# Step 1: Fetch the JSON dictionary from GitHub
def fetch_dictionary():
    url = "https://raw.githubusercontent.com/Codexadi25/Acebot/main/acebotDictonary.json?token=GHSAT0AAAAAACXM6KPYBEATTVGFGZQFCXI6ZXJ4Y7Q"
    response = requests.get(url)
    
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print(f"Error fetching the file: {response.status_code}")
        return {}

# Step 2: Monitor keypress and check against dictionary
def monitor_keypress(dictionary):
    buffer = ""  # Store user input
    while True:
        event = keyboard.read_event()
        
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            
            if key == "space":
                # When space is pressed, check if the buffer matches any key in the dictionary
                if buffer in dictionary:
                    # Step 3: Perform backspace to delete the old string
                    for _ in range(len(buffer)):
                        keyboard.press_and_release('backspace')
                    # Step 4: Paste the new string (dictionary value)
                    keyboard.write(dictionary[buffer])
                
                # Reset the buffer after checking
                buffer = ""
            elif len(key) == 1:  # Only append alphanumeric characters
                buffer += key
            elif key == 'backspace' and buffer:
                # Handle backspace manually
                buffer = buffer[:-1]

      #   time.sleep(0.01)  # Small delay to prevent high CPU usage

# Main logic
if __name__ == "__main__":
    dictionary = fetch_dictionary()
    if dictionary:
        monitor_keypress(dictionary)
    else:
        print("Could not fetch dictionary, exiting...")
