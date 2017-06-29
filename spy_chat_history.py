# importing different files and their function like select friend file, add_friend function, datetime function

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
            now = now.strftime("%b %d, %Y at %H:%M:%S")
            print (now + "%s said: [%s] ") % (friends[read_for].name, chat.message)