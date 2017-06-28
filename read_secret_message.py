from default_spy_detail import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from os import listdir
from os.path import isfile, join
from select_friend import select_a_friend
def read_message():

    sender = select_a_friend()

    img_path = "encrypted_images\\"
    img_name = ".jpg"
    select_file = [f for f in listdir("encrypted_images\\") if isfile(join("encrypted_images\\", f))]
    print select_file
    X = raw_input("What is the name of the Image that you want to decode: ")
    output_path = img_path + X + img_name

    secret_text = Steganography.decode(output_path)

    new_chat = ChatMessage(secret_text,False)

    friends[sender].chats.append(new_chat)

    print "Secret Message has been decoded!"
    print "\n\t\t****decoded Message Is : %s****"%secret_text