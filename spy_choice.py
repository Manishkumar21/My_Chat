from default_spy_detail import spy, Spy, ChatMessage, friends
from spy_status import add_status
from add_friend import add_friend
from send_secret_message import send_message
from read_secret_message import read_message
from spy_chat_history import read_chat_history

STATUS_MESSAGES = ["My name is Manish", "Change The GamE"]
def choice(spy):

    spy.name = spy.salutation + " " + spy.name
    if spy.age > 12 and spy.age < 50:
        show_menu = True
        while show_menu:
            choices = ("\n\t**Select from below action (1-6) what do you want.\n\t\t1.\tAdd Status.\n\t\t2.\tAdd Friend.\n\t\t3.\tSend Message.\n\t\t4.\tRead Message."
              "\n\t\t5.\tRead Older Chat\n\t\t6.\tClose Application.")
            menu_choice = raw_input(choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    print "\t****Please Add Your Thoughts With Us****"
                    updated_status_message = None
                    spy.current_status_message = add_status(STATUS_MESSAGES)
                elif menu_choice == 2:
                    print "\t****Select the friend you want to send the Message****"
                    number_of_friends = add_friend()
                    print("Now You Have Total Friends = %d" % number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                elif menu_choice == 6:
                    print "\t****Thank you. Its honor to have you with Us****"
                    exit(0)
                else:
                    show_menu = False
    else:
        print ("Sorry. You entered wrong Input. (-_-) ")