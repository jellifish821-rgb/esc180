string = "stressed"
rs = ""
for i in range(len(string)):
    rs = rs + string[-(i+1)]

print(rs)