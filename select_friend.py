#importing default profie
from default_spy_detail import spy, Spy, ChatMessage, friends

#create select_a_friend function to choose from them
def select_a_friend():
    item_number = 0

    #show all the friends
    for friend in friends:
        print "%d. %s %s. Age %d and rating %.2f is online" % (item_number +1, friend.salutation, friend.name,friend.age,friend.rating)
        item_number = item_number + 1

    #choose from the list
    friend_choice = raw_input("Choose from above Friends : ")
    friend_choice_position = int(friend_choice) - 1
    return friend_choice_position