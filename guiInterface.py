from guizero import App, Text, Box, PushButton, Window, TextBox

from hardware.servocontroller import ServoController
from time import sleep
import RPi.GPIO as GPIO
from hx711 import HX711
item_names = ["1", "2", "3", "4",
              "5", "6", "7", "8", "9"]
prices = [1.00,1.15,1.45,2.00,0.00,0.00,0.00,0.00,0.00]
calories = [5,7,10,15,0,0,0,0,0]
servo_calibrations = [5/16] * 9
servo_speeds = [1] * 9
servoToggleStates = [1] * 9
print(servoToggleStates)
global item_index
item_index = 0
global dispenser_index
dispenser_index = 0
global password
password = "password"
global items
texts = []
buttons = []
GPIO.setmode(GPIO.BCM)
global hx
hx = HX711(dout_pin=5, pd_sck_pin=6)
hx.set_scale_ratio(184.7111111111111)

servoController = ServoController()

def button_command(index):
    global item_index
    item_index = index
    item_name.value = "Selected: " + item_names[item_index]
    item_price.value = "Price: " + str(prices[item_index]) + "$"
    item_cals.value = "Calories: " + str(calories[item_index])

def dispenser_select(index):
    global dispenser_index
    dispenser_index = index
    item_dispenser_map.value = "Dispensor " + str(dispenser_index+1)
    curr_name.value = "Current Item: " + item_names[dispenser_index]
    curr_price.value = "Current Price: " + str(prices[dispenser_index]) + "$"
    curr_cals.value = "Current Caloriess: " + str(calories[dispenser_index])
    curr_calibration.value = servo_calibrations[dispenser_index]

def make_map():
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
    total_price = 0.0
    total_cals = 0
    global servoToggleStates
    global hx
    weight = hx.get_weight_mean()
    print("Before reading " + str(weight))
    for i in range(len(item_names)):
        total_price += float(prices[i]) * items[item_names[i]]
        total_cals += int(calories[i]) * items[item_names[i]]
        if items[item_names[i]] > 0:
            for j in range(items[item_names[i]]):
                servoController.setServoThrottle(i, servo_speeds[i] * servoToggleStates[i])
                sleep((servo_calibrations[i]))
                servoController.setServoThrottle(i, 0.0)
                sleep(1/16)
                servoToggleStates[i] *= -1
        items[item_names[i]] = 0
        texts[i].hide()
    weight2 = hx.get_weight_mean()
    ratio = weight2 - weight
    print("After reading " + str(weight2))
    print("Difference " + str(ratio) + "\n")
    price.value = "Total Cost: " + str(total_price) + "$"
    callories.value = "Total Calories: " + str(total_cals)
    dispense_view.show()

def edit():
    password_view.show(wait=True)

def back():
    global items
    items = make_map()
    manager_view.hide()

def back_pw():
    password_view.hide()

def back_dp():
    dispense_view.hide()

def change(name, price, cals):
    if name != "":
        curr_name.value = "Current Item: " + name
        item_names[dispenser_index] = name
        edit_item_input.value = ""
        buttons[dispenser_index].text = name;
    if price != "":
        curr_price.value = "Current Price: " + str(price) + "$"
        prices[dispenser_index] = float(price)
        edit_price_input.value = ""
    if cals != "":
        curr_cals.value = "Current Calories: " + str(cals)
        calories[dispenser_index] = int(cals)
        edit_cals_input.value = ""


def minus(arr, text, rate):
    if arr[dispenser_index] - rate < rate:
        return
        
    arr[dispenser_index] -= rate
    text.value = arr[dispenser_index]
    if rate == 0.1:
        text.value = round(arr[dispenser_index],1)
    

def plus(arr, text, rate):
    if rate == 0.1 and arr[dispenser_index] + rate > 1:
        return
    arr[dispenser_index] += rate
    text.value = arr[dispenser_index]
    if rate == 0.1:
        text.value = round(arr[dispenser_index],1)

def test_calibration():
    servoController.setServoThrottle(dispenser_index, servo_speeds[dispenser_index])
    sleep((servo_calibrations[dispenser_index]))
    servoController.setServoThrottle(dispenser_index, None)

def input(pin, number):
    pin += number

def confirm():
    if(password_input.value == password):
        password_view.hide()
        manager_view.show(wait=True)
        password_input.value = ""
        warning_text.value = ""
    else:
        warning_text.value = "Incorrect Password"
        

