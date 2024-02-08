# Importing necessary libraries
import pywhatkit
import pyautogui as auto
from time import sleep

# Function to send WhatsApp message
def wbot():
    # Taking user input for phone number, message, and scheduled time
    phn_no = input("Enter the phone number with country code... :")
    msg = input("Enter The message you want to send... :")
    h = int(input("Enter the time in hours :"))
    m = int(input("Enter the time in minutes :"))

    # Sending WhatsApp message using pywhatkit
    pywhatkit.sendwhatmsg(phn_no, msg, h, m)

# Function for an automated message sending bot
def wbot1():
    while True:
        # Writing 'hello', pressing enter, and then waiting for 1 second
        auto.write('hello')
        auto.press('enter')
        sleep(1)

# Function to choose and execute the desired bot
def auto():
    # Taking user input for the bot to use
    a = input("Input the bot you want to use (1 for WhatsApp message, 2 for automated message): ")

    # Checking user choice and calling the appropriate function
    if a == '1':
        wbot()
    elif a == '2':
        wbot1()
    else:
        print("Invalid Choice! Try Again.")
        auto()

# Calling the main function to execute the bot
auto()
