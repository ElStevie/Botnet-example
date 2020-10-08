from os import system, name


def print_centered(msg):
    length = len(msg)
    is_pair = length % 2 == 0
    starting_point = 40 - (length//2 + (0 if is_pair else 1))
    spacing = ""
    for i in range(starting_point):
        spacing += " "
    print(f"{spacing}{msg.upper()}")


def clear_screen():
    system(("cls" if name == "nt" else "clear"))


def pause(msg = None):
    input(msg if msg else "Press Enter to continue...")
