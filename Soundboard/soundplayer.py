# This is a command line based sound player made using Python 3.8.2
# Requires the playsound library
# Requires a "Sounds" folder in the same directory that you're running this from

import os
from playsound import playsound


def sound_player():

    directory = dirname = os.path.dirname(__file__) + "\\Sounds\\"
    err = 1

    while(1):

        user_input = ''
        print("\n")
        print("Welcome to the Wacky Soundboard Sound Player!\n")
        print("Type play to play a sound file.")
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

        elif (user_input == str('changedir')):
            while(user_input == str('changedir') and err == 1):
                directory = ''
                directory = input(str(directory))
                try:    
                    list = os.listdir(directory)
                    print("The directory is now: " + directory)
                    err = 0
                except OSError: # Captures error when selecting an invalid directory
                    err = 1
                    print("Invalid directory! Try again.")
            

        elif user_input == str('files'):
            for x in list:
                print(x)

        elif user_input == str('exit'):
            break # Exits the program

        else:
            print("This program doesn't understand that command")
    
sound_player()