import time

# Welcome message
print("Welcome to the Amazing Adventure Game!")
time.sleep(1)
print("Get ready to embark on a hilarious journey.")
time.sleep(2)

# Character creation
name = input("Enter your character name: ")
time.sleep(1)
print(f"Hello, {name}! Prepare yourself for some epic fun!")
time.sleep(2)

# Introductory scene
print("Once upon a time, in a land far, far away...")
time.sleep(2)
print("You find yourself in a mystical forest filled with talking animals and enchanted creatures.")
time.sleep(3)
print("You spot a mischievous squirrel with a top hat and a monocle.")
time.sleep(2)

# Squirrel interaction
print("Squirrel: Greetings, traveler! I'm Sir Nutsalot, the wisest squirrel in the land!")
time.sleep(3)
print("Squirrel: I have a riddle for you. Answer correctly, and I'll grant you a special power!")
time.sleep(3)

answer = input("Squirrel: What has keys but can't open locks? ")
time.sleep(1)

if answer.lower() == "a piano":
    print("Squirrel: Well done! Here's your special power: the ability to make anyone laugh uncontrollably!")
    time.sleep(3)
    print("Squirrel: Use it wisely, adventurer!")
else:
    print("Squirrel: Oh dear, that's not the right answer. Better luck next time!")
time.sleep(2)

# Adventure continuation
print("You continue your journey through the forest, armed with the power to make people laugh.")
time.sleep(3)
print("As you walk deeper into the forest, you encounter a grumpy bear blocking your path.")
time.sleep(3)

# Bear interaction
print("Bear: Who dares to disturb my slumber?")
time.sleep(2)
print("You decide to use your special power and tell the bear a joke.")
time.sleep(3)

joke = input(f"{name}: Hey bear, why don't fish play basketball? ")
time.sleep(1)

print("Bear: I don't know, why don't fish play basketball?")
time.sleep(2)

print(f"{name}: Because they're afraid of the net!")
time.sleep(2)

print("The bear bursts into laughter and steps aside, allowing you to pass.")
time.sleep(2)

# Grand finale
print("As you continue your adventure, you come across a magical treasure chest.")
time.sleep(3)
print("You open the chest and discover a scroll that grants you one final wish.")
time.sleep(3)

wish = input("What is your final wish, adventurer? ")
time.sleep(2)

print("Suddenly, a cloud of sparkles surrounds you, and your wish comes true.")
time.sleep(3)
print(f"Congratulations, {name}! You've successfully completed the Amazing Adventure Game with a touch of humor!")
time.sleep(3)
print("Hope you had a great time!")

# Farewell message
print("Thank you for playing! Goodbye!")
