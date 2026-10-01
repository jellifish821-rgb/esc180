def drink_coffee():
    global too_much_coffee
    global last_coffee_time
    global last_coffee_time2
    global current_time
    global knols

    if current_time - last_coffee_time2 < 120:
        too_much_coffee = True
    else:
        too_much_coffee = False

    last_coffee_time2 = last_coffee_time # -100 80
    last_coffee_time = current_time # 80

    print(knols)


def study(minutes):
    global current_time
    global too_much_coffee
    global last_coffee_time
    global last_coffee_time2
    global knols

    if too_much_coffee == False:
        if last_coffee_time == current_time:
            knols += 10*minutes
        elif last_coffee_time != current_time:
            knols += 5*minutes

    current_time += minutes

    print(knols)




def initialize():
    global too_much_coffee
    global current_time
    global last_coffee_time
    global last_coffee_time2
    global knols
    too_much_coffee = False
    current_time = 0
    knols = 0
    last_coffee_time = -100
    last_coffee_time2 = -100

if __name__ == "__main__":
    initialize() # start the simulation
    study(60) # knols = 300
    study(20) # knols = 400
    drink_coffee() # knols = 400
    study(10) # knols = 500
    drink_coffee() # knols = 500
    study(10) # knols = 600
    drink_coffee() # knols = 600, 3rd coffee in 20 minutes
    study(10) # knols = 60


