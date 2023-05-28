import speech_recognition as sr
import pyautogui
import threading

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the default microphone as the audio source
microphone = sr.Microphone()

# Adjust microphone settings if needed (sample rate and chunk size)
# microphone = sr.Microphone(sample_rate=44100, chunk_size=4256)
# scrollstatus="stopped"
# def scrollup():
#     while scrollstatus=="up":
#         pyautogui.scroll(5)
# def scrolldown():
#     while scrollstatus=="down":
#         pyautogui.scroll(-5)
# def scrollstop():
#     while True:
#         audioscroll = recognizer.listen(source)
#         textscroll = recognizer.recognize_google(audioscroll).lower()
#         print("You said:", textscroll)
#         if "stop" in textscroll:
#             scrollstatus="stopped"
#             break

# def scrollingmode(mode):
#     if mode=="down":
#         thread1 = threading.Thread(target=scrolldown)
#         thread2 = threading.Thread(target=scrollstop)
#         thread1.start()
#         thread2.start()
#         thread2.join()
#     elif mode=="up":
#         thread1 = threading.Thread(target=scrollup)
#         thread2 = threading.Thread(target=scrollstop)
#         thread1.start()
#         thread2.start()
#         thread2.join()

# Capture live audio from the microphone indefinitely
with microphone as source:
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("Listening...")

    while True:
        audio = recognizer.listen(source)

        try:
            # Convert speech to text
            text = recognizer.recognize_google(audio).lower()
            print("You said:", text)

            # Check if the wake keyword is detected
            if "open" in text and "new" in text and "tab" in text:
                # Press the Ctrl+T keyboard combination using pyautogui
                pyautogui.hotkey('ctrl', 't')
            
            if (text=='scroll') or ("scroll" in text and "down" in text):
                # Press the Ctrl+T keyboard combination using pyautogui
                pyautogui.scroll(-100)
            
                
            if "scroll" in text and "up" in text:
                # Press the Ctrl+T keyboard combination using pyautogui
                pyautogui.scroll(150)
                
            elif "close" in text and "tab" in text:
                # Press the Ctrl+T keyboard combination using pyautogui
                pyautogui.hotkey('ctrl', 'w')
                
            elif "close" in text and "window" in text:
                # Press the Ctrl+T keyboard combination using pyautogui
                pyautogui.hotkey('alt', 'f4')
                
            elif "switch" in text and "windows" in text:
                # Press the Ctrl+T keyboard combination using pyautogui
                pyautogui.hotkey('alt', 'tab')
                
            elif "open" in text and "youtube" in text:
                # Press the Ctrl+T keyboard combination using pyautogui
                pyautogui.write('youtube.com')
                pyautogui.press('enter')
                
            elif "go" in text and "windows" in text and "to" in text:
                # Press the Ctrl+T keyboard combination using pyautogui
                pyautogui.press('win')
            
            elif text.startswith('type') or text.startswith('search'):
                # Press the Ctrl+T keyboard combination using pyautogui
                if text.startswith('type'):
                    datatotype=text.replace("type ","")
                    pyautogui.write(datatotype)
                elif text.startswith('search for'):
                    datatotype=text.replace("search for ","")
                    pyautogui.write(datatotype)
                elif text.startswith('search'):
                    datatotype=text.replace("search ","")
                    pyautogui.write(datatotype)
            
            elif text.startswith('press'):
                # Press the Ctrl+T keyboard combination using pyautogui
                datatotype=text.replace("press ","")
                pyautogui.press(datatotype)
                
        except sr.UnknownValueError:
            print("Sorry, I could not understand your speech.")
        except sr.RequestError as e:
            print("Sorry, an error occurred. Error:", str(e))
