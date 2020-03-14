import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser as wb
import smtplib

print("Initializing Jarvis")



r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe(text):
    hour = int(datetime.datetime.now().hour)
    print("Its", hour, "now")


    if hour>=0 and hour<12:
        speak("Good Morning " + text)
        print('Good Morning Mr.Chatterjee')



    elif hour > 12 and hour < 16 :
        speak("Good afternoon "+ text )
        print("Good afternoon " , "Sir")

    else:
        speak("Good Evening "+ text )
        print("Good Evening " + "Sir")

    speak("I am JARVIS, Your digital AI assistant. How can I help you sir?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Please repeat that again")
        query = None

    return query



def main() :

    # Main program
    r3 = sr.Recognizer()

    speak("Initializing Jarvis")
    speak("Please Authorise Yourself:")

    text = takeCommand()



    wishMe(text)

    while(True):
        query = takeCommand()

        # Logic query
        if 'wikipedia' in query.lower():
             speak("Searching Wikipedia")
             query = query.replace("wikipedia", " ")
             results = wikipedia.summary(query, sentences=3)
             print(results)
             speak(results)

        if "youtube" in query.lower():
            r2 = sr.Recognizer()


            with sr.Microphone() as source:
                speak("Please Search your query")
                print('Search your query')
                audio = r2.listen(source)
            try:

                get = r2.recognize_google(audio)
                print(get)
                wb.get().open_new( 'https://www.youtube.com/results?search_query='+ get)

            except sr.UnknownValueError:
                print('Error')
            except sr.RequestError as e:
                print('failed'.format(e))

        if 'google' in query.lower():
            speak("searching google")
            query = query.replace("google", " ")
            results = wikipedia.summary(query, sentences=3)
            print(results)
            speak(results)

        elif "the time" in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"{text} it is {strTime} now")
            print("Its ", strTime, " right now")

        elif "thanks" in query.lower():
            speak("Welcome Sir, Always at your service")
            print("Welcome")
            break

        elif "code" in query.lower():
            speak("Opening Pycharm")
            codepath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3.1\\bin\\pycharm64.exe"
            os.startfile(codepath)




main()

















