from default_spy_detail import spy, Spy, ChatMessage, friends
from spy_choice import choice
from steganography.steganography import Steganography
from datetime import datetime

print("\n\t\t****Welcome to SpyChat Application****\n")
menu = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
choice1 = raw_input(menu)

if str.upper(choice1) == "Y":
    choice(spy)
elif str.upper(choice1) == "N":
    spy = Spy("","",0,0.0)
    spy.name = raw_input("Enter Your Name : ")
    if len(spy.name) > 0:
        spy.salutation = raw_input("Please define your Gender ?\n\t1.\tMale(M) \n\t2.\tFemale(F)\n\t\t")
        spy.age = raw_input("Enter your Age : ")
        spy.age = int(spy.age)
        print ("\t\t****Oh! Great %s . You can give us Rating****" % spy.name)
        spy.rating = raw_input("Please give Rating i.e ( 0-5) : ")
        spy.rating = float(spy.rating)
        choice(spy)
    else:
        print "Please add a valid spy name"