# import datetime function from library so we can use current date and time.
from datetime import datetime

# defining or creating a class
class Spy:

    # creating the constructor using __init__
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

# creating chat class where we can store the all chats with your friends.
class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
# default user
spy = Spy('Manish', 'Mr.', 21, 4.7)

#default friend
my_friend = Spy('Manu', 'Mr.', 21,4.1)

#friend list where all friends are going to store.
friends = [my_friend]
