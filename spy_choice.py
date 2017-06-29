# importing different files and their function like default user profile, status of the spy, add_friend function,
# send secret message function, chat history function

from default_spy_detail import spy, Spy, ChatMessage, friends
from spy_status import add_status
from add_friend import add_friend
from send_secret_message import send_message
from read_secret_message import read_message
from spy_chat_history import read_chat_history

#pre stored status messages
STATUS_MESSAGES = ["My name is Manish", "Change The GamE"]

#ask user what he/she want to do
def choice(spy):

    spy.name = spy.salutation + " " + spy.name
    if spy.age > 12 and spy.age < 50:
        show_menu = True
        while show_menu:
            choices = ("\n\t**Select from below action (1-6) what do you want.\n\t\t1.\tAdd Status.\n\t\t2.\tAdd Friend.\n\t\t3.\tSend Message.\n\t\t4.\tRead Message."
              "\n\t\t5.\tRead Older Chat\n\t\t6.\tClose Application.")
            menu_choice = raw_input(choices)

            #if user enter something
            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                #if user press 1
                if menu_choice == 1:
                    print "\t****Please Add Your Thoughts With Us****"
                    updated_status_message = None
                    #add status function is called
                    spy.current_status_message = add_status(STATUS_MESSAGES)

                #if user press 2
                elif menu_choice == 2:
                    print "\t****Enter the details of your Friend****"
                    # add friend function is called
                    number_of_friends = add_friend()
                    print("Now You Have Total Friends = %d" % number_of_friends)

                # if user press 3
                elif menu_choice == 3:
                    # send message function is called
                    send_message()

                # if user press 4
                elif menu_choice == 4:
                    # read message function is called
                    read_message()

                # if user press 5
                elif menu_choice == 5:
                    # read_chat_history function is called
                    read_chat_history()

                # if user press 6
                elif menu_choice == 6:
                    #it will close the application
                    print "\t****Thank you. Its honor to have you with Us****"
                    exit(0)
                # elif menu_choice == 7:
                #     delete(friends)

                # if user press anything else
                else:
                    show_menu = False

    # if user press nothing
    else:
        print ("Sorry. You entered wrong Input. (-_-) ")