from default_spy_detail import spy, Spy, ChatMessage, friends
def add_friend():

    new_friend = Spy('','',0,0.0)

    new_friend.name = raw_input("Please add your friend's Good Name : ")
    new_friend.salutation = raw_input("Specify the Gender.\n\t1.\tMale \n\t2.\tFemale\n\t\t ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Enter your Age : ")
    new_friend.age = int(new_friend.age)

    print ("\t\t****Oh! Great. Give us Rating****")
    new_friend.rating = raw_input("Please give Rating of your Friend from ( 0-5) : ")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= 2.0:
        friends.append(new_friend)
        print "\t****1(ONE) Friend Added Sucessfully****"
    else:
        print "Sorry! Invalid Input. We can't add Spy.\n\t\t****Thank You****"

    return len(friends)