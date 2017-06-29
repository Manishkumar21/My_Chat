# importing different files and their function like read_message file, listdir from os to show files in the folder
    # select friend file and Steganography after installing it in the sysyem

from default_spy_detail import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from os import listdir
from os.path import isfile, join
from select_friend import select_a_friend

#defining read_message function
def read_message():

    #which friend 's message you want to read
    sender = select_a_friend()

    #path and extension of the image
    img_path = "encrypted_images\\"
    img_name = ".jpg"

    # it will show the all the file stored in "encrypted_images" Folder
    select_file = [f for f in listdir("encrypted_images\\") if isfile(join("encrypted_images\\", f))]
    print select_file

    #variable that will call the image
    X = raw_input("What is the name of the Image that you want to decode: ")

    #decoding the image
    output_path = img_path + X + img_name
    secret_text = Steganography.decode(output_path)
    new_chat = ChatMessage(secret_text,False)
    friends[sender].chats.append(new_chat)
    print "Secret Message has been decoded!"

    #decoded message
    print "\n\t\t****decoded Message Is : %s****"%secret_text