from time import sleep
import random
import datetime
import turtle
from pip._internal import main
main(["install", "psutil"])
import psutil
battery = psutil.sensors_battery()
print(battery.percent)
if battery.percent == 15:
    print("Charge your device.")
if battery.percent == 10:
    print("Charge your device.")
if battery.percent == 5:
    print("Change your device.")
if battery.percent == 1:
    print("Charge your device quickly!")
def Game():
    turtle.pensize(5)
    turtle.onkey(GameMoveUp, "Up")

    turtle.listen()
def GameMoveUp():
    turtle.seth(90)
    turtle.fd(20)
def printtxt(text):
    print(text)
def Inputtext(text, colon):
    if colon == False:
        input(text)
    if colon == True:
        input(text + ": ")
def answer(firstFactor, secondFactor, equationType):
    if equationType == "+":
        print(int(firstFactor) + int(secondFactor))
    if equationType == "-":
        print(int(firstFactor) - int(secondFactor))
    if equationType == "/":
        print(int(firstFactor) / int(secondFactor))
    if equationType == "*":
        print(int(firstFactor) * int(secondFactor))
def Home(wait, now):
    if wait == False & now == True:
        sleep(0)
        user("Mark")
    if now == False:
        sleep(wait)
        user("Mark")
def randomNumber():
    print("Your ID from this server is: 1.0")
def close_Calculator():
    close = input("Close Calculator?")
    if close == "Yes":
        user("Mark")
def guest_mode(userName):
    sleep(1)
    while True:
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year
        day = datetime.datetime.now().strftime("%A")
        searchGM = input("Search anything, " + userName + "... ")
        if searchGM == "What's the date?":
            print(datetime.datetime.now())
        if searchGM == "What day is it?":
            print(day)
        if searchGM == "What year is it?":
            print(year)
        if searchGM == "Close":
            setup()
            break
        if searchGM == "What month is it?":
            print(month)
        if searchGM == "Calculator":
            firstFactor = input("First Factor: ")
            secondFactor = input("Second Factor: ")
            equation = input("Equation Type? +, -, /, *?: ")
            if equation == "+":
                print(int(firstFactor) + int(secondFactor))
                close_Calculator()
            if equation == "-":
                print(int(firstFactor) - int(secondFactor))
                close_Calculator()
            if equation == "/":
                print(int(firstFactor) / int(secondFactor))
                close_Calculator()
            if equation == "*":
                print(int(firstFactor) * int(secondFactor))
                close_Calculator()
            break
        if searchGM == "Battery Percentage":
            battery = psutil.sensors_battery()
            print(battery.percent)
def user(userName):
    sleep(1)
    while True:
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year
        day = datetime.datetime.now().strftime("%A")
        searchGM = input("Search anything, " + userName + "... ")
        if searchGM == "What's the date?":
            print(datetime.datetime.now())
        if searchGM == "What day is it?":
            print(day)
        if searchGM == "What year is it?":
            print(year)
        if searchGM == "Close":
            setup()
            break
        if searchGM == "What month is it?":
            print(month)
        if searchGM == "Settings":
            settingSearch = input("Search a setting...")
            if settingSearch == "Close Settings":
                print("Closed Settings.")
                user("Mark")
            if settingSearch == "Date and Time":
                year = input("What's the year?")
                day = input("What's the day?")
                month = input("What's the month?")
                print("Is this the time you wanted?:")
                print(datetime.datetime(int(year), int(month), int(day)))
                yesorno = input("Yes or no?")
                if yesorno == "Yes":
                    print("Cannot change it, This will be a future update!")
                if yesorno == "No":
                    print("Canceled.")
                    user("Mark")
            break
        if searchGM == "ID":
            randomNumber()
            sleep(2)
            user("Mark")
            break
        if searchGM == "Calculator":
            firstFactor = input("First Factor: ")
            secondFactor = input("Second Factor: ")
            equation = input("Equation Type? +, -, /, *?: ")
            if equation == "+":
                print(int(firstFactor) + int(secondFactor))
                close_Calculator()
            if equation == "-":
                print(int(firstFactor) - int(secondFactor))
                close_Calculator()
            if equation == "/":
                print(int(firstFactor) / int(secondFactor))
                close_Calculator()
            if equation == "*":
                print(int(firstFactor) * int(secondFactor))
                close_Calculator()
            break
        if searchGM == "CMD":
            sleep(1)
            print("Please wait... We are getting all commands...")
            sleep(1)
            print("You can code the CMD prompt fixing this file...")
            printtxt("Nothing here....")
            Inputtext("Nothing here....", False)
            Inputtext("Nothing here....", True)
            answer(5, 5, "+")
            answer(5, 5, "-")
            answer(5, 5, "/")
            answer(5, 5, "*")
            user("Mark")
            break
        if searchGM == "Games until restart please":
            Game()
            break
        if searchGM == "Battery Percentage":
            battery = psutil.sensors_battery()
            print(battery.percent)
def setup():
    sleep(1)
    turtle.write("Welcome to Itzgametime OS Python...")
    print("Welcome to Itzgametime OS Python...")
    sleep(1)
    hello = input("Create User, Or Select a user. ")
    if hello == "Create User":
        print("You will be guest.")
        sleep(1)
        print("Please wait...")
        sleep(1)
        print("Arduino Watch/")
        sleep(1)
        print("Arduino watch/Setup")
        sleep(1)
        print("Arduino/Setup/index.py")
        sleep(1)
        print("Done")
        guest_mode("Guest")
    if hello == "Select a user.":
        name = input("What's your name?: ")
        if name == "Mark":
            while True:
                pw = input("Password?: ")
                if pw == "1964":
                    print("Congrats! You are in!")
                    user(name)
                    break
                else:
                    print("Wrong password! Try again.")
setup()