import tkinter as tk
import keyboard
import pyautogui
import pyperclip
import time
import json
import os
import sys

# Dictionary to match strings and corresponding replacements
replacement_dict = {
   "mymail" : "Aditya.Sahu1@startek.com",

   "/pn" : "Karma // Disputes // 0 disputes in linked // \n\nIssues Raised: \n\nObservation :-",

   "pquv": "PQ // UV Issues // Hence, Denied as per RB",

   "pqstale": "PQ : Stale/smell // UV Issues // Hence, Denied as per RB",

   "fsicnp": "FSSAI :   // Checks not passed as per RB // not a clean history // Same Pattern // Hence, Denied as per RB",

   "nch" : "Calling Ticket // Non-Calling Hrs. // ON HOLD",

   "refs" : "We have initiated a refund of ₹XX for your order XXXXXXXXXX. The amount shall reflect in the source account within 7 working days.",

   "mxpromo" : "A one-time use code has been already added to the promo section of your cart. The flat discount of ₹XXXX will be auto-applied once you place the order from the same restaurant(XXXXXXXXXX).",

   "refp" : "We would like to inform you that we have already initiated a promo code (XXXXXXXXX) on XXX . You can use it one-time only to get a flat discount of ₹XXXX on your next order The code will be valid for 30 days and is applicable for all restaurants.",

   "cxur" : "As per your request, we tried to reach you over call but your call went unresponsive.",

   "cxur1" : "With regards to your concern, as you have requested a call back from us, we attempted to call you on your registered number but your call went unresponsive.",

   "fdbk" : "Don't worry we will not let this go unnoticed and your feedback is valuable to us. We would love to work on your significant feedback to improve our services.",

   "fdbk1" : "Please be assured that your feedback will not go unnoticed. It is very important to us, and we are committed to using it to improve our services.",

   "rca": "Ticket ID:[]\nOrder ID: []\nCX Karma:[]\nCX VOC:\nIssue:\nObservation:\nResolution: [Pending]",

   "inf" : "We understand you are unhappy that the restaurant has missed following your instructions. We would have been happy to help you with it. Though, we haven't assured you that 100%% instruction will be followed as it depends upon the restaurant and the same is also mentioned in the disclaimer.",

   "mxpromo" : "A one-time use code has been already added to the promo section of your cart. The flat discount of ₹XXXX will be auto-applied once you place the order from the same restaurant(XXXXXXXXXX).",

   "ddelay" : "We know what you would be going through as food is something for which one can never wait especially when one is hungry. We request you to consider this as a one time exception and give us another chance to fix this and serve you better.",

   "pq" : "Zomato is an intermediary platform connecting restaurants and customers, with limited control over the quality and quantity of the food. However, in an effort to enhance customer satisfaction and avoid potential issues, we actively share feedback with the respective restaurants. However, considering the current scenario, we shall not be able to issue a refund.",

   "dpbeh" : "We looked into your concern and apologies for the inappropriate behavior of our delivery executive. We always aim to provide the best customer satisfaction to all our foodies and will keep working hard to ensure this.",

   "ackmail" : "Hi XXXX,\n\nHope you are doing well.\n\nWe completely understand that your recent online ordering experience was not up to your expectations. We are dedicated to swiftly resolving this issue and assuring your satisfaction.\n\nWe would like to inform you that we are actively working on your concern and will get back to you as soon as possible. Your patience is highly appreciated.\n\nRest assured that we constantly work towards providing you with a good experience.\n\nBest Regards,\nTeam Zomato",

   "missmxdpur" : "Hi XXXXXXX,\n\nHope you are doing well.\n\nThis mail is for Order ID - XXXXXXX from XXXXXX.\n\nWe want to sincerely apologize for the inconvenience caused by the missing item in your recent order. We certainly never want our customers to face these kinds of issues.\n\nWe understand the importance of your satisfaction and we have attempted to contact our restaurant partner to validate your claim, however, we would like to inform you that we have not received confirmation from the restaurant partner. Unfortunately without the confirmation, we are unable to make any adjustments in case of compensation against this order.\n\nRest assured we are constantly trying to improve our services so that we can try to serve you better in future orders.\n\nRegards\nTeam Zomato",

   "/pquv" : "Hi XXXXX,\n\nHope you are doing well.\n\nThis mail is for Order ID - XXXXXX from [Restaurant Name].\n\nWe completely understand how inconvenient it could be when the order is not delivered as per expectations. We certainly never want our customers to face these kinds of issues.\n\nZomato is an intermediary platform connecting restaurants and customers, with limited control over the quality and quantity of the food. However, in an effort to enhance customer satisfaction and avoid potential issues, we actively share feedback with the respective restaurants. However, considering the current scenario, we shall not be able to issue a refund.\n\nWe request you to drop a review on the restaurant page to help them serve better. We appreciate your understanding in this matter and remain committed to addressing any other concerns you may have.\n\nRegards,\nTeam Zomato",

   "pqlq" : "PQ :: Less Qty // UV Issues // Hence, Denied as per RB",

   "cat" : "Uncat. // NO Order Details // Hence, Requested",

   "samemx" : "We would like to inform you that the order is delivered to you from the restaurant that you have chosen. Further we would request you to please check the restaurant rating before placing the order.",

   "pquvl" : "Zomato is an intermediary platform connecting restaurants and customers, with limited control over the quality and quantity of the food. However, in an effort to enhance customer satisfaction and avoid potential issues, we actively share feedback with the respective restaurants. However, considering the current scenario, we shall not be able to issue a refund.",

   "gcbur" : "GIFT_CALLBACK // Giftee UR",

   "/gcbur" : "Hi XXXXXXXX,\n\nHope you are doing well.\n\nThis mail is regarding your gift order with order ID XXXXXXXX from XXXXXXXX.\n\nThe gift recipient raised the concern and we called the recipient but the call was not answered.\n\nIf you have any concerns, please reach out to us. We'll be happy to assist you.\n\nBest regards,\nTeam Zomato",

   "/gcbno" : "Hi XXXX,\n\nHope you are doing well.\n\nThis mail is regarding your gift order with order ID- XXXXXX from XXXXXXX\n\nThe gift recipient raised the concern and we called the recipient but, the customer said that he had no issue with the order.\n\nIf you have any concerns, please reach out to us. We'll be happy to assist you.\n\nBest regards,\nTeam Zomato",

   "/gcbcard" : "Hi XXXX,\n\nHope you are doing well.\n\nThis mail is regarding your gift order with order ID- XXXXXX from XXXXXXX\n\nThe gift recipient raised the concern and we called the recipient they have informed us that they have not received the gift card with the order.\n\nA gift card is an e-card and no physical card will be sent. As soon as when you places a gift order for someone, an SMS will be sent to that customer along with a link. After clicking on the link, the gift card can be viewed for whom the order has been placed.\n\nIf you have any concerns, please reach out to us. We'll be happy to assist you.\n\nBest regards,\nTeam Zomato",

   "/wmxur" : "Hi XXXXX,\n\nHope you are doing well.\n\nThis mail is for Order ID - XXXXXXX from XXXXXXXX.\n\nWe understand the frustration and inconvenience of receiving the wrong item, and we sincerely apologize for this oversight. We certainly never want our customers to face these kinds of issues.\n\nWe would like to inform you that we have not received confirmation from the restaurant partner. Unfortunately without the confirmation, we are unable to make any adjustments in case of compensation against this order.\n\nWe would also request you to drop a review on the restaurant page to help them serve better. If you have any further questions or concerns, please feel free to contact us.\n\nRegards,\nTeam Zomato",

   "/wrongmxdeny" : "Hi XXXXXX,\n\nHope you are doing well.\n\nThis mail is for Order ID - XXXXXXXX from XXXXXXX.\n\nWe understand the frustration and inconvenience of receiving the wrong item, and we sincerely apologize for this oversight. We certainly never want our customers to face these kinds of issues.\n\nWe raised your concern with our restaurant partner, and they informed us that correct items were delivered to you. Having carefully evaluated the issue based on your complaint, we regret to inform you that we will not be able to proceed with a refund against your escalation. We encourage you to share a review on the restaurant page to help your fellow foodies make an informed choice to their liking.\n\nIf you have any further questions or concerns, please feel free to contact us.\n\nRegards,\nTeam Zomato",

   "/fssaicnp" : "Hi XXXXX,\n\nHope you are doing well.\n\nThis mail is for Order ID - XXXXXX from  [Restaurant Name].\n\nWe deeply regret the inconvenience caused by the presence of <foreign object name>  in your food. We certainly never want our customers to face these kinds of issues.\n\nWhile we empathize with your concern, we regret to inform you that the image provided by you did not pass the checks we ran before disputing this order with the restaurant. Consequently, we are unable to proceed with a refund at this moment.\n\nWe apologize for any inconvenience this may cause and appreciate your understanding. If you have any further questions or concerns, please feel free to contact us.\n\nRegards,\nTeam Zomato",

   "det" : "Hi There,\n\nHope you are doing well.\n\nWe completely understand how inconvenient it could be when the order is not delivered as per expectations. We certainly never want our customers to face these kinds of issues.\n\nRegarding your complaint, we have attempted to locate your details using your registered email ID, but we have been unsuccessful in doing so. We kindly request you to provide us with the necessary information, such as your concerned order ID. Your prompt cooperation in this matter would greatly facilitate our efforts to assist you effectively.\n\nRegards,\nTeam Zomato",
   
   "wour" : "Hi XXXXX,\n\nHope you are doing well.\n\nThis mail is for Order ID - XXXXXXX from XXXXXXXX.\n\nWe understand the frustration and inconvenience of receiving the wrong item, and we sincerely apologize for this oversight. We certainly never want our customers to face these kinds of issues.\n\nWe would like to inform you that we have not received confirmation from the restaurant partner. Unfortunately without the confirmation, we are unable to make any adjustments in case of compensation against this order.\n\nWe would also request you to drop a review on the restaurant page to help them serve better. If you have any further questions or concerns, please feel free to contact us.\n\nRegards,\nTeam Zomato",

   "mul" : "Hi xxx,\n\nHope you are doing well.\n\nThis mail is for Order ID- xxxx from xxxx\n\nWe understand the issue you had to face regarding the overall experience in your Zomato order. We are dedicated to swiftly resolving this issue and assuring your satisfaction.\n\nWith regard to your...\n\nIf you have any other concerns, please reach out to us. We'll be happy to assist you.\n\nRegards\nTeam Zomato",


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

print("\t\tAxila started listening for key presses...")
print("\tPlease minimise this window and keep working in background.")
print("\n\tType 'lsdict' to view complete dictonary.")
print("\n\n\n\t\tAditya Tech. & Devoops. - 2024")
# Keep the script running indefinitely
keyboard.wait()
