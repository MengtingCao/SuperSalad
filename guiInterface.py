from guizero import App, Text, Box, PushButton

item_names = ["green", "red", "purple", "brown",
              "yellow", "blue", "pink", "orange", "black", "white"]
item_index = 0


def button_command(index):
    item_index = index
    item_name.value = item_names[item_index]


def make_map(list):
    items = {}
    for item in item_names:
        items[item] = 1
    return items


app = App(title="Customizable Food Dispenser")

#Make map with item names as keys and quantity as values starting from 0
items = make_map(item_names)

#container format
buttons_box = Box(app, align="left", height="fill")
right_box = Box(app, align="right", height="fill", width="fill")
detail_box = Box(right_box, width="fill")

#item add/remove box i.e. detail box
item_name = Text(detail_box, text=item_names[item_index])
add_remove_box = Box(right_box, layout="grid")
add_button = PushButton(add_remove_box, height="fill", text="Add", grid=[0, 0])
box_pad = Box(add_remove_box, height="fill", width="20", grid=[1, 0])
remove_button = PushButton(
    add_remove_box, height="fill", text="Remove", grid=[2, 0])

#button group for items
for i in range(len(item_names)):
    button = PushButton(buttons_box, command=button_command(i),
                        width="fill", height="fill", text=item_names[i])

#receipt box
receipt_box = Box(right_box, width="fill", height="fill", border=True)
title = Text(receipt_box, text="Current Cart")
for item in items:
    if not items[item] == 0:
        item_quantity = item + " " + str(items[item]) + "x"
        text = Text(receipt_box, text=item_quantity)

#dispense box
dispense_box = Box(right_box, width="fill", align="bottom")
dispense_button = PushButton(dispense_box, text="Dispense", align="right")

app.display()
