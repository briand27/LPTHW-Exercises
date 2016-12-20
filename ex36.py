from sys import exit

def custom_input():
    print "\n"
    result = raw_input(">> ")
    print "\n"
    return result

def dead(prompt):
    print prompt, "\nCongrats, you are lose. Nice work!\n"
    exit(0)

def start():
    print "\n\tYou are in a dark room."
    print "To your left there is a door through which you can hear rustling grass."
    print "To your right there is a door through which you hear water dripping."
    print "Which one do you take?"

    door = custom_input()

    if(door == 'left'):
        plain(False)
    elif(door == 'right'):
        cave(False)
    else:
        dead("You stumble around in the darkness until you die.")

def plain(troll):
    print "\tYou open the door and see a jaguar prowling about in a wide open plain."

    if troll:
        print "The troll, used to the dark caverns, is blinded by the sun."

    print "\nDo you choose to:"
    print "1. Charge the jaguar"
    print "2. Run from the jaguar"

    if troll:
        print "3. Run from the troll"
        print "4. Hide behind the troll?"

    choice = int(custom_input())

    if choice == 1:
        dead("Please you can't fight a jaguar.")
    elif choice == 2:
        dead("Please you can't outrun a jaguar.")
    elif troll and choice == 3:
        dead("The jaguar sees you darting and chases you down.")
    elif troll and choice == 4:
        print "\tThe jaguar runs at you, baring its fangs."
        print "You hide behind the thrashing, infuriated troll."
        print "The jaguar collides into the troll and the two begin fighting."
        print "\n"
        print "You see a door to the North and the East, which do you go through?"

        door = custom_input();

        if door == "N" or door == "North":
            forest()
        elif door == "E" or door == "East":
            cave(True)
        else:
            dead("The jaguar turns its attention to you as you are deciding.")

    else:
        dead("As you stand there in indecision the troll smashes you into the ground in its blind rampage.")

def cave(visited):
    print "\tYou stumble into a dark, damp cave"
    print "Water drips off the stalactites onto the floor\n"

    if visited:
        print "A group of trolls investigating the roar they heard earlier spots you."
        dead("You stumble into their midst and they beat you with their clubs.")

    print "A lone troll is feeding when he sees you enter."
    print "The troll roars at you, drops the carcass, and grabs a club."

    print "\nDo you choose to:"
    print "1. Fight troll"
    print "2. Run"

    choice = int(custom_input())

    if choice == 1:
        print "A sudden wave of courage washes over you."
        dead("Unfortunately you are a scrub and he is a troll.")
    elif choice == 2:
        print "You run from the troll with it close behind!"
        print "You see a door to the North through which you hear nothing but crashing waves."
        print "You see a door to the East through which you hear a familiar rustling grass."
        print "Which way do you go?"

        door = custom_input()

        if door == "N" or door == "North":
            sea(False)
        elif door == "E" or door == "East":
            plain(True)
        else:
            dead("You can't decide and the troll catches you.")

def forest():
    print "\tYou enter a dense forest."
    print "The jaguar, after defeating the blind troll, sprints in after you."
    print "\nWhat will you do?"
    print "1. Run"
    print "2. Hide"
    print "3. Fight"

    choice = int(custom_input())

    if choice == 1:
        dead("You trip on a gnarled root and the jaguar pounces on you.")
    elif choice == 2:
        print "You quickly duck behind one of the many trees"
        print "The jaguar crashes through the door."
        print "It runs frantically around, trips on a root, knocks its head on a tree, and passes out."
    elif choice == 3:
        dead("Please, you can't fight a jaguar.")
    else:
        dead("In your indecision the jaguar catches you")

    print "\nYou emerge from behind the tree."
    print "You see a door to the East through which you hear nothing but crashing waves."
    print "\nDo you:"
    print "1. Peek through the door"
    print "2. Walk confidently through the door"
    print "3. Run through the door!"

    choice = int(custom_input())

    if choice == 1:
        print "You peek through the door and see an ocean 50 feet below."
    elif choice == 2 or choice == 3:
        sea(False)
    else:
        print "As you stand there deciding what to do, the jaguar wakes up."
        dead("Angered at being tricked, it bares its fangs and pounces on you.")

    print "You step back into the forest to decide what to do."
    print "\nDo you choose to:"
    print "1. Dive through the door into the ocean gracefully like a swan"
    print "2. Walk confidently through the door"
    print "3. Run through the door!"
    print "4. Fashion a raft"

    choice = int(custom_input())

    if choice == 1 or choice == 2 or choice == 3:
        print "I did mention it was 50 feet right?"
        sea(False)
    elif choice == 4:
        print "You fashion a raft out of fallen branches and thick leaves and vines."
        print "You descend peacefully down onto the ocean on longer vines."
        sea(True)
    else:
        print "As you stand there deciding what to do, the jaguar wakes up."
        dead("Angered at being tricked, it bares its fangs and pounces on you.")

def sea(raft):
    if not raft:
        print "You crash through the door..."
        dead("... and plummet 50 feet into an ocean and drown.")

    print "\n\tYou are in a vast, seemingly endless ocean."
    print "There is a pleasant breeze and a delightful sunny presence."
    print "Something probably stirs beneath the waves but you don't want to find out."
    print "You see a door to the North and one to the South, which do you row to?"

    door = custom_input()

    if door == "N" or door == "North":
        print "You row your raft North and climb gently out into the door."
        win()
    elif door == "S" or door == "South":
        print "You row your raft South and get swept through the door in a sudden current."
        cave(True)
    else:
        print "As you sit around drinking in the rays a large sea monster breaks through the surface."
        dead("Fun fact: You can't run, hide, or fight a large sea monster.")

def win():
    print "You walk into a room filled with gold and treasures and smile."
    print "Congratulations, you win!"
    exit(0)

start()
