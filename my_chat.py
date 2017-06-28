# importing different files

from default_spy_detail import spy, Spy, ChatMessage, friends
from spy_name_validation import name_validation, age_validation, rating_validation
from spy_choice import choice
from steganography.steganography import Steganography
from datetime import datetime

# importing ends

#s pychat Application starts from here
print("\n\t\t****Welcome to SpyChat Application****\n")

# Ask want to continue as stored user or want to create new profile
menu = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
choice1 = raw_input(menu)

# if you agreed with saved profile than
if str.upper(choice1) == "Y":
    choice(spy)

# if you want a new profile
elif str.upper(choice1) == "N":
    # clearing the stored profile
    spy = Spy("","",0,0.0)
    spy.name = raw_input("Enter Your Name : ")
    if len(spy.name) > 0:
        
        # validation on name
        spy.salutation = raw_input("Please define your Gender.\n\t1.\tMale(M) \n\t2.\tFemale(F)\n\t\t")
        if spy.salutation.upper() == "M" or spy.salutation == "1":
            spy.name = ("Mr." + " " +spy.name)
            spy.name = spy.name.upper()
            print ("\t\t****Welcome %s ****"%spy.name)
        elif spy.salutation.upper() == "F" or spy.salutation == "2":
            spy.name = ("Miss." + "  "+ spy.name)
            spy.name = spy.name.upper()
            print ("\t\t****Welcome %s ****" % spy.name)
        else:
            print("Please Enter valid options. (-_-)")
            exit(0)

        # validation on age
        spy.age = raw_input("Enter your Age : ")
        if len(spy.age) > 0:
            spy.age = int(spy.age)
            if (spy.age > 12 and spy.age < 50):
                print ("\t\t****Oh! Great %s . You can give us Rating****" % spy.name)
                spy.rating = float(raw_input("Please give Rating i.e ( 0-5) : "))
            elif (spy.age > 50):
                print ("\t\t****Sorry. You are Older to become a spy. (-_-) ****")
            elif (spy.age < 12):
                print ("\t\t****Sorry. You are not eligible to become a spy. (-_-) ****")
            else:
                print ("\t\t****Sorry. You entered wrong Input. (-_-) ****")

            # validation on rating
            spy.age = int(spy.age)
            if (spy.age > 12 and spy.age < 50):
                if spy.rating > 4.5 and spy.rating <= 5.0:
                    print (
                        "\n\t****With the rating of %s .You have done an Excellent Job. Keep it up.**** " % spy.rating)
                    print ("Authentication Complete.\n\tWelcome " + spy.name + ". \t Age : " + str(spy.age)
                           + ". \t And rating : " + str(spy.rating) + ".\n\t\t**** You are in Our Team.****")
                    choice(spy)
                elif (spy.rating > 3.5 and spy.rating <= 4.5):
                    print (
                        "\t****With the rating of %s You have done good Job. But there is scope of Improvement.**** " % spy.rating)
                    print ("Authentication Complete.\n\tWelcome " + spy.name + ". \t Age : " + str(spy.age)
                           + ". \t And rating : " + str(spy.rating) + ".\n\t\t**** You are in Our Team.****")
                    choice(spy)
                elif (spy.rating >= 2.5 and spy.rating <= 3.5):
                    print ("\t****With the rating of %s You can do better than this.**** " % spy.rating)
                    print ("Authentication Complete.\n\tWelcome " + spy.name + ". \t Age : " + str(spy.age)
                           + ". \t And rating : " + str(spy.rating) + ".\n\t\t**** You are in Our Team.****")
                    choice(spy)
                elif (spy.rating < 2.5):
                    print ("\t\t****We are so sorry you are not elligible for this. (-_-)**** ")
                elif (spy.rating > 5.0):
                    print ("\t\t****%s Rating is not Available. (-_-)**** " % spy.rating)
                else:
                    print ("\t\t****You have entered wrong Input. (-_-)**** ")
                    spy.is_online = True
        else:
            print "\n\tPlease Enter your Age First (-_-)"
    else:
        print ("\n\tPlease Enter your Name first. (-_-)")