from guizero import App, Text, Box, PushButton

item_names = ["green", "red", "purple", "brown",
              "yellow", "blue", "pink", "orange", "black", "white"]
global item_index
item_index = 0

texts = []

def button_command(index):
    global item_index
    item_index = index
    item_name.value = item_names[item_index]


def make_map(list):
    items = {}
    for item in item_names:
        items[item] = 0
    return items

def add():
    items[item_names[item_index]] = items[item_names[item_index]]+1
    if(items[item_names[item_index]] > 0):
        texts[item_index].value = item_names[item_index] + " " + str(items[item_names[item_index]]) + "x"
        texts[item_index].show()

def remove():
    

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
add_button = PushButton(add_remove_box,command= lambda:add(), height="fill", text="Add", grid=[0, 0])
box_pad = Box(add_remove_box, height="fill", width="20", grid=[1, 0])
remove_button = PushButton(add_remove_box, height="fill", text="Remove", grid=[2, 0])

#button group for items
button = PushButton(buttons_box, command= lambda: button_command(0),
                    width="fill", height="fill", text=item_names[0])
button1 = PushButton(buttons_box, command= lambda: button_command(1),
                    width="fill", height="fill", text=item_names[1])
button2 = PushButton(buttons_box, command= lambda: button_command(2),
                    width="fill", height="fill", text=item_names[2])
button3 = PushButton(buttons_box, command= lambda: button_command(3),
                    width="fill", height="fill", text=item_names[3])
button4 = PushButton(buttons_box, command= lambda: button_command(4),
                    width="fill", height="fill", text=item_names[4])
button5 = PushButton(buttons_box, command= lambda: button_command(5),
                    width="fill", height="fill", text=item_names[5])
button6 = PushButton(buttons_box, command= lambda: button_command(6),
                    width="fill", height="fill", text=item_names[6])
button7 = PushButton(buttons_box, command= lambda: button_command(7),
                    width="fill", height="fill", text=item_names[7])
button8 = PushButton(buttons_box, command= lambda: button_command(8),
                    width="fill", height="fill", text=item_names[8])
button9 = PushButton(buttons_box, command= lambda: button_command(9),
                    width="fill", height="fill", text=item_names[9])

#receipt box
receipt_box = Box(right_box, width="fill", height="fill", border=True)
title = Text(receipt_box, text="Current Cart")
for item in items:
        item_quantity = item + " " + str(items[item]) + "x"
        texts.append(Text(receipt_box, text=item_quantity,visible=False))
        

#dispense box
dispense_box = Box(right_box, width="fill", align="bottom")
dispense_button = PushButton(dispense_box, text="Dispense", align="right")

app.display()
