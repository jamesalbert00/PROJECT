import pyttsx3
import os
import speech_recognition as sr
from word2number import w2n
import random
from icmplib import ping, multiping, traceroute, resolve, Hop
from icmplib import ICMPv4Socket, ICMPv6Socket, ICMPRequest, ICMPReply


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

random1 = ['What do you want me to do','What the heck is you need for me','Iam busy can you interrupt me another time.','Make it faster Just make an order']
attn = random.choices(random1) 
random2 = ['Idiot','Fucker','Asshole','Puss']
attn2 = random.choices(random2)
r = sr.Recognizer()



def listen(prompt):
    with sr.Microphone() as source:
        print(prompt)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print('You said :{}' .format(text))
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def say(prompt):
    with sr.Microphone() as source:
        print(prompt)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print('You said :{}' .format(text))
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def talk(message):
    engine.say(message)
    engine.runAndWait()

talk('Hello, I am Alexa, your personal companion.')


while 1:
    attentionCalled = listen("I'm listening waiting for you to call my attention...")
    if attentionCalled == "hey alexa":
        # let user pick an action/command
        # action #1 -- manage user records
        # action #2 -- ping a website
        prompt=attn
        talk(attn)
        talk('Do you want to manage a record')
        talk('or Do you want to Ping a Website')
        talk(attn2)
        
        
        command_list = ['record','ping a website']
        command = ''

        while command not in command_list:
            command = listen(prompt)
        
            if command == "record":
            #code here for user management
                talk("I am managing you user records.")
                employee = []
                talk('How many records to enter')

                record = say('How many records to enter: ')
                say(record)
                record = w2n.word_to_num(record)
                print(record)
                talk(record)
                os.system('cls||clear')
                record1 ={'fname':'','lname':'','account':''}


                for i in range(record):
                    os.system('cls||clear')
                    record1 ={'fname':'','lname':'','accountNo':''}
        
                    talk('What is your First name')
                    record1['fname']=say('What is your First name')
                

        
                    talk('What is your Last name')
                    record1['lname']=say('What is your Last name')
        
                    talk('What is your Account Number')
                    record1['accountNo']=say('What is your Account Number')
                    employee.append(record1)
                    os.system('cls||clear')
                talk('Printing List of Employees')
                print('Printing List of Employees:')

                for x in employee:
                    # talk('Printing List of Employees')
                    print(x['fname'],x['lname'],x['accountNo'])

                    z1 = x['fname']
                    z2 = x['lname']
                    z3 = x['accountNo']
                    talk(z1)
                    talk(z2)
                    talk(str(z3))
                
                talk('All Records has been saved. Thank you')
            elif command == "ping a website":
                #code here for pinging
                # talk("I am pinging a website.")
            
                talk("What is the ip address")
                ipaddress = say("What is the ip address")
                print("Pinging IP address, please wait...")
                host=ping(ipaddress,count=10, interval=0.2)
                if host.is_alive==True:
                    print("Website is reachable")
                    talk("Website is reachable!")
                    print("The minimum round-trip time is "+ str(host.min_rtt) + " with the average round-trip time of " + str(host.avg_rtt) + " and maximum round-trip time of "+ str(host.max_rtt))
                    talk("The minimum round-trip time is "+ str(host.min_rtt) + " with the average round-trip time of " + str(host.avg_rtt) + " and maximum round-trip time of "+ str(host.max_rtt))
                    print("I Alexa, sent "+ str(host.packets_sent) + " and received total of " + str(host.packets_received) + " packets. As I computed there is a total of "+ str(host.packet_loss) + " packet loss.")
                    talk("I, Alexa, sent "+ str(host.packets_sent) + " and received total of " + str(host.packets_received) + " packets. As I computed there is a total of "+ str(host.packet_loss) + " packet loss.")    

                elif host.is_alive==False:
                    print("Website is UNREACHABLE!")
                    talk("Website is UNREACHABLE!")
                    pass
                else:
                    print("Error Error")
                    os.system('cls')    
            else:
                talk("Still waiting for your command for me to make an action")






