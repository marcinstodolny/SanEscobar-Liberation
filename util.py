import sys
import os
from main import create_player
import ui


def key_pressed():
    try:
        import tty
        import termios
    except ImportError:
        try:
            # probably Windows
            import msvcrt
            key = msvcrt.getch()
            if key == b'\xe0':
                msvcrt.getch()
                return None
            else:
                return key.decode("utf-8")
        except ImportError:
            # FIXME what to do on other platforms?
            raise ImportError("getch not available")
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def input_validator(prompt, possible_options, character=False):
    user_input = input(prompt)
    while user_input not in possible_options:
        clear_screen()
        if character:
            ui.display_classes(character)
        user_input = input(f"{prompt}\nTry again ")
    return int(user_input)
