import wolframalpha
import pyttsx3
import webbrowser
import speech_recognition as sr
import wikipedia
import os
import datetime
import time
import subprocess
from winsound import PlaySound, SND_FILENAME
from googletrans import Translator
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from tkinter import *
import pyautogui as pya
import pyperclip
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


engine = pyttsx3.init()
David = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
engine.setProperty('rate', 130)
engine.setProperty('volume', 1.0)
engine.setProperty('voice', David)




class jarvis():

    global My_command,emailsend,activate,playmusic,translation,query,audio,record
    query = ""

    def soundeffect(self,sound):
        PlaySound(sound, SND_FILENAME)

    def speak(self,audio):
        print("Jarvis: " + audio)
        engine.say(audio)
        engine.runAndWait()

    def news(self):

        news_url = "https://news.google.com/news/rss"
        Client = urlopen(news_url)
        xml_page = Client.read()
        Client.close()
        soup_page = soup(xml_page, "xml")
        news_list = soup_page.findAll("item")
        for news in news_list[:5]:
            jarvis().speak(news.title.text)

    def My_command(self):

        jarvis().soundeffect("PremiumBeat_0013_cursor_click_06.wav")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

            try:
                query = r.recognize_google(audio)
                print('user: ', query)
                return query

            except:
                jarvis().soundeffect("somthing wrong.wav")
                jarvis().speak("sorry sir! \n I didn\'t get that! \n Can you speak again")


    def emailsend(self):
        sender = 'bigbang7434@gmail.com'
        password = "601701801"
        jarvis().speak('who is the receiver ?')
        # darling="zeecool401@gmail.com"
        email_reciever = My_command(self)
        # reciever="zeecool401@gmail.com"
        if "darling" in email_reciever or "Darling" in email_reciever or "baby" in email_reciever:
            reciever = "zeecool401@gmail.com"
            jarvis().speak("what is the subject?")
            subject = My_command(self)
            jarvis().speak("what is content sir?")
            content = My_command(self)

            msg = MIMEMultipart()  # instance of class (create object named "msg")
            msg['From'] = sender
            msg['To'] = reciever
            msg['Subject'] = subject
            msg.attach(MIMEText(content, 'plain'))

            # attachement in gmail(.txt,.png,.jpg etc.)
            jarvis().speak("do you want to attache any file: ")
            ask_for_file = My_command(self)
            if (ask_for_file == "yes"):
                jarvis().speak("what is the name of file sir?")
                file_name = My_command(self) + ".png"
                file_location = "C:\\Users\AMD\PycharmProjects\zahidkvy\personal_assistant\\" + file_name  # file_location example: D:\pythonman\pythonimage.png
                # example: pyhonimage.png

                attachment = open(file_location, "rb")
                p = MIMEBase('application', 'octet-stream')
                p.set_payload((attachment).read())
                encoders.encode_base64(p)
                p.add_header('Content-Disposition', "attachment; filename= %s" % file_name)
                msg.attach(p)  # attached file into msg

            server = smtplib.SMTP('smtp.gmail.com', 587)  # make server
            server.starttls()
            server.login(sender, password)
            text = msg.as_string()  # convert object into string
            server.sendmail(sender, reciever, text)
            jarvis().speak("email send.")
            server.quit()

        else:
            jarvis().speak("this email is not exist")
            self.emailsend(self)

    global des_lang
    des_lang = {
        "English": 'en',
        'Hindi': 'hi',
        'French': 'fr',
        'Spanish': 'es',
        'Japanese': 'ja',
        'Russian': 'ru',
        'Italian': 'it'
    }


    def copy_clipboard(self):
        pya.hotkey('ctrl', 'c')
        time.sleep(.01)
        return pyperclip.paste()

    global cleint
    app_id = 'VLKT3H-GWWK8HYR69'
    cleint = wolframalpha.Client(app_id)
    file_location = ''
    file_name = ''

    des_lang = {
        "English": 'en',
        'Hindi': 'hi',
        'French': 'fr',
        'Spanish': 'es',
        'Japanese': 'ja',
        'Russian': 'ru',
        'Italian': 'it'
    }




    def playmusic(self):
        music_folder = 'D:\python program\scifi sound effect\PB - Sci-Fi UI Free SFX\PremiumBeat SFX'
        jarvis().speak('Which song do you want to listen')
        song = My_command(self)
        jarvis().speak("here is your song\n Enjoy")
        PlaySound(music_folder + "\\" + song + ".wav", SND_FILENAME)

    def translation(self):
        translator = Translator()
        self.speak("In which language do you want to translate?")
        de = My_command(self)
        self.speak("ok speak something")
        text = My_command(self)
        trans = translator.translate(text, dest=des_lang[de]).text
        self.speak(trans)

    def greeting(self):
        self.soundeffect("PremiumBeat_0013_cursor_click_06.wav")
        command = "C:\Program Files\Rainmeter\Rainmeter.exe"

        self.speak("All the systems are going to start\n I am going online sir \n Internet connection is checked \n Now I am Online sir")
        subprocess.Popen(command)
        jarvis().soundeffect("PremiumBeat_0046_sci_fi_type_beep.wav")
        current_time = datetime.datetime.now().hour
        if (current_time <= 0 and current_time < 12):
            self.speak("good Morning zahid sir")
        elif (current_time >= 12 and current_time < 18):
            self.speak('good afternoon zahid sir')
        else:
            self.speak('good evening zahid sir')
        self.speak('I am jarvis \n your personal assistant ')
        self.speak('at your service ')


    def activate(self):
        got = ''
        me = True
        while me == True:

            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print('Command sir....')
                jarvis().speak('command sir')
                audio = r.listen(source)

                call_jarvis = r.recognize_google(audio)
                print('you said:', call_jarvis)
                if 'alpha' in call_jarvis or "Alpha" in call_jarvis:
                    got = My_command()
                    me = False
                return got

    def myassistant(self):
        self.greeting()

        if __name__ == "__main__":
            jar = True
            file = ''
            f = ''
            while jar == True:

                try:
                    command_query = ""
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        r.adjust_for_ambient_noise(source)
                        print('Next Command sir....')
                        audio = r.listen(source)

                        call_jarvis = r.recognize_google(audio)
                        print('you said:', call_jarvis)
                        if 'alpha' in call_jarvis or "Alpha" in call_jarvis:
                            self.speak("command sir")
                            command_query = My_command(self)
                            query = command_query

                        else:
                            query = self.activate()

                    if "search" in query:
                        jarvis().soundeffect("PremiumBeat_0013_cursor_click_06.wav")

                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            r.pause_threshold = 1
                            r.adjust_for_ambient_noise(source)
                            jarvis().speak('What is your query zahid sir')
                            jarvis().soundeffect( "PremiumBeat_0013_cursor_click_06.wav")
                            audio = r.listen(source)
                            query = r.recognize_google(audio)
                            print('you said:', query)
                            url = query
                            webbrowser.open('https://www.google.com/search?q=%s' % url)
                            self.ids.entry.text = "jarvis: " + str("This is your result zahid sir")
                            jarvis().speak("This is your result zahid sir")


                    elif "shut up" in query or "stop" in query or "sleep" in query or "abort" in query or "by" in query or "shut down" in query:
                        jarvis().speak('ok sir \n have a good day')
                        jar=False



                    elif "YouTube" in query:
                        jarvis().speak("aapka hukum sir")
                        webbrowser.open_new_tab('www.youtube.com')

                    elif "time" in query:
                        now = datetime.datetime.now()
                        self.speak('Current time is %d hours %d minutes' % (now.hour, now.minute))

                    elif "what's up" in query:
                        self.speak("Nothing speacial\n only doing my work sir")

                    elif "how are you" in query:
                        self.speak("I am fantastic sir\n what about you sir?")
                        me=jarvis().My_command(self)
                        if "fine" or "good" or "fantastic" or "same" in me:
                            self.speak("Glad to know sir.")
                        elif "not good" or "sad" in me:
                            self.speak("sorry to know \n you can share with me anything sir.")



                    elif "Facebook" in query:
                        webbrowser.open_new_tab("https://www.facebook.com/?ref=tn_tnmn")
                        jarvis().speak("ye lo sir aapka Facebook")


                    elif "Google" in query:
                        webbrowser.open_new_tab('www.google.com')
                        jarvis().speak("This is your result sir")

                    elif 'hello' in query:
                        jarvis().speak('Hello! sir\n')

                    elif 'text file' in query:
                        file = subprocess.Popen(["notepad",'jarvis.txt'])
                        jarvis().speak("This is your file sir")

                    elif 'text file' in query and 'close' in query:
                        jarvis().speak("Ok sir")
                        os.close(jarvis.txt)

                    elif "headlines" in query or 'headline' in query:
                        self.news()

                    elif "music player" in query:
                        command="C:\Program Files (x86)\VideoLAN\VLC"+"\\"+"vlc.exe"
                        subprocess.Popen(command)

                    elif "start" in query:
                        command="C:\Program Files\Rainmeter\Rainmeter.exe"
                        subprocess.Popen(command)


                    elif "Pagla" in query:
                        jarvis().speak("Haan \n paglaa gaya hai sir")

                    elif 'music' in query or 'Music' in query:
                        playmusic(self)


                    elif "translate" in query:
                        translation(self)

                    elif 'pause' in query:
                        jarvis().speak("Ok sir")
                        PlaySound(None, SND_FILENAME)

                    elif "email" in query or 'gmail' in query or 'Email' in query or 'mail' in query:
                        emailsend(self)

                    elif "read" in query:
                        pya.tripleClick(pya.position())
                        zahid = []
                        var = self.copy_clipboard()
                        zahid.append(var)
                        read= " ".join(zahid)
                        print(read)
                        self.speak(read)

                    elif "copy" in query:
                        pya.tripleClick(pya.position())
                        pya.hotkey('ctrl', 'c')
                        time.sleep(.01)
                        copied=pyperclip.paste()
                        self.speak("copied sir")

                    elif "paste" in query:
                        copy_list=[]
                        copied=pyperclip.paste()
                        copy_list.append(copied)
                        copied_item=" ".join(copy_list)
                        pyperclip.paste()
                        print(pyperclip.paste())
                        self.speak("ok sir\n pasted ")

                    elif "record" in query:
                        jarvis().speak("tell me sir what I record so that I will remember you later.")
                        record=My_command(self)

                    elif "remember" in query:
                        jarvis().speak("you were said: ")
                        jarvis().speak(record)


                    elif "I am" in query or 'my name' in query:
                        jarvis().speak("Hello! dear")

                    elif "where is" in query:
                        data=""
                        jarvis().speak("Ok sir")
                        data=data.split(" ")
                        location=data[2]
                        jarvis().speak("Hold on\n I will show you where "+location+"is.")
                        os.system("chromium-browser https://www.google.nl/maps/place/"+location+"/&amp;")


                    else:
                        query = query
                        my_query = query.lower()
                        try:
                            jarvis().soundeffect("PremiumBeat_0046_sci_fi_type_beep.wav")
                            answer = cleint.query(my_query)
                            res = next(answer.results).text
                            jarvis().speak("ok got it")
                            jarvis().speak(res)

                        except:
                            jarvis().soundeffect("PremiumBeat_0046_sci_fi_type_beep.wav")
                            res = wikipedia.summary(my_query, sentences=2)
                            #self.ids.entry.text = "jarvis: "+str(res)
                            jarvis().speak("got it \n according to Wikipedia")
                            jarvis().speak(res)


                except:
                    # webbrowser.open_new("www.google.com")
                    pass


zahid=jarvis()

#GUI Programming
win=Tk()
win.config(bg='black')
win.title('Jarvis')

label=Label(win)
label.pack()

frame1=Frame(label,relief=SUNKEN,bg="gray15",bd=10)
frame1.pack()

image=PhotoImage(file='haissha.png')

play=Button(frame1,text='Play',bd=5,fg='white',bg='black',font=('arial',15,'bold'),relief=SUNKEN,padx=25,pady=4,command=lambda: zahid.myassistant(),image=image)
play.grid(row=3,column=2,sticky=W)

win.mainloop()
