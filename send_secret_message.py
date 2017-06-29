# importing different files and their function like spy details, listdir from os to show files in the folder
    # select friend file and Steganography after installing it in the sysyem

from default_spy_detail import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from os import listdir
from os.path import isfile, join
from select_friend import select_a_friend

#defining send_message function
def send_message():

    #ask which friend you want to send the message
    friend_choice = select_a_friend()

    # path and extension of the image
    img_path = "original_images\\"
    img_name = ".jpg"
    select_file = [f for f in listdir("original_images\\") if isfile(join("original_images\\", f))]
    print select_file
    print ("\n\t\tSelect from Above Images Name")
    X = raw_input("\tWhat is the name of the Image : ")
    original_image = img_path + X + img_name

    #if image is in the folder than message will be coded
    try:
        counter = 1
        output_path = "encrypted_images\%d.jpg"%counter
        text = raw_input("\tWhat do you want to Say (MAX- 100) : ")

        #if length of message is less then 100 and greater than 0
        if len(text) <= 100 and len(text) > 0:

            #Special Keywords using simple if statement
            if text.upper() == "SOS":
                text="Save our Soul"
            if text.upper()=="SAVE ME" and text.upper()=="SAVEME":
                text="I am in danger, Please save me"
            if text.upper()=="BUSY":
                text="I am busy right now, I will contact you later"

            Steganography.encode(original_image, output_path, text)
            counter = counter +1
            print "\n\t\tSecret Message is sent inside the Image."
        else:
            print "\n\t\tCheck Your Written Message Properly"

    #if image is not in the folder than message will not coded
    except:
        print "Wrong Image Name"
    new_chat = ChatMessage(text,True)

    #message will added in the list so we can read the history of chats
    friends[friend_choice].chats.append(new_chat)
