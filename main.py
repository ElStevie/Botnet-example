from controller import Controller
from utils import *
import getpass


def add_new_bot(controller):
    print_centered("Adding a new bot")
    host = input("Host's IP Addres: ")
    user = input("Username: ")
    password = getpass.getpass()
    if controller.add_bot(host, user, password):
        print("\nBot added successfully!")


def send_command(controller):
    print_centered("Sending a command")

    command = input("Enter the command: ")
    print("This is the command to be sent:")
    print(f"-->{command}<--")
    answer = input("Ok? (y/n) ")
    send = True if answer.lower() == "y" else False
    if send:
        controller.command_bots(command)
        print("\nEnd of the execution.")
    else:
        print("\nNo command was sent.")


if __name__ == '__main__':
    ADD_NEW_BOT = 0
    SEND_CMD = 1
    EXIT = 2

    options = ["Add new bot", "Send command to bots", "Exit"]

    controller = Controller()

    while True:
        for i, opt in enumerate(options):
            print(f"[{i + 1}] {opt}")

        try:
            selected = int(input("Your choice: ")) - 1
            options_qty = EXIT + 1

            valid_option = 0 <= selected < options_qty
            if valid_option:
                if selected == ADD_NEW_BOT:
                    add_new_bot(controller)
                elif selected == SEND_CMD:
                    send_command(controller)
                else: # selected == EXIT
                    break

                if selected != EXIT:
                    pause()
            else:
                pause(f"Options are between 1 and {options_qty}.")
        except ValueError:
            pause("Enter a valid integer.")
            selected = -1

        if selected != EXIT:
            clear_screen()
