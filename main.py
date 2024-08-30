from pyperclip import paste
from pynput import keyboard
from pynput.keyboard import Controller, Key
import mouse
from time import sleep

keyboard_controller = Controller()



wait_time = 0.1
points = [
    (274, 305), 
    (493, 302), 
    (683, 295), 
    (268, 533), 
    (474, 501), 
    (666, 507), 
    (304, 680), 
    (505, 693), 
    (671, 687), 
    (239, 894), 
    (451, 889), 
    (707, 917),
]

translation_dict = {
    "the sea": "el mar",
}


two_way_dict = {}
for key, value in translation_dict.items():
    two_way_dict[key] = value
    two_way_dict[value] = key

def convert_to_list(multiline_string):
    return [line.strip() for line in multiline_string.strip().split('\n')]

def my_function():
    type_ctrl_a_c()
    sleep(wait_time)
    text = paste()
    items = convert_to_list(text)
    #     items = items[7:] WHEN NOT LOGGED IN

    items = items[6:]
    print(items)

    processed_items = set()

    for item in items:
        if item not in processed_items and item in two_way_dict:
            pair = two_way_dict[item]
            print(f"Item: {item}, Pair: {pair}")

            try:
                item_index = items.index(item)
                if item_index < len(points):
                    mouse.move(*points[item_index])
                    sleep(wait_time)
                    mouse.click()
                    sleep(wait_time)

                processed_items.add(item)
                
                if pair in items:
                    pair_index = items.index(pair)
                    if pair_index < len(points):
                        mouse.move(*points[pair_index])
                        sleep(wait_time)
                        mouse.click()
                        sleep(wait_time)

                    processed_items.add(pair)

            except ValueError:
                pass

def type_ctrl_a_c():
    with keyboard_controller.pressed(Key.ctrl):
        keyboard_controller.press('a')
        keyboard_controller.release('a')
    
    with keyboard_controller.pressed(Key.ctrl):
        keyboard_controller.press('c')
        keyboard_controller.release('c')

def on_press(key):
    try:
        if key.char == 'q':
            my_function()
        if key.char == 'w':
            print(str(mouse.get_position()) + ", ")

    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
