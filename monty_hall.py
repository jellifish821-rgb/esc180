import random

def simluate_monty_hall(num_trials):
    stay_win = 0
    switch_win = 0

    for i in range(num_trials):
        car_door = random.randint(1,3)
        player_choice = random.randint(1,3)

        if car_door == player_choice:
            stay_win += 1
        else:
            switch_win += 1

    print("totoal number of trials", num_trials)
    print("stay win: ", stay_win)
    print("switch win:", switch_win)

if __name__ == "__main__":
    simluate_monty_hall(1000)