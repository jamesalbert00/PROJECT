import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()

while 1:
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        print(r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
