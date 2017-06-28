from default_spy_detail import spy, Spy, ChatMessage, friends
def add_status(STATUS_MESSAGES):
    updated_status_message = None
    if spy.current_status_message != None:

        print "Your current Message is %s\n" % (spy.current_status_message)
    else:
        print "\tYou don't have any status message currently \n"

    default = raw_input("Do you want to select from the older status (Y/N) ")

    if default.upper() == "N":
        new_status_message = raw_input("What Status do you want to set ? ")
        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message
            spy.current_status_message = updated_status_message
    elif default.upper() == 'Y':
        item_position = 1
        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above Messages : "))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print "Option Is not valid."

    if updated_status_message:
        print "Your updated status message is : %s" % (updated_status_message)
    else:
        print "you did not enter any status message"

    return updated_status_message