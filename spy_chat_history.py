from select_friend import select_a_friend
from add_friend import friends
def read_chat_history():

    read_for = select_a_friend()

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)