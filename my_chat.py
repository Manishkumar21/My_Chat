# importing different files and their functions like default user profile, validation file, spy_choice file,
    # datetime function from library and Steganography after installing it in the sysyem

from default_spy_detail import spy, Spy, ChatMessage, friends
import sys
from termcolor import colored
from spy_choice import choice
from steganography.steganography import Steganography
from datetime import datetime


#spychat Application starts from here
text = colored("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t****Welcome to SpyChat Application****\n","blue")
print text

# Ask want to continue as stored user or want to create new profile
menu = "\t\t\t\t*****Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? ****"
choice1 = raw_input(menu)

# if you agreed with saved profile than
if str.upper(choice1) == "Y":
    choice(spy)

# if you want a new profile
elif str.upper(choice1) == "N":
    # clearing the stored profile
    spy = Spy("","",0,0.0)
    spy.name = raw_input("\n\t\tEnter Your Name : ")
    if len(spy.name) > 0:

        # validation on name
        spy.salutation = raw_input("\nPlease define your Gender.\n\t1.\tMale(M) \n\t2.\tFemale(F)\n\t\t")
        if spy.salutation.upper() == "M" or spy.salutation == "1":
            spy.name = ("Mr." + " " +spy.name)
            spy.name = spy.name.upper()
            print ("\n\t\t****Welcome %s ****"%spy.name)
        elif spy.salutation.upper() == "F" or spy.salutation == "2":
            spy.name = ("Miss." + "  "+ spy.name)
            spy.name = spy.name.upper()
            print ("\n\t\t****Welcome %s ****" % spy.name)
        else:
            print("\n\t\t\t****Please Enter valid options. (-_-)****")
            exit(0)

        # validation on age
        spy.age = raw_input("\tEnter your Age : ")
        if len(spy.age) > 0:
            spy.age = int(spy.age)
            if (spy.age > 12 and spy.age < 50):
                print ("\n\t\t****Oh! Great %s . You can give us Rating****" % spy.name)
                spy.rating = float(raw_input("\tPlease give Rating i.e ( 0-5) : "))
            elif (spy.age > 50):
                print ("\n\t\t****Sorry. You are Older to become a spy. (-_-) ****")
            elif (spy.age < 12):
                print ("\n\t\t****Sorry. You are not eligible to become a spy. (-_-) ****")
            else:
                print ("\n\t\t****Sorry. You entered wrong Input. (-_-) ****")

            # validation on rating
            spy.age = int(spy.age)
            if (spy.age > 12 and spy.age < 50):
                if spy.rating > 4.5 and spy.rating <= 5.0:
                    print (
                        "\n\n\t****With the rating of %s .You have done an Excellent Job. Keep it up.**** " % spy.rating)
                    print ("Authentication Complete.\n\tWelcome " + spy.name + ". \t Age : " + str(spy.age)
                           + ". \t And rating : " + str(spy.rating) + ".\n\t\t**** You are in Our Team.****")
                    spy.is_online = True
                    choice(spy)
                elif (spy.rating > 3.5 and spy.rating <= 4.5):
                    print (
                        "\n\n\t****With the rating of %s You have done good Job. But there is scope of Improvement.**** " % spy.rating)
                    print ("Authentication Complete.\n\tWelcome " + spy.name + ". \t Age : " + str(spy.age)
                           + ". \t And rating : " + str(spy.rating) + ".\n\t\t**** You are in Our Team.****")
                    spy.is_online = True
                    choice(spy)
                elif (spy.rating >= 2.5 and spy.rating <= 3.5):
                    print ("\n\n\t****With the rating of %s You can do better than this.**** " % spy.rating)
                    print ("Authentication Complete.\n\tWelcome " + spy.name + ". \t Age : " + str(spy.age)
                           + ". \t And rating : " + str(spy.rating) + ".\n\t\t**** You are in Our Team.****")
                    spy.is_online = True
                    choice(spy)
                elif (spy.rating < 2.5):
                    print ("\n\n\t\t****We are so sorry you are not elligible for this. (-_-)**** ")
                elif (spy.rating > 5.0):
                    print ("\n\n\t\t****%s Rating is not Available. (-_-)**** " % spy.rating)
                else:
                    print ("\n\n\t\t****You have entered wrong Input. (-_-)**** ")
        else:
            print "\n\tPlease Enter your Age First (-_-)"
    else:
        print ("\n\tPlease Enter your Name first. (-_-)")