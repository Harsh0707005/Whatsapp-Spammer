# Author : Harsh Master

'''
It is a program for sending spam messages to friends/family for fun.
Note: Before continuing make sure you have installed Whatsapp App in your system, it is linked to your whatsapp account and have a stable internet connection for smooth execution.

While executing it the first time you need to allow chrome to open whatsapp app and tick the checkbox.
'''

# Importing the dependencies
import time
import webbrowser as wb
import pyautogui

print('''*****Note from Developer: Before Continuing with the program make sure you have Whatsapp application installed in your system and has been linked with Mobile Whatsapp...*****
Creator : Harsh Master''')

# Defining function


def Process():
    number = input(
        "Enter the Mobile number of the person you want to send spams... ")
    M_no = str("91") + number

    msg = input("Enter the message that you want to spam... ")
    frq = int(input("Enter the number of times you want send spams... "))
    print("")
    print('''Make sure you have an active internet connection else the program will fail to execute.

    Whatsapp will initiate in 10 seconds and after 20 seconds messages will be sent!!!''')

    time.sleep(10)
    if frq >= 1:
        wb.open(f"https://wa.me/{M_no}?text={msg}")
        # If you have slow internet connection or slow computer, you can increase this parameter.
        time.sleep(20)
        pyautogui.press("enter")
        for i in range(frq-1):
            pyautogui.typewrite(msg)
            pyautogui.press("enter")
    else:
        print("")
        print("The program is terminated as the number of times the message needed to be sent entered by you is invalid.  ")

        print("")

        def Response():

            # asking if retry or quit
            ask = input(
                "If you want to retry press 'r' or willing to quit press 'q' ... ")

            if ask == 'r':
                print("")
                Process()
            elif ask == 'q':
                quit()
            else:
                print("")
                print("********** Please enter a valid response !!! **********")
                print("")
                Response()

        Response()


Process()

print("********The program is successfully executed !!! ********")
print("Found any bug? Feel free to let us know")
