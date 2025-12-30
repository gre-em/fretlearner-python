import random

action = ""
settings = ["E","A","D","G","B"]



# well... play the game
def playGame(settings):

    notes = ["c", "d", "e", "f", "g", "a", "b"]
    strings = settings

    print("[ENTER] to continue to next excercise\n")
    
    # create list of combinations (no open strings)
    combinations = []
    for i in notes:
        for j in strings:
            if (ord(i) != ord(j) + 32):
                combinations.append([i, j])
            

    # randomize excercises until no combinations are left
    while combinations:
        exc = combinations[random.randint(0, len(combinations) - 1)]
        
        # if String == "E", decide for high or low randomly
        if exc[1] != "E":
            eString = ""
        else :
          highLowBool = random.randint(0,1)
          if highLowBool == 0:
              eString = "[high]"
          else:
              eString = "[low]"

        # print excercise
        print("Find (" + exc[0] + ") on the "+ eString +"(" + exc[1] + ")-string! [ENTER]")

        # wait until solved + remove current excercise from combinations
        enter = input("")
        combinations.remove(exc)

    print("Done!\n\n")

    

# choose strings you want to practice
# maybe add option to choose whether to use B or H
def setup():
    x = []
    stringList = list(input("Type the strings you want to practice. (E A D G B)\n"))
    for i in stringList:
        if ord(i) in range(97, 104):
            stringList.append(chr(ord(i) - 32))
    available = ["E","A","D","G","B"]
    for i in available:
        if i in stringList:
            x.append(i)
    return x


print("choices: 'play', 'settings', 'quit'\n")

while action != "quit":
    print("current selection = ", settings, "\n")
    action = input("What would you like to do? ")
    print("\n\n")
    if action == "play":
        playGame(settings)
    elif action == "settings":
        settings = setup()
    elif action == "how to":
        print(">>some how-to-use-this-thing-text, formatted of course!<<\n")
    elif action != "quit":
        print("Invalid input! Try 'play', 'settings' or 'quit'.\n")
