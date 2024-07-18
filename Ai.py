import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import smtplib
import os
import sys
import subprocess
import time
import psutil  # For system information
from googletrans import Translator, LANGUAGES  # For translation
import re  # For regular expressions
import random  # For random responses
import pyautogui

# Initialize speech recognition and text-to-speech engine
listener = sr.Recognizer()
listener.dynamic_energy_threshold = True
listener.energy_threshold = 300  # Adjust as needed
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change voice index as needed
engine.setProperty('rate', 170)  # Adjust speech rate
engine.setProperty('volume', 1.0)  # Ensure maximum volume

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, timeout=5, phrase_time_limit=5)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "sudo" in command:
                command = command.replace("sudo", "").strip()
                print("Command:", command)
            return command  # Return recognized command
    except sr.WaitTimeoutError:
        print("Listening timeout")
        talk("I didn't hear anything. Please try again.")
    except sr.UnknownValueError:
        print("Unable to understand audio")
        talk("I couldn't understand your audio")
    except sr.RequestError as e:
        print(f"Error fetching results; {e}")
        talk("Sorry, I could not fetch results at the moment")
    except Exception as e:
        print(f"Error: {e}")
        talk("An error occurred while processing your request")

def run_sudo():
    while True:
        command = take_command()
        if command:
            print("Command:", command)
            if re.match(r"play .+ on youtube", command):
                song_match = re.search(r"play (.+) on youtube", command)
                if song_match:
                    song = song_match.group(1)
                    talk(f"Playing {song} on YouTube")
                    pywhatkit.playonyt(song)
                else:
                    talk("Sorry, I couldn't find the song.")
            elif re.match(r"play .+ on spotify", command):
                song_match = re.search(r"play (.+) on spotify", command)
                if song_match:
                    song = song_match.group(1)
                    talk(f"Playing {song} on Spotify")
                    play_song_on_spotify(song)
                else:
                    talk("Sorry, I couldn't find the song.")
            elif "time" in command:
                current_time = datetime.datetime.now().strftime('%I:%M %p')
                print("Current time:", current_time)
                talk("The current time is " + current_time)
            elif "wikipedia" in command:
                search_query = command.replace("wikipedia", "").strip()
                try:
                    result = wikipedia.summary(search_query, sentences=1)
                    print("According to Wikipedia:", result)
                    talk("According to Wikipedia, " + result)
                except wikipedia.exceptions.DisambiguationError as e:
                    print("Disambiguation Error:", e)
                    talk("There are multiple results. Please be more specific.")
                except wikipedia.exceptions.PageError as e:
                    print("Page Error:", e)
                    talk("Sorry, I could not find any information.")
                except Exception as e:
                    print("Error:", e)
                    talk("Something went wrong with Wikipedia search.")
            elif "open website" in command:
                website = command.replace("open website", "").strip()
                url = "https://" + website
                webbrowser.open(url)
                talk(f"Opening {website}")
            elif "send email" in command:
                try:
                    talk("What should I say?")
                    content = take_command()
                    to = "receiver@example.com"  # Replace with recipient's email
                    send_email(to, content)
                    talk("Email sent successfully!")
                except Exception as e:
                    print(f"Error sending email: {e}")
                    talk("Unable to send email at the moment.")
            elif "search" in command:
                search_query = command.replace("search", "").strip()
                url = f"https://www.google.com/search?q={search_query}"
                webbrowser.open(url)
                talk(f"Here are the search results for {search_query}")
            elif "calculator app" in command:
                os.system("calc")  # Opens Calculator on Windows
                talk("Opening Calculator")
            elif "notepad app" in command:
                os.system("notepad")  # Opens Notepad on Windows
                talk("Opening Notepad")
            elif "spotify app" in command:
                talk("Opening Spotify")
                open_spotify()
            elif "youtube app" in command:
                talk("Opening YouTube")
                open_youtube()
            elif "word app" in command or "microsoft word" in command:
                talk("Opening Microsoft Word")
                open_ms_word()
            elif "excel app" in command or "microsoft excel" in command:
                talk("Opening Microsoft Excel")
                open_ms_excel()
            elif "powerpoint app" in command or "microsoft powerpoint" in command:
                talk("Opening Microsoft PowerPoint")
                open_ms_powerpoint()
            elif "chrome app" in command or "google chrome" in command:
                talk("Opening Google Chrome")
                open_chrome()
            elif "store app" in command or "microsoft store" in command:
                talk("Opening Microsoft Store")
                open_ms_store()
            elif "paint app" in command:
                talk("Opening Paint")
                open_paint()
            elif "calendar app" in command:
                talk("Opening Calendar")
                open_calendar()
            elif "settings app" in command:
                talk("Opening Settings")
                open_settings()
            elif "shutdown" in command:
                talk("Shutting down the system. Goodbye!")
                os.system("shutdown /s /t 1")
            elif "restart" in command:
                talk("Restarting the system now.")
                os.system("shutdown /r /t 1")
            elif "exit" in command:
                talk("Exiting sudo assistant. Goodbye!")
                sys.exit()
            elif "how are you" in command:
                responses = [
                    "I'm functioning perfectly! How can I assist you today?",
                    "I'm doing great! Thank you. What can I do for you?",
                    "I'm feeling wonderful! What do you need help with?",
                ]
                talk(random.choice(responses))
            elif "tell me a joke" in command:
                jokes = [
                    "Why don't scientists trust atoms? Because they make up everything!",
                    "Parallel lines have so much in common. It’s a shame they’ll never meet.",
                    "I told my wife she should embrace her mistakes. She gave me a hug.",
                ]
                talk(random.choice(jokes))
            elif "i love you" in command:
                talk("Sorry, but I'm in a relationship with WiFi.")
            elif "what is your name" in command:
                talk("I am your Sudo Assistant. What's your name?")
            elif "my name is" in command:
                name = command.replace("my name is", "").strip()
                talk(f"Nice to meet you, {name}!")
            elif "do you like me" in command:
                talk("Of course I do! You're my favorite person.")
            elif "tell me something interesting" in command:
                facts = [
                    "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
                    "The Eiffel Tower can be 15 cm taller during the summer, due to the expansion of the iron on hot days.",
                    "Octopuses have three hearts: two pump blood through the gills, while the third pumps it through the rest of the body.",
                ]
                talk(random.choice(facts))
            elif "tell me about you" in command:
                talk("""This script integrates various Python libraries to create a voice-controlled virtual assistant capable of performing 
                     tasks ranging from basic web searches and media playback to sending emails and retrieving system information. It leverages 
                     speech recognition for user input and text-to-speech for output, making it interactive and engaging. Each function serves a 
                     specific purpose, utilizing Python's standard and third-party libraries to achieve functionality across different domains!
                     How can I assist you today?""")
            elif "file operations" in command:
                talk("Opening File Operations")
                # file operations function added soon ...
            elif "system information" in command:
                talk("Fetching System Information")
                get_system_information()
            elif "translate" in command:
                handle_translation()
            elif "math" in command or re.match(r"what is \d+[+\-*/%^]\d+", command):
                math_match = re.search(r"what is (.+)", command)
                if math_match:
                    math_expression = math_match.group(1)
                    calculate_math_expression(math_expression)
                else:
                    talk("Sorry, I couldn't understand the math expression.")
            elif "what can you do" in command or "capabilities" in command:
                what_can_you_do()
            elif "close" in command:
                app_name = command.replace("close", "").strip()
                close_application(app_name)
            else:
                talk("I don't understand your command")

