##Q6



def id_popular_candy(faves):
    candies = {}
    for candy in faves.values():
        if candy in candies:
            candies[candy] += 1
        else:
            candies[candy] = 1

    max_num = 0
    for num in candies.values():
        if num > max_num:
            max_num = num

    for candy, num in candies.items():
        if num == max_num:
            return candy

def list_names(faves):
    L = []
    popular_candy = id_popular_candy(faves)
    for kid, candy in faves.items():
        if candy == popular_candy:
            L.append(kid)

    return L

if __name__ == "__main__":
    faves = {"Alice": "Mars", "Bob": "Snickers", "Charlie": "Mars", "Dave": "Coffee time"}
    print(id_popular_candy(faves))
    print(list_names(faves))

##Q7

def zeros(x):
    count = -1
    while True:
        x = x *10
        count += 1
        if x>1:
            return count

print(zeros(0.12))