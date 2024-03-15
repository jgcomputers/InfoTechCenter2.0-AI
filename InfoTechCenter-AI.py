import time
import sys

def boot_up_animation():
    # Set the time interval between each ellipsis animation
    time_to_sleep = 0.5
    # Initialize the ellipsis count
    ellipsis_count = 0
    # Define the message template for the boot-up animation
    message_template = "Infotech Center System Booting"

    # Loop for 20 iterations to simulate the boot-up process
    for _ in range(20):
        # Update the ellipsis count cyclically (0, 1, 2, 3, 0, 1, ...)
        ellipsis_count = (ellipsis_count + 1) % 4
        # Construct the message with the current ellipsis count
        message = f"{message_template}{'.' * ellipsis_count}"
        # Print the message with a carriage return to overwrite previous output
        sys.stdout.write(f"\r{message}")
        # Flush the output to ensure immediate printing of the animation update
        sys.stdout.flush()
        # Wait for the specified time interval before the next iteration
        time.sleep(time_to_sleep)

    # Print a newline after the animation completes
    print("\n\nOperating System Booted Up - Retina Scanned - Access Granted")

if __name__ == "__main__":
    # Print a welcome message before starting the animation
    print("\n\nWelcome to InfoTech Center V1.0\n")
    # Wait for 1 second before starting the animation
    time.sleep(1)
    # Call the boot-up animation function
    boot_up_animation()