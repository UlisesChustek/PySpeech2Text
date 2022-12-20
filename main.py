# import the speech_recognition and pyttsx3 modules
import speech_recognition
import pyttsx3

# create a Recognizer object
recognizer = speech_recognition.Recognizer()

# run the program in an infinite loop
while True:
    
    try:
        # create a Microphone object to listen to audio from the microphone
        with speech_recognition.Microphone() as mic:
            # adjust the Recognizer's energy threshold to filter out background noise
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            # listen for audio from the microphone
            audio = recognizer.listen(mic)
            
            # recognize the spoken text
            text = recognizer.recognize_google(audio)
            # convert the text to lowercase
            text = text.lower()
            
            # print the recognized text
            print(f"Recognized {text} ")
    
    # if speech recognition fails, create a new Recognizer object and continue the loop
    except speech_recognition.UnknownValueError():
            
        recognizer = speech_recognition.Recognizer()
        continue

# note: this code only works in English