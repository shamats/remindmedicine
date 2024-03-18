#-------------------------------------------------------------------------------------#
# Author: Shama.T.S
# Project Name : Reminder to take medicines
# Version : 1.1
# Date : 15-03-2024
# To Do : install pyttsx3 by : pip install pyttsx3
#-------------------------------------------------------------------------------------#

import datetime
import time
import pyttsx3

def remind_medicine(medicine, dosage, interval):
    engine = pyttsx3.init()
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        print(f"It's {current_time}. Time to take {dosage} of {medicine}.")
        
        engine.say(f"It's time to take {dosage} of {medicine}.")
        engine.runAndWait()
        
        time.sleep(interval)

def main():
    medicine = input("Enter the name of the medicine: ")
    dosage = input("Enter the dosage: ")
    interval = int(input("Enter the reminder interval in seconds: "))
    
    print(f"Reminder set for {medicine} - {dosage} every {interval} seconds.")
    remind_medicine(medicine, dosage, interval)

if __name__ == "__main__":
    main()
