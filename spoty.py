#import modules

import pyttsx3                                                      #for getting voices
import datetime                                                     #for fetching time
import speech_recognition as sr                                     #for getting voice as output
import wikipedia                                                    #to fetch wikipedia
import webbrowser                                                   #to use webbrowser
import os                                                           #to operate operations related to os
import smtplib                                                      #for sending mail via google mails
import random                                                       #to select random values from the given input
import cv2                                                          #for camera operation
import wmi                                                          #for brightness and screen controll operations,temprature fetching
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume        #for controlling volume settings
import psutil
import time                                                         #for time functions
from datetime import date                                           #for date


#get voices 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


#voices[0].id is a male voice and voices[1].id is a female voice
# print(voices[0].id)

#setting the voice 
engine.setProperty('voice',voices[1].id)



#mail collection,the reciever mail should be mentioned here 
mails = {"name1":"email1@gmail.com",
    "name2":"email2@gmail.com"
    
}


#speak function ,speakes evrything which is passes as a parameter
def speak(audio): 
    engine.say(audio)
    engine.runAndWait()



#wish function ,it wishes according to the time 
def wish():
    hour = int(datetime.datetime.now().hour)
    
    speak("hello          i am spotty")

    print("please identify yourself")
    speak("please identify yourself")
    identity = take_command()

    if "open" in identity:
        pass
        
    else:
        print("i am sorry you are not authorised...  autentication required.")
        speak("i am sorry you are not authorised  autentication required.")
        print("quitting")

        speak("terminating the program")
        quit()

    # print(hour)
    if hour >= 0 and hour <= 12:
        print("Good morning sir")
        speak("Good morning sir")

    elif hour >= 12 and hour <= 16:
        print("Good afternoon sir")
        speak("Good afternoon sir")

    else:
        print("Good evening sir")
        speak("Good evening sir")


    
        
    print(" please tell me how may i help you")
    speak(" please tell me how may i help you")    


#mail function,it uses smtp mail module and send mail when called .

'''

DONT SHOW MAIL PART 
PASSWARD AND MAIL ID INCLUDED
ACCESS DENIED


'''
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'passward')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


#take_command function which takes commands from the user 
def take_command():
   while True:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            r.energy_threshold =10000
            audio = r.listen(source)
        try:
            print("recognizing...")
            query = r.recognize_google(audio,language='en-in')
            print("user said:"+query)
            #speak("user said:"+query)
            return query
        #except Exception as e:
        except Exception:
            speak("dint get it. will you please sat that again")
            #return "none"    

   


#main function 


