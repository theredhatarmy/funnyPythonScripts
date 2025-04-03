import time
import os
import platform

def clear_screen():
    """
    Clears the terminal screen based on the operating system.
    """
    system_name = platform.system()

    # For Windows
    if system_name == "Windows":
        os.system("cls")
    # For macOS and Linux
    else:
        os.system("clear")

def print_clock(current_time):
    """
    Prints the digital clock in a nice layout.
    """
    clear_screen()
    print("\nDigital Clock\n".center(30, '-'))
    print(f"{current_time}".center(30))
    print("-" * 30)

def digital_clock():
    """
    Runs the digital clock program, continuously updating the time every second.
    """
    try:
        while True:
            # Get the current time in HH:MM:SS format
            current_time = time.strftime("%H:%M:%S")

            # Print the clock
            print_clock(current_time)

            # Wait for 1 second before updating the clock
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nClock stopped.")
        exit(0)

# Run the digital clock program
if __name__ == "__main__":
    digital_clock()
