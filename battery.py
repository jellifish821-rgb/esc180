cur_time = 0
cur_temp = 20
cur_charge = 50
good_battery_health = True
# either 100 or 80, based on battery health
max_charge = 100
def initialize():
    global cur_temp # in degrees Celsius
    global cur_charge # in percentage points
    global cur_time # in minutes
    global good_battery_health

def simulate_activity(activity, int: duration):
    global cur_temp
    global cur_charge
    global cur_time
    global good_battery_health

    if activity == "charge":
        while cur_charge < 100
        if duration_fast_charge_possible() == 0:
            cur_charge += 1
            cur_temp += 0.25
        else:
            for i in range(duration_fast_charge_possible()):
                cur_charge += 3

    elif activity == "use":
        ...
    elif activity == "idle":
        ...
    else:
        pass


def duration_fast_charge_possible():
    charge_time = 0
    mock_cur_temp = cur_temp
    mock_cur_charge = cur_charge
    if (0 < cur_temp < 40) and cur_charge < 80 and good_battery_health == True:
        while cur_charge < 80 and cur_temp < 40:
            charge_time += 1
            mock_cur_temp += 0.5
            mock_cur_charge += 3
    else:
        return 0
    return charge_time



def get_cur_temp():
    global cur_temp
    return float(cur_temp)

def get_cur_charge():
    global cur_charge
    return float(cur_charge)

def get_cur_battery_health():
    global good_battery_health
    return float(good_battery_health)

def charge_time_needed(minutes):
    pass

if __name__ == '__main__':
    initialize()
    print(get_cur_temp())
'''
    print(duration_fast_charge_possible()) # 10
    print(charge_time_needed(50)) # 30
    simulate_activity("charge",30)
    print(get_cur_charge()) # 100
    print(get_cur_temp()) # 30
    simulate_activity("use",50)
    print(get_cur_charge()) # 0
    print(get_cur_temp()) # 80
    simulate_activity("use",10)
    print(get_cur_charge()) # 0
    print(get_cur_temp()) # 70
    simulate_activity("charge",100)
    print(get_cur_charge()) # 100
    print(get_cur_temp()) # 95
    simulate_activity("idle",100)
    print(get_cur_charge()) # 50
    print(get_cur_temp()) # 0
    print(get_cur_battery_health()) # True
    print(duration_fast_charge_possible()) # 10
    simulate_activity("charge",80)
    print(get_cur_charge()) # 90
    print(get_cur_temp()) # 22.5
    print(get_cur_battery_health()) # False
    simulate_activity("use",40)
    print(get_cur_charge()) # 10
    print(get_cur_temp()) # 62.5
    simulate_activity("charge",80)
    print(get_cur_charge()) # 80
    print(get_cur_temp()) # 82.5
    initialize()
    # add
    '''