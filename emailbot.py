import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage


listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():

    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()

    except:
        pass

def send_email(receiver, subject, message):

    server = smtplib.SMTP('smtp@gmail.com', 587)
    server.starttls()
    server.login('paramveer*****@gmail.com', '********')

    email = EmailMessage()

    email['From'] = 'paramveermarwahafc@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject

    email.set_content(message)

    server.sendmail(email)

email_list = {
    'jenny' : 'jennymarwaha@gmail.com',
    'lisa' : 'paramveermarwah214@gmail.com'
}

def get_email_info():
    talk("Who you wish to send the email?")
    name = get_info()

    receiver = email_list[name]
    print(receiver)

    talk("What is the subject of your email?")
    subject = get_info()

    talk("What is the body of your email?")
    message = get_info()

    send_email(receiver, subject, message)

get_email_info()

