import time
def selection_sort(L):
    #l = len(L)  - 1 k starts at the end
    for k in range(len(L)-1, 0, -1):
        cur_max = L[k]
        loc_max = k
        # iteratre through unsorted portion
        for i in range(k):
            if L[i] > cur_max:
                cur_max = L[i]
                loc_max = i
        #perform swap
        L[k], L[loc_max] = L[loc_max], L[k]
        print("L is now:", L)
#no need to return L, because it mutates the list

def bubble_sort():
    #check adj neighbours starting from beginning of the list
    #out of order? swap
    #keep going until reach end
    #grow sorted list --> each iteration bubbles up the gretes element in unsorted to be the next elemtn of the sorted list
    #best case run time is better than worst time-best - only iterates once

if __name__ == "__main__":
    L = [3,2]
    start = time.perf_counter()
    selection_sort(L)
    end = time.perf_counter()
    print(end-start)



