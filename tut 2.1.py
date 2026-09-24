current_value = 0
memory = current_value
previous_value = memory

def display_current_value():
    print("Welcome to the calculator program.")
    print(f"Current Value: {current_value}")

def add(to_add):
    global current_value
    global previous_value
    previous_value = current_value
    current_value += to_add
    return current_value

def mult(to_mult):
    global current_value
    global previous_value
    previous_value = current_value
    current_value = current_value*to_mult
    return current_value

def div(to_div):
    global current_value
    global previous_value
    previous_value = current_value
    current_value = current_value/to_div
    return int(current_value)

def save():
    global current_value
    global memory
    memory = current_value

def recall():
    global current_value
    global memory
    current_value = memory
    display_current_value()

def undo():
    global current_value
    global previous_value
    current_value, previous_value = previous_value, current_value
    display_current_value()


if __name__ == "__main__":
    display_current_value()
    add(5)
    display_current_value()
    add(10)
    display_current_value()
    undo()
    undo()