if __name__ == "__main__":
    
    
    
    
    #wishes function called to wish the user and intruduce the program
    wish()
    


    #while loop so that the program can run in a loop
    while True:


        # #try to avoid exceptions and print them when needed
        # try:

            #statement to take the input from user and save it a variable query so that we can use it anytime we want
            query = take_command().lower()
            try:
                if 'wikipedia' in query:
                    speak('searching wikipedia...')
                    print("searching...")
                    #  query = query.replace("wikipedia","")


                    #statement to fetch wikipedia and print 2 lines
                    results = wikipedia.summary(query,sentences=2)
                    speak("according to wikipedia")
                    print(results)
                    speak(results)
            except Exception:
                    speak("cannot find proper information")   
                    take_command()   
                   
                   
                   
                   
                   
            if 'open youtube' in query:
                    print("opening youtube...")
                    speak("opening youtube...")
                    webbrowser.open('youtube.com')

            

            elif 'open google' in query:
                    print("opening google...")
                    speak("opening google...")
                    webbrowser.open('google.com') 
            

            elif 'open watsapp' in query:
                    print("opening whats app...")
                    speak("opening whats app...")
                    webbrowser.open('whatsapp.com') 
            
            elif 'open instagram' in query:
                    print("opening instagram...")
                    speak("opening instagram...")

                    webbrowser.open('instagram.com') 

            elif 'play music' in query:
                print("playing music...")
                speak("playing music...")
                music_dir = '\\Users\\HP\\Desktop\\folders\\music'
                

                #list the songs in the file
                songs=os.listdir(music_dir)
                print(songs)

                #chooses random song from the list of songs by calculating the length of list of songs
                n=random.randint(0,len(songs)-1)
                os.startfile(os.path.join(music_dir,songs[n]))
                        
            elif 'time' in query:
                    time=datetime.datetime.now()
                    print(time)

                    #convert time to any parameter you want like min ,hour ,year etc
                    hour = time.hour
                    min = time.minute
                    secs = time.second
                    speak(f"the time is{hour}hours{min}minutes{secs}seconds")
                    print(f"time = {hour}:{min}:{secs}")


            elif 'open code' in query:
                    print("opening visual studio code...")
                    speak("opening visual studio code...")
                    codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)


            elif 'open pycharm' in query:
                    print("opening pycharm...")
                    speak("opening pycharm...")
                    pycharm = "C:\\Users\\HP\\Desktop\\folders\\tools\\JetBrains PyCharm Community Edition 2019.2.1 x64.lnk"
                    os.startfile(pycharm)
            

            elif 'open code blocks' in query:
                    print("opening codeblocks...")
                    speak("opening codeblocks...")
                    code_block = "C:\\Users\\HP\\Desktop\\folders\\tools\\CodeBlocks.lnk"
                    os.startfile(code_block)


            


            elif 'open chrome' in query:
                    print("opening chrome...")
                    speak("opening chrome...")
                    chrome = "C:\\Users\\HP\\Desktop\\folders\\others\\Google Chrome.lnk"
                    os.startfile(chrome)

                

            

            
            elif 'increase brightness'  in query:

                    #parameter to set brightness
                    brightness = 100 # percentage [0-100]
                    c = wmi.WMI(namespace='wmi')

                    methods = c.WmiMonitorBrightnessMethods()[0]
                    methods.WmiSetBrightness(brightness, 0)
                    print("brightness increased")
                    speak("brightness increased")

            elif 'decrease brightness'  in query:
                    brightness = 0 # percentage [0-100]
                    c = wmi.WMI(namespace='wmi')

                    methods = c.WmiMonitorBrightnessMethods()[0]
                    methods.WmiSetBrightness(brightness, 0)
                    print("brightness decreased")
                    speak("brightness decreased")


            elif 'decrease volume'  in query:
                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(
                IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                volume = cast(interface, POINTER(IAudioEndpointVolume))
                
                # Control volume
                #volume.SetMasterVolumeLevel(-0.0, None) #max
                #volume.SetMasterVolumeLevel(-5.0, None) #72%
                volume.SetMasterVolumeLevel(-20.0, None) #51%
                print("volume decreased")
                speak("volume decreased")

            elif 'increase volume'  in query:
                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(
                IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                volume = cast(interface, POINTER(IAudioEndpointVolume))
                
            
                volume.SetMasterVolumeLevel(-0.0, None) #max
                print("volume increased")
                speak("volume increased")



            


            elif 'open movies' in query:
                    print("opening movies...")
                    speak("opening movies...")
                    movies_Path = 'E:\\'
                    
                    os.startfile(movies_Path)
                #     speak("which movie u want to watch sir!!!")
                #     movie_name = take_command()
                #     print(movie_name)
                #     movie_list = os.listdir(movies_Path)
                    
                
                #    # print(movie_list)
                #     try:
                #         for i in movie_list:
                #             if movie_name in i:
                            
                #                 os.startfile("E:\\"+movie_name)

                    

                #     except Exception as e:
                #         speak("movie not found")
                        
            elif 'open internet settings' in query:
                print("opening settings...")
                speak("opening settings...")
                os.system('control.exe Inetcpl.cpl')
                        
                        
            


            elif 'shutdown computer' in query:
                print("do you want to shutdown computer sir..? say yes if you want to")
                speak("do you want to shutdown computer sir..? say yes if you want to")
                shutdown =take_command()
                try:
                   # if 'yes' or 'do it' or 'yea' in shutdown:  =>this makes the program go wrong and then the progran 
                   #shuts down the computer even if u say no so use only one word as a key for proper functioning.
                    if 'yes' in shutdown:
                        print("shutting down the computer...")
                        speak("shutting down the computer...")
                        os.system("shutdown /s /t 1")
                except Exception:
                    
                    print("shutdown process terminated..")
                    speak("shutdown process terminated..")
                    break


            elif 'restart computer' in query:
                speak("do you want to restart computer sir..? say yes if you want to")
                restart =take_command()
                try:
                    if 'yes'  in restart:
                        print("restarting the computer...")
                        speak("restarting the computer...")
                        os.system("shutdown /r /t 1")  
                except Exception:
                    print("restart process terminated..")
                    speak("restart process terminated..")
                    break
            
    

            elif 'sleep screen' in query:
                print("going to sleep good night...")
                speak("going to sleep good night...")
                os.system(r'%windir%\system32\rundll32.exe powrprof.dll,SetSuspendState Sleep')  
                #replace sleep with hyberante for hybernating the screen


            elif 'mail' in query:
                    try:

                        #takes input from user and checks whom to send mail from dictionary provided above
                        print("whom to send")
                        speak("whom to send")
                        re=take_command().lower()
                        to = mails[re] 

                        speak("What should I say?")
                        content = take_command()
                        
                        sendEmail(to, content)
                        print(f"reciever{to}")
                        print(f"message{content}")

                        print("Email has been sent!")
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        print("not able to send email..check wheather the reciever is there on list...")
                        speak("not able to send email..check wheather the reciever is there on list...")


            



            elif 'open this pc' in query:
                    print("opening this pc...")
                    speak("opening this pc...")
                    home = "C:\\Users\\HP\\Desktop\\folders\\tools\\This PC - Shortcut.lnk"
                    os.startfile(home)            


            elif 'open camera' in query:
                print("opening camera...")
                speak("opening camera...")
                print("press escape to quit")
                speak("press escape to quit")

                cv2.namedWindow("preview")
                vc = cv2.VideoCapture(0)

                if vc.isOpened(): # try to get the first frame
                    rval, frame = vc.read()
                else:
                    rval = False

                while rval:
                    cv2.imshow("preview", frame)
                    rval, frame = vc.read()
                    key = cv2.waitKey(20)
                    if key == 27: # exit on ESC
                        break
                        
                    
                #closes the camera window
                cv2.destroyWindow("preview")
                print("you look great...")
                speak("you look great...")


            elif 'battery status'  in query:
                
                
                battery = psutil.sensors_battery()
                plugged = battery.power_plugged
                percent = str(battery.percent)
                if plugged==False: plugged="Not Plugged In"
                else: plugged="Plugged In"
                print(f"battery status:{percent}'% | '{plugged}")
                speak(percent+'% | '+plugged) 

            elif '*' in query:
                speak("uhh .!! that was rude...please dont use bad words")

            

            elif 'how are you' in query:
                speak("i am good, how about you")
                x=take_command()
                speak("thats great..may i know what can i do for you")
                take_command()

            elif 'wait' in query:
                time.sleep(15)
                # for i in range(15):
                #     print(i)
                #     time.sleep(1)

                speak("hello sir..may i do anything for you..?")

            elif  'updates' in query:

                today_int=datetime.datetime.today().weekday()  #it will give you an integer value as output from 
                #which you can get weekday with help of dict
    
   
                #weekdays dict
                weekdays={
                    0:"monday",
                    1:"tuesday",
                    2:"wednesday",
                    3:"thursday",
                    4:"friday",
                    5:"saturday",
                    6:"sunday"

                }


                #print(weekdays[today_int])
                current_events="current events"    #passing it as input to wikipedia
                time=datetime.datetime.now()
                todays_date={time.year}-{time.month}-{time.day}
                w = wmi.WMI(namespace="root\\wmi")
                temperature_info = w.MSAcpi_ThermalZoneTemperature()[0]
                temprature = (temperature_info.CurrentTemperature/10)-273
                print(f"time = {time.hour}:{time.minute}:{time.second}")
                speak(f"well It's a good day and the time is{time.hour}hours{time.minute}minutes{time.second}seconds")
                print(f"date ={time.year}-{time.month}-{time.day}")
                print(f"weekday= {weekdays[today_int]}")
                speak(f"and the date is{todays_date} that is{weekdays[today_int]}") 
                speak(f"and the temprature now is around{temprature} degree celcius")
                speak(f"and the main current news are {wikipedia.summary(current_events,sentences=3)}")
                
               # speak(f"and the temprature is{cpu.temprature()}")




            elif 'quit' in query:
                speak("terminating the program")
                print("quitting...")
                quit()
            
        # except Exception as e:
        #     print(e)
        #     speak("oops!!!something went wrong")

            
   



    
    
