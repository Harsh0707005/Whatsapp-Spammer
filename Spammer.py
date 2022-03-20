# Author : Harsh Master

'''
It is a program for sending spam messages to friends/family for fun.
Note: Before continuing make sure you have linked your whatsapp to Wwb interface and have a stable internet connection for smooth execution.
'''

# Importing the dependencies
import pywhatkit as kit
import pyautogui
from datetime import datetime   

print("*****Note from Developer: Before Continuing with the program make sure you have linked Whatsapp Web with Mobile Whatsapp...*****")
print("Creator : Harsh Master")

print("")


# Defining function
def Process():
    number = input(
        "Enter the Mobile number of the person you want to send spams... ", )
    M_no = str("+91") + number # asking for mobile number

    msg = input("Enter the message that you want to spam... ") # asking for message to be sent
    
    frq = int(input("Enter the number of times you want send spams... ")) # asking for number of times message to be spammed
    

    today_date = datetime.now() #fetching date and time
    hour = today_date.hour
    minute = today_date.minute
    
    if minute >= 60:  # if time is something like 7:59
        hour = hour + 1
        minute = minute - 60
    else:
        pass

    # to minimize wait time
    if today_date.second >= 35:  # as pywhatkit requires 20 second of wait time by default.
        minute = minute + 2
    else:
        minute = minute + 1

    
    if frq >= 1:
        print("")
        print("Make sure you have an active internet connection else the program will fail to execute.")
        print("")

        kit.sendwhatmsg(M_no, msg, hour, minute)

        for i in range(frq-1):
            pyautogui.typewrite(msg)
            pyautogui.press("enter")
    else:
        print("")

        print("The execution of the program is interrupted as the number of times the message needed to be sent entered by you is invalid.  ")

        print("")

        def Response():
            
            # asking if retry or quit
            ask = input(
                "If you want to retry press 'r' or willing to quit press 'q' ...")
            
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
