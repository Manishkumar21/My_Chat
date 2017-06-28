from default_spy_detail import spy, Spy, ChatMessage, friends
from spy_choice import choice
def name_validation():
    if len(spy.name) > 0:
        spy.salutation = raw_input("Please define your Gender.\n\t1.\tMale(M) \n\t2.\tFemale(F)\n\t\t")
        if spy.salutation.upper() == "M" or spy.salutation == "1":
            spy.name = ("Mr." + " " +spy.name)
            spy.name = spy.name.upper()
            print ("Welcome %s "%spy.name)
        elif spy.salutation.upper() == "F" or spy.salutation == "2":
            spy.name = ("Miss." + "  "+ spy.name)
            spy.name = spy.name.upper()
            print ("Welcome %s " % spy.name)
        else:
            print("Please Enter valid options. (-_-)")
            exit(0)
    else:
        print ("\n\tPlease Enter your Name first. (-_-)")

def age_validation():
    spy.age = int(spy.age)
    if (spy.age > 12 and spy.age < 50):
        print ("\t\t****Oh! Great %s . You can give us Rating****" % spy.name)
        spy.rating = float(raw_input("Please give Rating i.e ( 0-5) : "))
        return (spy.rating)
    elif (spy.age > 50):
        print ("Sorry. You are Older to become a spy. (-_-) ")
    elif (spy.age < 12):
        print ("Sorry. You are not eligible to become a spy. (-_-) ")
    else:
        print ("Sorry. You entered wrong Input. (-_-) ")

def rating_validation():
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
            print ("We are so sorry you are not elligible for this. (-_-) ")
        elif (spy.rating > 5.0):
            print ("%s Rating is not Available. (-_-) " % spy.rating)
        else:
            print ("You have entered wrong Input. (-_-) ")
        spy.is_online = True

    # if len(spy.name) > 0:
    #     spy.salutation = raw_input("Please define your Gender ?\n\t1.\tMale(M) \n\t2.\tFemale(F)\n\t\t")
    #     spy.age = raw_input("Enter your Age : ")
    #     spy.age = int(spy.age)
        print ("\t\t****Oh! Great %s . You can give us Rating****" % spy.name)
        spy.rating = raw_input("Please give Rating i.e ( 0-5) : ")
        spy.rating = float(spy.rating)
        choice(spy)
    # else:
    #     print "Please add a valid spy name"