# AAABBCCCCAAAA
#more compactly?
# A3B2C4A4

a_dec = ["a", "a", "a", "b"]
a_enc = [("a", 3), ("b", 1)]

def encode(s):
    result = []
    if len == 0:
        return result

    count = 1
    for i in range(len(s) - 1):
    # len(s) - 1 : avoid stepping out of bounds
        if s[i] == s[i+1]:
            count += 1
        else:
            result.append((s[i], count))
            count = 1

    result.append((s[-1], count))

    return result

b = encode(a_dec)
print(b)

def decode(encoded):
    result = []
    for item in encoded:
        char = item[0]
        count = item[1]

        for i in range(count):
            result.append(char)

        # or result.extend(char*count)

    return result

a = decode(a_enc)
print(a)