app = App(title="Customizable Food Dispenser")
#Make map with item names as keys and quantity as values starting from 0
items = make_map()

#manager view window
manager_view = Window(app, title="Change Dispensers")
manager_view.hide()
dispenser_list = Box(manager_view, align="left", height="fill")
right_box_m = Box(manager_view, align="right", height="fill", width="fill")

#Display current information and input box for new item name
item_dispenser_map = Text(
    right_box_m, text="Dispensor " + str(dispenser_index+1))
curr_name = Text(right_box_m, text="Current Item: " + item_names[dispenser_index])
curr_price = Text(right_box_m, text="Current Price: " + str(prices[dispenser_index]) + "$")
curr_cals = Text(right_box_m, text="Current Caloriess: " + str(calories[dispenser_index]))
input_box = Box(right_box_m, layout="grid")
edit_item = Text(input_box, text="Edit Item: ", grid=[0, 0])
edit_item_input = TextBox(input_box, grid=[1, 0], width=20)
edit_price = Text(input_box, text="Edit Price: ", grid=[0, 1])
edit_price_input = TextBox(input_box, grid=[1, 1], width=20)
edit_cals = Text(input_box, text="Edit Cals: ", grid=[0, 2])
edit_cals_input = TextBox(input_box, grid=[1, 2], width=20)
#super scuffed invocation of change to update the current window
change_button = PushButton(
    right_box_m, command=lambda: change(edit_item_input.value, edit_price_input.value, edit_cals_input.value), text="Change")

box_pad = Box(right_box_m, width="fill", height="10")

#calibration
calibrate_title = Text(right_box_m, text="calibration")
calibrate_box = Box(right_box_m, layout="grid", align="top")
minus_button = PushButton(calibrate_box, command=lambda: minus(servo_calibrations, curr_calibration, 1/16), text="-", grid=[0,0])
curr_calibration = Text(calibrate_box, text=servo_calibrations[dispenser_index], grid=[1,0])
plus_button = PushButton(calibrate_box, command=lambda: plus(servo_calibrations, curr_calibration, 1/16), text="+", grid=[2,0])

speed_box = Box(right_box_m, layout="grid", align="top")
sminus_button = PushButton(speed_box, command=lambda: minus(servo_speeds, curr_speed, 0.1), text="-", grid=[0,0])
curr_speed = Text(speed_box, text=round(servo_speeds[dispenser_index],1), grid=[1,0])
splus_button = PushButton(speed_box, command=lambda: plus(servo_speeds, curr_speed, 0.1), text="+", grid=[2,0])
stest_button = PushButton(right_box_m, command=lambda: test_calibration(), text="test calibration")

#back and change buttons in manager view
buttons_box_m = Box(right_box_m, align="bottom")
back_button = PushButton(
    buttons_box_m, command=lambda: back(), text="Back")

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

password_view = Window(app, title="Password")
password_view.hide()

global password_input

password_text = Text(password_view, text="Password: ")
password_input = TextBox(password_view, width=20)
warning_text = Text(password_view, text="")

#back and confirm buttons in password view
bot_box = Box(password_view, layout="grid", align="bottom")
back_button = PushButton(bot_box, command=lambda: back_pw(), text="Back", grid=[0,0])
box_pad = Box(bot_box, height="fill", width="50", grid=[1, 0])
box_pad = Box(bot_box, height="fill", width="50", grid=[2, 0])
confirm_button = PushButton(bot_box, command=lambda: confirm(), text="Confirm", grid=[3, 0])

#container format
buttons_box = Box(app, align="left", height="fill", width="fill")
right_box = Box(app, align="right", height="fill", width="fill")
detail_box = Box(right_box, width="fill")

#item add/remove box i.e. detail box
item_name = Text(detail_box, text="Selected: " + item_names[item_index])
item_price = Text(detail_box, text="Price: " + str(prices[item_index]) + "$")
item_cals = Text(detail_box, text="Calories: " + str(calories[item_index]))
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
buttons = [button,button1,button2,button3,button4,button5,button6,button7,button8]

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

dispense_view = Window(app, title="Dispensed", visible=False)
#weight = Text(dispense_view, text="Weight: "+str({round(0.00, 2)}))
price = Text(dispense_view, text="Price: "+str({round(0.00,2)}))
callories = Text(dispense_view, text="Calories: "+str(0))
back_button = PushButton(dispense_view, command=lambda: back_dp(), text='Back')


app.display()
