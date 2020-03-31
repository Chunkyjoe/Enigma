# This is a command line based sound player made using Python 3.8.2
# Requires a "sound" folder in the same directory as the folder you're running this from

import os
from playsound import playsound


def sound_player():

    directory = dirname = os.path.dirname(__file__) + "\\Sounds\\"

    while(1):

        user_input = ''
        print("\n")
        print("Welcome to the Wacky Soundboard Sound Player!\n")
        print("Type play to play a sound test file.")
        print("Type files to list the files in the folder.")
        print("Type changedir to change the file directory")
        print("Type exit to exit this program.")

        user_input = input(str(user_input))
        if user_input == str('play'):
            user_input = ''

            print("Type in the filename (exclude .mp3 when typing)")
            print("Any mismatched name will return you to the main menu")

            list = os.listdir(directory)  # Generates a list of files found in the directory location
            for x in list:
                list = x[:-4]   # This line removes the filetype (.mp3) from the list
            user_input = input(str(user_input))

            if user_input in list:
                playsound(directory + user_input + '.mp3')

        elif user_input == str('changedir'):
            directory = ''
            directory = input(str(directory))
            print("The directory is now: " + directory)

        elif user_input == str('files'):
            list = os.listdir(directory)
            for x in list:
                print(x)

        elif user_input == str('exit'):
            break # Exits the program

        else:
            print("This program doesn't understand that command")
    
sound_player()