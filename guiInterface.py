from guizero import App, Text, Box, PushButton, Window, TextBox

item_names = ["green", "red", "purple", "brown",
              "yellow", "blue", "pink", "orange", "black", "white"]
prices = [0,0,0,0,0,0,0,0,0,0]
weights = [0,0,0,0,0,0,0,0,0,0]
callories = [0,0,0,0,0,0,0,0,0,0]
global item_index
item_index = 0
global dispenser_index
dispenser_index = 0
global password
password = "password"

texts = []

def button_command(index):
    global item_index
    item_index = index
    item_name.value = "Selected: " + item_names[item_index]

def dispenser_select(index):
    global dispenser_index
    dispenser_index = index
    item_dispenser_map.value = "Dispensor " + str(dispenser_index+1)
    curr_name.value = "Current Item: " + item_names[dispenser_index]

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
    if(items[item_names[item_index]] > 0):
        items[item_names[item_index]] = items[item_names[item_index]]-1
    if(items[item_names[item_index]] == 0):
        texts[item_index].hide()
    texts[item_index].value = item_names[item_index] + " " + str(items[item_names[item_index]]) + "x"
    
def dispense():
    for i in range(len(item_names)):
        items[item_names[i]] = 0
        texts[i].hide()
    dispense_view.show()

def edit():
    password_view.show(wait=True)

def back():
    manager_view.hide()

def back_pw():
    password_view.hide()

def change():
    manager_view.hide()

def input(pin, number):
    pin += number

def confirm():
    if(password_input.value == password):
        password_view.hide()
        manager_view.show(wait=True)

app = App(title="Customizable Food Dispenser")

#Make map with item names as keys and quantity as values starting from 0
items = make_map(item_names)

#manager view window
manager_view = Window(app, title="Change Dispensers")
manager_view.hide()
dispenser_list = Box(manager_view, align="left", height="fill")
right_box_m = Box(manager_view, align="right", height="fill", width="fill")

#Display current information and input box for new item name
item_dispenser_map = Text(
    right_box_m, text="Dispensor " + str(dispenser_index+1))
curr_name = Text(right_box_m, text="Current Item: " +
                 item_names[dispenser_index])
input_box = Box(right_box_m, layout="grid")
edit_item = Text(input_box, text="Edit Item: ", grid=[0, 0])
edit_item_input = TextBox(input_box, grid=[1, 0], width=20)

#back and change buttons in manager view
buttons_box_m = Box(right_box_m, layout="grid", align="bottom")
back_button = PushButton(
    buttons_box_m, command=lambda: back(), text="Back", grid=[0, 0])
box_pad = Box(buttons_box_m, height="fill", width="50", grid=[1, 0])
box_pad = Box(buttons_box_m, height="fill", width="50", grid=[2, 0])
change_button = PushButton(
    buttons_box_m, command=lambda: change(), text="Change", grid=[3, 0])

#button group for items
dispensor1 = PushButton(dispenser_list, command=lambda: dispenser_select(0),
                     width="fill", height="fill", text="Dispenser 1")
dispensor2 = PushButton(dispenser_list, command=lambda: dispenser_select(1),
                     width="fill", height="fill", text="Dispenser 2")
dispensor3 = PushButton(dispenser_list, command=lambda: dispenser_select(2),
                     width="fill", height="fill", text="Dispenser 3")
dispensor4 = PushButton(dispenser_list, command=lambda: dispenser_select(3),
                     width="fill", height="fill", text="Dispenser 4")
dispensor5 = PushButton(dispenser_list, command=lambda: dispenser_select(4),
                     width="fill", height="fill", text="Dispenser 5")
dispensor6 = PushButton(dispenser_list, command=lambda: dispenser_select(5),
                     width="fill", height="fill", text="Dispenser 6")
dispensor7 = PushButton(dispenser_list, command=lambda: dispenser_select(6),
                     width="fill", height="fill", text="Dispenser 7")
dispensor8 = PushButton(dispenser_list, command=lambda: dispenser_select(7),
                     width="fill", height="fill", text="Dispenser 8")
dispensor9 = PushButton(dispenser_list, command=lambda: dispenser_select(8),
                     width="fill", height="fill", text="Dispenser 9")
dispensor10 = PushButton(dispenser_list, command=lambda: dispenser_select(9),
                     width="fill", height="fill", text="Dispenser 10")

password_view = Window(app, title="Password")
password_view.hide()

global password_input
global pin
pin = ""

password_text = Text(password_view, text="Password: ")
password_input = TextBox(password_view, text=pin, width=20)

#back and confirm buttons in password view
bot_box = Box(password_view, layout="grid", align="bottom")
back_button = PushButton(bot_box, command=lambda: back_pw(), text="Back", grid=[0,0])
box_pad = Box(bot_box, height="fill", width="50", grid=[1, 0])
box_pad = Box(bot_box, height="fill", width="50", grid=[2, 0])
confirm_button = PushButton(bot_box, command=lambda: confirm(), text="Confirm", grid=[3, 0])

#container format
buttons_box = Box(app, align="left", height="fill")
right_box = Box(app, align="right", height="fill", width="fill")
detail_box = Box(right_box, width="fill")

#item add/remove box i.e. detail box
item_name = Text(detail_box, text="Selected: " + item_names[item_index])
add_remove_box = Box(right_box, layout="grid")
add_button = PushButton(add_remove_box,command= lambda:add(), height="fill", text="Add", grid=[0, 0])
box_pad = Box(add_remove_box, height="fill", width="50", grid=[1, 0])
box_pad = Box(add_remove_box, height="fill", width="50", grid=[2, 0])
remove_button = PushButton(add_remove_box, command= lambda:remove(), height="fill", text="Remove", grid=[3, 0])

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
dispense_box = Box(right_box, layout="grid")
edit_buton = PushButton(dispense_box, command=lambda: edit(), text="Edit Items", grid=[0, 0])
box_pad = Box(dispense_box, height="fill", width="50", grid=[1, 0])
box_pad = Box(dispense_box, height="fill", width="50", grid=[2, 0])
dispense_button = PushButton(dispense_box, command=lambda: dispense(), text="Dispense", grid=[3, 0])

dispense_view = Window(app, title="Dispensed")
dispense_view.hide()
weight = Text(dispense_view, text="Weight: "+str({round(0.00, 2)}))
price = Text(dispense_view, text="Price: "+str({round(0.00,2)}))
callories = Text(dispense_view, text="Calories: "+str(0))

app.display()
