## 2025 Q1 (b)

'''
if statement - 3 marks
return statements - 3 marks
1 mark general correctness
'''
def evaluate_candy_haul(num_pieces):
    if num_pieces >= 50:
        return "Great Haul!"
    elif num_pieces >= 20 and num_pieces < 50:
        return "Not bad!"
    else:
        return "Try more houses!"

## 2025 Q1 (c)

def get_perfect_squares_for(n):
    array = []
    for idx in range(n): # range -> 0 to n-1
        if idx**2 <= n:
            array.append(idx**2)

    return array

def get_perfect_squares_while(n):
    array = []
    idx = 0
    while idx ** 2 <= n:
        array.append(idx**2)
        idx += 1

    return array

'''
making a list
arithmetic
appending to list
returning list
'''
def get_perfect_squares(n):
    array = []
    for idx in range(n): # range -> 0 to n-1
    # range(5) = [0, 1, 2, 3, 4]
        idx = idx**2
        array.append(idx)

    return array

print(get_perfect_squares(10))
print(get_perfect_squares(25) )
print(get_perfect_squares(30) )
print(get_perfect_squares(0) )

## 2025 Q1 (d)
def below_average(L):
    total = sum(L)
    count = len(L)
    avg   = total / count
    '''
    total  = 0
    count = 0
    for el in L: # goes through each element of L
        total += el
        count += 1
    '''
    array = []
    for el in L:
        if el < avg:
            array.append(el)

    return array

'''
3 marks for avg
2 making and returning
3 marks checking and appending
'''
print(below_average([3, 1, 4, 2, 5]))
print(below_average([40, 10, 30, 20]))
print(below_average([10, 1, 1, 1]))

## 2023 Q7

valid = True
cur_prime = 1 # when we start playing the game, we get 2

def check_next_prime(n):
   global valid
   global cur_prime
   if not valid:
       print("Game is over")
   else:
       current = get_next_prime(cur_prime)
       if n == current:
           cur_prime = current
           print("Correct")
       else:
           valid = False
           print("Incorrect, game over")

# Helper func
def get_next_prime(num):
    # assume num is prime
    number = num
    divisor_count = 0 # arbitrary
    while divisor_count != 2:
        number += 1
        divisor_count = 0
        # divisors of number are beteen 1 and itself
        for idx in range(1, number+1): # [1, 2, 3,...,number]
            if number % idx == 0:
                divisor_count += 1

    return number

'''
get_next_prime(3)
number = 3
div = 3
1st while
number = 4
div = 0, 1, 2, 2, 3
2nd while
number = 5
div = 0, 1, 1, 1, 1, 2
'''

'''
if __name__ == "__main__":
    # Get user unput and play the game
    global valid
    while valid: # while valid == True
        user = int(input("Next prime")) # string -> int
        check_next_prime(user)

'''
while True:
    user = int(input("Next prime")) # string -> int
    check_next_prime(user)


'''
3 marks - global vars + running code
3 marks - check_next_prime handling n
3 marks - calculating/checking the next prime
1 mark correctness
'''

## 2025 Q3

def is_popular(faves, activity):
# dictionary items = {keys : values}

    activities_counts = {}
    for act in faves.values():
        if act in activities_counts:
            activities_counts[act] += 1
            # act_counts[act] = act_counts[act] + 1
        else:
            activities_counts[act] = 0

    act_max = None
    count_max = 0

    for act in activities_counts:
        if activities_counts[act] > count_max:
            act_max = act
            count_max = activities_counts[act]

    return act_max == activity

print(is_popular({"Alice": "trick-or-treating",
"Bob": "pumpkin carving",
"Charlie": "trick-or-treating"},
"trick-or-treating"))

'''
5 marks for getting activity counts
5 marks for comparing activities
5 marks general
'''
## 2025 Q5

user = input("Enter command: ")
commands = ["WALK", "RUN", "END"]
if user in commands:
    if user == "WALK":
        distance = float(input("Enter command:"))

#for el in "10": --> ["1", "0"]


## Lab 5 preview






