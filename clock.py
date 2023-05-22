import time

def digital_clock():
    while True:
        # Clear the screen (works on Windows, Linux, and macOS)
        print("\033[H\033[J")

        # Get the current time
        current_time = time.strftime("%H:%M:%S")

        # Print the current time
        print("Digital Clock")
        print("----------------")
        print(current_time)

        # Wait for 1 second
        time.sleep(1)

# Run the digital clock program
digital_clock()