def send_email(to, content):
    # Replace with your email credentials and SMTP server details
    server = smtplib.SMTP('smtp.example.com', 587)
    server.ehlo()
    server.starttls()
    server.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))
    server.sendmail(os.getenv('EMAIL_USER'), to, content)
    server.close()

def play_song_on_spotify(song):
    talk(f"Playing {song} on Spotify")
    # Open Spotify
    os.startfile("C:\Program Files\WindowsApps\SpotifyAB.SpotifyMusic_1.241.434.0_x64__zpdnekdrzrea0\Spotify.exe")  # Make sure the path to Spotify executable is correct

    # Wait for Spotify to open
    time.sleep(5)

    # Search for the song
    pyautogui.hotkey("ctrl", "l")  # Focus on the search bar
    time.sleep(1)
    pyautogui.typewrite(song)
    pyautogui.press("enter")

    # Wait for the search results to load
    time.sleep(3)

    # Play the first song in the search results
    pyautogui.press("tab", presses=3, interval=0.2)  # Navigate to the first song
    pyautogui.press("enter")

def open_spotify():
    os.startfile("C:\Program Files\WindowsApps\SpotifyAB.SpotifyMusic_1.241.434.0_x64__zpdnekdrzrea0\Spotify.exe")
def open_youtube():
    webbrowser.open("https://www.youtube.com")
    talk("Opening YouTube")

def open_ms_word():
    os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")  # Adjust path
    talk("Opening Microsoft Word")

def open_ms_excel():
    os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")  # Adjust path
    talk("Opening Microsoft Excel")

def open_ms_powerpoint():
    os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")  # Adjust path
    talk("Opening Microsoft PowerPoint")

def open_chrome():
    try:
        subprocess.Popen(['C:/Program Files (x86)/Google/Chrome/Application/chrome.exe', 'https://www.google.com'])
        talk("Opening Google Chrome")
    except Exception as e:
        print(f"Error opening Chrome: {e}")
        talk("Error opening Google Chrome")

