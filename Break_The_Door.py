# Break-The-Door_1.0 - Base version, with a variable for door_health and and
#                      small damages.
# Break-The-Door_1.1 - If door breaks, print something. -> while True (?)

print "This is the Break-The-Door Game!"
door_health = 100

def Break_The_Door():
    global door_health
    while True:
        n = raw_input("Do you want to damage it? Health: %d" (door_health))
        if n.strip() == "yes":
            door_health -= 10
        elif n.strip() == "no":
            print "Door is at %d" (door_health)
        elif door_health == 0:
            break

Break_The_Door()
