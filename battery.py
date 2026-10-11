
def initialize():
    global cur_temp # in degrees Celsius
    global cur_charge # in percentage points
    global cur_time # in minutes
    global good_battery_health
    global max_charge
    global overcharge_times

    cur_time = 0 # in minutes
    cur_temp = 20
    cur_charge = 50
    good_battery_health = True
    # either 100 or 80, based on battery health
    max_charge = 100
    overcharge_times = [0,0]


def simulate_activity(activity, duration):
    global cur_temp
    global cur_charge
    global cur_time
    global good_battery_health
    global max_charge
    global overcharge_times

    if activity == "charge":
        fast_charge_duration = duration_fast_charge_possible() #in minutes
        slow_charge_duration = duration - fast_charge_duration #in minutes

        #only fast charge
        if fast_charge_duration >= duration:
            cur_charge += 3 * duration
            cur_temp += 0.5 * duration
            cur_time += 1 * duration

        #fast then slow charge or slow only slow charge
        if fast_charge_duration < duration:
            #fast charge until not possible
            cur_charge += 3 * fast_charge_duration
            cur_temp += 0.5 * fast_charge_duration
            cur_time += 1 * fast_charge_duration


            for i in range(round(slow_charge_duration*6)): #update loops every 6th of a minute

                #check for overcharge
                if cur_charge == 90:
                    #record time of overcharge
                    overcharge_times.append(cur_time)
                    #check if overcharged 3 times within the past hour
                    if (overcharge_times[-1] - overcharge_times[-3] < 360) and (overcharge_times[-3] > 0):
                        good_battery_health = False

                if good_battery_health == False:
                    max_charge = 80


                #updates stats for each 6th of a minute
                if cur_charge < max_charge:
                    cur_charge += 1/6
                    cur_time += 1/6
                    cur_temp += 0.25/6

    elif activity == "use":
        for i in range(duration):
            cur_time += 1

            if cur_charge > 0:
                cur_charge -= 2
                cur_temp += 1
                if cur_charge < 0:
                    cur_charge = 0

            elif cur_charge == 0:
                cur_temp -= 1


    elif activity == "idle":
        for i in range(duration):
            cur_time += 1

            if cur_charge > 0:
                cur_charge -= 0.5

            if cur_temp > 0:
                cur_temp -= 1

    else:
        pass

# Return duration of time that fast charging is possible
def duration_fast_charge_possible():
    global cur_temp
    global cur_charge
    global mock_cur_charge

    charge_time = 0
    mock_cur_temp = cur_temp #Mock used to avoid updating true status, which is need for activity
    mock_cur_charge = cur_charge
    if (0 <= cur_temp < 40) and cur_charge < 80 and good_battery_health == True: #Checks all fast charge conditions
        while mock_cur_charge < 80 and mock_cur_temp < 40: #Loops while conditions met
            if mock_cur_charge == 78: #case correction for 78% charge
                charge_time += (2/3)
                mock_cur_temp += 0.5*(2/3)
                mock_cur_charge += 2
            elif mock_cur_charge == 79: # case correction for 79% charge
                charge_time += 1/3
                mock_cur_temp += 0.5*(1/3)
                mock_cur_charge += 1
            elif mock_cur_temp == 39.75: # case correction for 39.75 degreees
                charge_time += 0.5
                mock_cur_temp += 0.5/2
                mock_cur_charge += 3/2
            else: #otherwise, updates as usual
                charge_time += 1
                mock_cur_temp += 0.5
                mock_cur_charge += 3
    else:
        return 0
    return charge_time #Return duration of mock charge session as a float


def get_cur_temp():
    global cur_temp
    return float(cur_temp)

def get_cur_charge():
    global cur_charge
    return float(cur_charge)

def get_cur_battery_health():
    global good_battery_health
    return good_battery_health

# Return the duration needed for charging to enable use for a specified duration
def charge_time_needed(minutes):
    global cur_charge
    global max_charge

    total_charge_needed = minutes*2
    charge_difference = total_charge_needed - cur_charge

    if charge_difference <= 0:
        return 0
    elif total_charge_needed > max_charge:
        return None
    else:
        duration_slow_charge = total_charge_needed - 80
        charge_time = duration_fast_charge_possible() + duration_slow_charge
        return charge_time

if __name__ == '__main__':
    initialize()
    cur_charge = 52
    print(duration_fast_charge_possible())
    print(charge_time_needed(40))
    simulate_activity("charge", 10)
    print(get_cur_charge())

'''
    print(get_cur_temp())
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
