# import the default_spy_detail file.
from default_spy_detail import spy, Spy, ChatMessage, friends

# defining add_friend function that will add friends to your App.
def add_friend():

    # create a profile for your friend.
    new_friend = Spy('','',0,0.0)

    # using some names validations.
    new_friend.name = raw_input("Please add your friend's Good Name : ")
    if len(new_friend.name) > 0:
        new_friend.salutation = raw_input("Please define your Gender.\n\t1.\tMale(M) \n\t2.\tFemale(F)\n\t\t")
        if new_friend.salutation.upper() == "M" or new_friend.salutation == "1":
            new_friend.name = ("Mr." + " " +new_friend.name)
            new_friend.name = new_friend.name.upper()
            print ("\n\t\t****Your Friend name is %s ****"%new_friend.name)
        elif new_friend.salutation.upper() == "F" or new_friend.salutation == "2":
            new_friend.name = ("Miss." + "  "+ new_friend.name)
            new_friend.name = new_friend.name.upper()
            print ("\n\t\t****Welcome %s ****" % new_friend.name)
        else:
            print("\n\t\t****Please Enter valid options. (-_-)****")
            exit(0)

        # using some age validations.
        new_friend.age = raw_input("Enter your Age : ")
        if len(new_friend.age) > 0:
            new_friend.age = int(new_friend.age)
            if (new_friend.age > 12 and new_friend.age < 50):
                print ("\n\t\t****Oh! Great %s . You can give us Rating****" % new_friend.name)
                new_friend.rating = float(raw_input("Please give Rating i.e ( 0-5) : "))

                # using some Rating validations.
                if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= 2.0:
                    friends.append(new_friend)
                    print "\n\t****1(ONE) Friend Added Sucessfully****"
                else:
                    print "\n\t\tSorry! Invalid Input. We can't add Spy.\n\t\t****Thank You****"
            elif (new_friend.age > 50):
                print ("\n\t\t****Sorry. You are Older to become a spy. (-_-) ****")
            elif (new_friend.age < 12):
                print ("\n\t\t****Sorry. You are not eligible to become a spy. (-_-) ****")
            else:
                print ("\n\t\t****Sorry. You entered wrong Input. (-_-) ****")
        else:
            print "\n\t\t****Please Enter the Age of your Friend (-_-)****\n"

        return len(friends)
    else:
        print "\n\t\t****Please Enter the Name of your Friend (-_-)****"


