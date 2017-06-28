from default_spy_detail import spy, Spy, ChatMessage, friends
def select_a_friend():
    item_number = 0

    for friend in friends:
        print "%d. %s %s. Age %d and rating %.2f is online" % (item_number +1, friend.salutation, friend.name,friend.age,friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from above Friends : ")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position