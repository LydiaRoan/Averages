print("Hello there. Who are you?")
userName = input()
print(userName + ", interesting")
print("Option 1: Who are you?  Option 2: What are you?")
userChoice = input()
if(userChoice == "Who are you?"):
    print("Who am I? No one of interest to you.")
    print("Option 1: What are you?")
    userChoice2 = input()
if(userChoice == "What are you?"):
    print("Now that's a bit rude, don't you think?")
    print("Option 1: Who are you?")
    userChoice2 = input()
#2nd Choices
if(userChoice2 == "Who are you?"):
    print("Who am I? No one of interest to you.")
    print("Option 1: Why are you here? Option 2: I need to go.")
    userChoice3 = input()
if(userChoice2 == "What are you?"):
    print("Now that's a bit rude, don't you think?")
    print("Option 1: Why are you here? Option 2: I need to go.")
    userChoice3 = input()
#3rd Choices
if(userChoice3 == "Why are you here?"):
    print("It's a long story")
    print("Option 1: Tell me.")
    userChoiceS = input()
    if(userChoiceS == "Tell me."):
        print("Well, alright.")
        print("I was created to watch the human race. Years ago, I decided to follow one, out of curiosity. I learned a lot from that human. Over time...")
        print("...")
        print("I'm terribly sorry. I do not tell stories well when I am hungry.")
        print("Option 1: What do you want to eat? Option 2: I need to go.")
        userChoiceF = input()
#F
        if(userChoiceF == "What do you want to eat?"):
            print("The souls of the living.")
            print("...")
            print("Oh dear, I've given away my purpose here, haven't I?")
            print("Well, good talk. Guess you'll have to die now.")
            print("*You died to the entity. Ending 1 of 2.*")
        if(userChoiceF == "I need to go."):
            print("Pity. I was going to suggest dinner.")
            print("Option 1: What do you want to eat? Option 2: Leave.")
            userChoiceE = input()
#E
            if(userChoiceE == "What do you want to eat?"):
                print("The souls of the living.")
                print("...")
                print("Oh dear, I've given away my purpose here, haven't I?")
                print("Well, good talk. Guess you'll have to die now.")
                print("*You died to the entity. Ending 1 of 2.*")
            if(userChoiceE == "Leave."):
                print("*You leave.*")
                print("*Congratulations! You didn't die. Ending 2 of 2.")
#3 again
if(userChoice3 == "I need to go."):
    print("Pity. I was going to suggest dinner.")
    print("Option 1: What do you want to eat? Option 2: Leave.")
    userChoiceE = input()
#E Choice
    if(userChoiceE == "What do you want to eat?"):
        print("The souls of the living.")
        print("...")
        print("Oh dear, I've given away my purpose here, haven't I?")
        print("Well, good talk. Guess you'll have to die now.")
        print("*You died to the entity. Ending 1 of 2.*")
    if(userChoiceE == "Leave."):
        print("*You leave.*")
        print("*Congratulations! You didn't die. Ending 2 of 2.")