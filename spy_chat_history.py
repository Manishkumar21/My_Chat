# importing different files and their function like select friend file, add_friend function, datetime function
# and color

import sys
from termcolor import colored
from select_friend import select_a_friend
from add_friend import friends
from datetime import datetime
import time

#creating read_chat_history to show all the chating history
def read_chat_history():

    read_for = select_a_friend()

    #creating variable "now" in which current datetime function is stored
    now = datetime.now()

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            #it is showing the chat history with the date and time

            #it will show the date
            a = now.strftime("%b %d, %Y ")
            #it will show the time
            b = now.strftime("%H:%M:%S ")

            #change the color of date
            text = colored(a,'red')
            #change the color of the time
            text1 = colored(b, 'blue')
            text2 = (text + "at "+ text1)

            #change the color of the user
            d = colored(chat.message,"green")
            #change the color of the Message
            c = colored(friends[read_for].name,"cyan")
            print ("\n\n\t\t\t****" +text2+ "%s said: [%s] ****") %(c,d)


            # text = colored('Hello, World!', 'blue', attrs=['reverse', 'blink'])
            # print(text)