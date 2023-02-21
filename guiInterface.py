from guizero import App, Text, Box, PushButton

def button_command():
    return 0

def make_map(list):
    items = {}
    for item in item_names:
        items[item] = 0
    return items

app = App(title="Customizable Food Dispenser")

item_names = ["green", "red", "purple", "brown", "yellow", "blue", "pink", "orange", "black", "white"]

#Make map with item names as keys and quantity as values starting from 0
items = make_map(item_names)

#container format
buttons_box = Box(app, align="left", height="fill")
right_box = Box(app, align="right", height="fill", width="fill")
detail_box = Box(right_box, width="fill")
receipt_box = Box(right_box, width="fill")

#item add/remove box
item_name = Text(detail_box, text=item_names[0])
add_remove_box = Box(right_box, layout="grid")
add_button = PushButton(add_remove_box, height="fill", text="Add", grid=[0, 0])
box_pad = Box(add_remove_box, height="fill", width="20", grid=[1,0])
remove_button = PushButton(add_remove_box, height="fill", text="Remove", grid=[2,0])

#button group for items
for item in item_names:
    button = PushButton(buttons_box, command=button_command,
                        width="fill", height="fill", text=item)

#

app.display()