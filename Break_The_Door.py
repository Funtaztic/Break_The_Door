# Break-The-Door_1.0 - Base version, with a variable for door_health and and
#                      small damages.

print "This is the Break-The-Door Game!"
door_health = 100

def Break_The_Door():
    global door_health
    print "The door is at %d" % (door_health)
    door_health -= 10
    print "The door is at %d" % (door_health)
    door_health -= 10
    print "The door is at %d" % (door_health)

Break_The_Door()
