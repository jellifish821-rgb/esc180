
def compute_pi(num_loops):
    res = 0
    for i in range(num_loops+1):
        leb = ((-1)**i)/(2*i + 1)
        res += leb
    pi = 4*res
    return pi

'''
num_loops = 0
digits_of_pi = 1
while digits_of_pi<5:
    digits_of_pi = len(str(compute_pi(num_loops))) -1
    num_loops +=1

print(compute_pi(num_loops))

for digit in str(compute_pi(num_loops)).replace(".", ""):
    print(digit)
'''