def open_ms_store():
    os.startfile("ms-windows-store://home")
    talk("Opening Microsoft Store")

def open_paint():
    os.startfile("mspaint")
    talk("Opening Paint")

def open_calendar():
    os.startfile("outlookcal:")
    talk("Opening Calendar")

def open_settings():
    os.startfile("ms-settings:")
    talk("Opening Settings")

def get_system_information():
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    info = f"CPU Usage: {cpu_usage}%, RAM Usage: {ram_usage}%, Disk Usage: {disk_usage}%"
    print("System Information:", info)
    talk("Here is your system information: " + info)

def handle_translation():
    try:
        talk("What text should I translate?")
        text_to_translate = take_command()
        if text_to_translate:
            talk("Which language should I translate it to?")
            dest_language = take_command().lower()
            if dest_language in LANGUAGES.values():
                translate_text(text_to_translate, dest_language)
            else:
                talk("I'm sorry, I don't know that language.")
        else:
            talk("I didn't catch the text to translate.")
    except Exception as e:
        print(f"Translation error: {e}")
        talk("Sorry, I couldn't translate the text.")

def translate_text(text, dest_language):
    translator = Translator()
    dest_language_code = LANGUAGES[dest_language]
    try:
        translated_text = translator.translate(text, dest=dest_language_code)
        print(f"Translated from {translated_text.src} to {translated_text.dest}: {translated_text.text}")
        talk(f"Translated to {translated_text.dest}: {translated_text.text}")
    except Exception as e:
        print(f"Translation error: {e}")
        talk("Sorry, I couldn't translate the text.")

def calculate_math_expression(expression):
    try:
        result = eval(expression)
        print(f"Evaluating: {expression}")
        talk(f"The result is {result}")
    except Exception as e:
        print(f"Math error: {e}")
        talk("Sorry, I couldn't calculate that.")

def what_can_you_do():
    try:
        functionalities = """
        Here are the things I can do:
        1. Play videos on YouTube or Spotify.
        2. Tell you the current time.
        3. Search information on Wikipedia.
        4. Open websites.
        5. Send emails.
        6. Perform web searches.
        7. Open applications like 
        [Calculator, Notepad, Spotify, YouTube, Word, Excel, 
        PowerPoint, Chrome, Microsoft Store, Paint,
        Calendar, and Settings]
        8. Shutdown or restart the system.
        9. Respond to casual questions like "How are you?" and "Tell me a joke."
        10. Perform file operations (feature under development).
        11. Provide system information.
        12. Translate text.
        13. Perform calculations.
        """
        print(functionalities)
        talk("Here are the things I can do for you.")
    except Exception as e:
        print(f"Error: {e}")
        talk("Sorry, I couldn't fetch the functionalities at the moment.")
        
def close_application(app_name):
    try:
        if app_name in ['notepad', 'calculator', 'spotify', 'youtube', 'word', 'excel', 'powerpoint', 'chrome', 'store', 'paint', 'calendar', 'settings']:
            if app_name == 'notepad':
                app_name = 'notepad.exe'
            elif app_name == 'calculator':
                app_name = 'Calculator.exe'
            elif app_name == 'spotify':
                # Kill Spotify process
                for proc in psutil.process_iter(['pid', 'name']):
                    if proc.info['name'].lower() == 'Spotify.exe':
                        proc.kill()
                        talk("Closed Spotify")
                        return
                talk("Spotify is not running.")
                return
            elif app_name == 'youtube':
                # Close browser tab with YouTube
                pyautogui.hotkey('ctrl', 'w')
                return
            elif app_name == 'word':
                app_name = 'WINWORD.EXE'
            elif app_name == 'excel':
                app_name = 'EXCEL.EXE'
            elif app_name == 'powerpoint':
                app_name = 'POWERPNT.EXE'
            elif app_name == 'chrome':
                app_name = 'chrome.exe'
            elif app_name == 'store':
                app_name = 'WinStore.App.exe'
            elif app_name == 'paint':
                app_name = 'mspaint.exe'
            elif app_name == 'calendar':
                app_name = 'HxCalendarAppImm.exe'
            elif app_name == 'settings':
                app_name = 'SystemSettings.exe'

            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['name'].lower() == app_name.lower():
                    proc.kill()
                    talk(f"Closed {app_name.replace('.exe', '')}")
                    return
            talk(f"{app_name.replace('.exe', '')} is not running.")
        else:
            talk(f"Sorry, I don't know how to close {app_name}.")
    except Exception as e:
        print(f"Error closing {app_name}: {e}")
        talk(f"Could not close {app_name.replace('.exe', '')}")

if __name__ == "__main__":
    run_sudo()
