# Break-The-Door_1.0 - Base version, with a variable for door_health and and
#                      small damages.
# Break-The-Door_1.1 - If door breaks, print something. -> while True (?)
# Break-The-Door_1.2 - based on The_Closed_Door1.2.py, it will have two options, but eventually one will make the other work. Removed while.

print "This is the Break-The-Door Game!"
door_health = 100

def Break_The_Door():
    global door_health
    n = raw_input("Do you want to damage it?")
    if n == "yes":
        door_health -= 10
        print "Door health: %r" % (door_health)
        Break_The_Door()
    elif n == "no":
        print "The door stays intact."
        print "Door health: %r" % (door_health)
        Break_The_Door()

def restart():
    if door_health > 0:
        Break_The_Door()
    else:
        print "You broke the door! Enter some text and enter to quit."
        exit = raw_input

restart()
