import json
import time

from colorama import Fore, init


init()


y = Fore.LIGHTYELLOW_EX
r = Fore.LIGHTRED_EX
c = Fore.LIGHTCYAN_EX
re = Fore.RESET


class Chatbot():
    def __init__(self):
        t = time.strftime("%A")[:3].upper() + " | " +  time.strftime("%Y-%m-%d")
        print("[ Chat-Bot ] [ " + t + " ]")
        print("")
        self.prompt()

    def prompt(self):

        t = time.strftime("%H:%M:%S")

        userinput = input("[ " + t + " ] [ " + y + "You" + re + " ] ")

        no_answer = True


        if userinput == "exit":
            print("[ " + t + " ] [ " + r + "Bot" + re +" ] " + "Goodbye and until next time!")
            print("")
            quit()


        with open('data.json', 'r') as json_file:

            json_data = json.load(json_file)

            # print(json_data["greetings"]["user"])

            for part in json_data:

                for index, phrase in enumerate(json_data[part]["user"]):
                    if userinput.upper() in phrase.upper() or phrase.upper() in userinput.upper():
                        if part == "functions":
                            if json_data[part]["bot"][index] == "show_time":
                                no_answer = False
                                self.show_time()

                            elif json_data[part]["bot"][index] == "show_day":
                                no_answer = False
                                self.show_day()

                            elif json_data[part]["bot"][index] == "show_date":
                                no_answer = False
                                self.show_date()

                            elif json_data[part]["bot"][index] == "show_help":
                                no_answer = False
                                self.show_help(json_data)
                            
                        else:
                            t = time.strftime("%H:%M:%S")
                            print("[ " + t + " ] [ " + c + "Bot" + re +" ] " + json_data[part]["bot"][index])
                            no_answer = False

            if no_answer:
                t = time.strftime("%H:%M:%S")
                print("[ " + t + " ] [ " + r + "Bot" + re +" ] " + "Sorry I did not understand this.")
                print("[ " + t + " ] [ " + r + "Bot" + re +" ] " + "Please try again!")

        print("")
        self.prompt()

    
    def show_time(self):
        t = time.strftime("%H:%M:%S")
        show_time = time.strftime("%H:%M")
        print("[ " + t + " ] [ " + c + "Bot" + re +" ] " + "It is " + show_time + " now.")

    
    def show_day(self):
        t = time.strftime("%H:%M:%S")
        show_day = time.strftime("%A")
        print("[ " + t + " ] [ " + c + "Bot" + re +" ] " + "Today it is " + show_day + ".")

    
    def show_date(self):
        t = time.strftime("%H:%M:%S")
        show_date = time.strftime("%d.%m.%Y")
        print("[ " + t + " ] [ " + c + "Bot" + re +" ] " + "The date is " + show_date + " today.")


    def show_help(self, json_data):
        t = time.strftime("%H:%M:%S")
        print("[ " + t + " ] [ " + c + "Bot" + re +" ] " + "You can ask these things:")

        for part in json_data:
            for index, phrase in enumerate(json_data[part]["user"]):
                print("[ " + t + " ] [ " + c + "Bot" + re +" ] " + json_data[part]["user"][index])


Chatbot()
