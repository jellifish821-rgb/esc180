def_sum_list2_fast(L, start, end):
    if start == end:
        return 0
    if end == start + 1:
        return l[start]

    mid = (start + end) //2
    return sum _list2fast(L, start, mid) + sum_list2_fast(L, mid, end)


def power_rec(base, exp):
    if exp == 0:
        return 1
    if exp < 0:
        return 1/power_rec(base, -exp)

    return power_rec(base, exp -1)

# what if guarenteed can be expressed with base 2?
def power_rec_fast(base, exp):
    if n ==0:
        return 1
    if n ==1:
        return base

    half_power = power_rec_fast(x, n//2)
    return half_power*half_power
