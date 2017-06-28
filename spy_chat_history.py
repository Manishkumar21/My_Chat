from select_friend import select_a_friend
from add_friend import friends
from datetime import datetime
from blessings import Terminal
import time
def read_chat_history():

    read_for = select_a_friend()
    now = datetime.now()

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            now = now.strftime("%b %d, %Y at %H:%M:%S")
            print (now + "%s said: [%s] ") % (friends[read_for].name, chat.message)