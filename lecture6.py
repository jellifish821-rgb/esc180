'''
a = 10
b = 1
step = -2


for i in range(a, b, step):
    print(i)

def count_while(a, b, step):
    i = a
    if step > 0:
        while i < b:
            print(i)
            i = i + step
    else:
        while i > b:
            print(i)
            i = i + step

print("while loop output:")
count_while(a, b, step)


#log function
 def my_log10(n):
     res = 1
     i = 0
     while res < n:
         res = res*10
         i = i + 1
    return i

print(my_log10(100000))
'''

# infinite loop!
i=0
while True:
    i += 1
    print(i)
