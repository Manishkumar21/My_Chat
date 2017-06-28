from default_spy_detail import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from os import listdir
from os.path import isfile, join
from select_friend import select_a_friend
def send_message():

    friend_choice = select_a_friend()
    img_path = "original_images\\"
    img_name = ".jpg"
    select_file = [f for f in listdir("original_images\\") if isfile(join("original_images\\", f))]
    print select_file
    print ("Select from Above Images Name : ")
    X = raw_input("What is the name of the Image : ")
    original_image = img_path + X + img_name
    try:
        output_path = "encrypted_images\output.jpg"
        text = raw_input("What do you want to Say : ")
        Steganography.encode(original_image, output_path, text)
    except:
        print "Wrong Image Name"

    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)

    print "Secret Message is sent inside the Image."