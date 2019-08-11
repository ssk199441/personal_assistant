import os
import sys
import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import wolframalpha
import webbrowser
import smtplib
import random
from pygame import mixer
import playsound
import numpy
import cv2

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('U63W2J-AHQUH9UYW3')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 2].id)


def talk(audio):
    print('KryptoKnite: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    CurrentHour = int(datetime.datetime.now().hour)
    if CurrentHour >= 0 and CurrentHour < 12:
        talk('Good Morning!')

    elif CurrentHour >= 12 and CurrentHour < 18:
        talk('Good Afternoon!')

    elif CurrentHour >= 18 and CurrentHour != 0:
        talk('Good Evening!')


greetMe()

talk('Hey Buddy, It\'s  your assistant KryptoKnite!')
talk('tell me about today?')


def GivenCommand():
    # k = sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("Listening...")
    #     k.pause_threshold = 1
    #     audio = k.listen(source)
    # try:
    #     Input = k.recognize_google(audio, language='en-in')
    #     print('Kunal Dhariwal: ' + Input + '\n')
    #
    # except sr.UnknownValueError:
    #     talk('Sorry! I didn\'t get that! Try typing it here!')


      Input = str(input('Command: '))
      return Input


if __name__ == '__main__':

    while True:

        Input = GivenCommand()
        Input = Input.lower()

        if 'open google' in Input:
            talk('sure')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in Input:
            talk('sure')
            webbrowser.open('www.gmail.com')

        elif 'open youtube' in Input:
            talk('sure')
            webbrowser.open('www.youtube.com')

        elif "what\'s up" in Input or 'how are you' in Input:
            setReplies = ['Just doing some stuff!', 'I am good!', 'Nice!', 'I am amazing and full of power']
            talk(random.choice(setReplies))

        elif "who are you" in Input or 'where are you' in Input or 'what are you' in Input:
            setReplies = [' I am KryptoKnite', 'In your system', 'I am an example of AI']
            talk(random.choice(setReplies))

        elif 'email' in Input:
            talk('Who is the recipient? ')
            recipient = GivenCommand()

            if 'me' in recipient:
                try:
                    talk('What should I say? ')
                    content = GivenCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    talk('Email sent!')

                except:
                    talk('Sorry ! I am unable to send your message at this moment!')

        elif 'nothing' in Input or 'abort' in Input or 'stop' in Input:
            talk('okay')
            talk('Bye, have a good day.')
            sys.exit()

        elif 'hello' in Input:
            talk('hey')

        elif 'bye' in Input:
            talk('Bye, have a great day.')
            sys.exit()


        elif 'play music' in Input:
            # music_folder = 'C:\\Users\\Public\\Music\\'
            # music = ['Adada-Mazhaida']
            # random_music = music_folder + random.choice(music) + '.mp3'
            # os.system(random_music)
            playsound.playsound('F:\Music\Adada-Mazhaida.mp3', True)
            # mixer.init()
            # mixer.music.load('C:/Users/Public/Music/Adada-Mazhaida.mp3')
            # mixer.music.play()

            talk('Okay, here is your music! Enjoy!')

        elif 'show images' in Input:
            # images_folder = 'C:\\Users\\Public\\Pictures\\'
            # images_folder = 'C:\\Users\\Admin\\Pictures\\CameraRoll\\'
            #
            # images = ['IMG_20180219_170426']
            # random_images = images_folder + random.choice(images) + '.jpg'
            # os.system(random_images)
            img = cv2.imread('D:\Giri\Giri_1.jpg', 0)
            cv2.imshow('image', img)
            # cv2.waitkey(0)
            # cv2.destroyAllWindows()


            talk('Okay, here are your images! Have Fun!')


        else:
            Input = Input
            talk('Searching...')
            try:
                try:
                    res = client.Input(Input)
                    outputs = next(res.outputs).text
                    talk('Alpha says')
                    talk('Gotcha')
                    talk(outputs)

                except:
                    outputs = wikipedia.summary(Input, sentences=3)
                    talk('Gotcha')
                    talk('Wikipedia says')
                    talk(outputs)


            except:
                talk("searching on google for " + Input)
                say = Input.replace(' ', '+')
                webbrowser.open('https://www.google.co.in/search?q=' + Input)

        talk('Next Command! Please!')
