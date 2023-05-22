import time

def silly_dance():
    print("Get ready for a silly dance!")
    time.sleep(2)
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("Dance!")
    print("(o)(o)")
    print(" \\../")
    print("  **")
    

def joke_teller():
    print("Knock, knock!")
    
    time.sleep(2)
    print("Who's there?")
    time.sleep(2)
    print("Boo.")
    time.sleep(2)
    print("Boo who?")
    time.sleep(2)
    print("Don't cry, it's just a joke!")

def silly_song():
    lyrics = [
        "I once had a pet named Fred,",
        "He liked to eat cheese and bread.",
        "One day he danced on his head,",
        "And now he's got jelly instead!"
    ]
    for line in lyrics:
        print(line)
        time.sleep(2)

print("Welcome to the Silly Python Show!")
time.sleep(2)
print("What would you like to see?")
time.sleep(2)
print("1. Silly Dance")
print("2. Joke Teller")
print("3. Silly Song")
choice = input("Enter your choice (1, 2, or 3): ")

if choice == "1":
    silly_dance()
elif choice == "2":
    joke_teller()
elif choice == "3":
    silly_song()
else:
    print("Oops! That's not a valid choice.")

print("Thanks for joining the Silly Python Show! Come back soon!")
