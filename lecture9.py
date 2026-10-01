def num_factors(n, k):
    count = 0
    while (n%k ==0):
        count += 1
        n = n//k

def trailing_zeros_faster():
    count_factor5 = 0
    for i in range (1, n+1):
        count_factor5 + = num_factors(i,5)

    return count_factor5


def trailing_zeros_fastest():
    count_factor5 = 0
    skip_by = 5

    while skip_by <=n:
        count_factor5 += n//skip_by
        skip_by *= 5

        return count_factor5

## matching
usernames = [a, b, c]
passwords = [one, two, three]

def login
    if username not in username:
        return False
    ind = usernames.index(username)
    correct_psw = passwords[ind]

    if password == correct_password:
        return True
    else:
        return False

# return password == passwords[usernames.index(username)]

## loop login
def login_loop():
    while True:
        username = input("user: ")
        password = input("password: ")

        if login(username, password) == True:
            break