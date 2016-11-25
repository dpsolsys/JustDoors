from sys import exit
import random


def green_room():
    print "You are in the green room and there are two doors."
    print "Red Room or Blue Room"

    next_room = raw_input('> ').lower()

    pad_access()

    if next_room == 'red':
        red_room()
    elif next_room == 'blue':
        blue_room()
    else:
        end()


def end():
    print "There is no such color"
    exit(0)


def denied_message(the_message):
    print the_message, "Access Denied"


def pad_access():
    print "There is a number pad on the door"

    while True:
        print "A blinking cursor looking for a single number from 1 - 9"

        rand_digit = random.randrange(10)
        
        single_digit = str(raw_input("> "))

        if len(single_digit) >= 2:
            denied_message("Only 1 - 9.")
            print "Please try again"

        elif int(single_digit) != rand_digit:
            denied_message("Incorrect Digit.")

        else:
            # single_digit == rand_digit
            print "The door slowly opens"
            break


def red_room():
    print "You just entered the Red room with two doors"
    print "Green room or Blue Room"

    next_room = raw_input('> ').lower()

    pad_access()

    if next_room == 'green':
        green_room()
    elif next_room == 'blue':
        blue_room()
    else:
        end()


def blue_room():
    print "You entered the Blue room with two doors"
    print "Green Room or Red Room"

    next_room = raw_input('> ').lower()

    pad_access()

    if next_room == 'green':
        green_room()
    elif next_room == 'red':
        blue_room()
    else:
        end()


def start():
    print "Welcome and your journey through the colored doors starts here."
    print "There are three doors in front of you"
    print "Green, Blue and Red"
    print "choose a door"

    next_door = raw_input("> ").lower()
    assert next_room, "No such room"
    pad_access()

    if next_door == "red":
        red_room()
    elif next_door == 'green':
        green_room()
    elif next_door == 'blue':
        blue_room()
    else:
        end()

start()







