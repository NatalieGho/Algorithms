# PA2 Skeleton Code
# DSA2, spring 2025

def BinarySearchThing(array, min, max, TAs):
    if min == max:  #this is covering the base case
        return min
    mid_value = (min+max)//2
    curr_TAs = 1
    base_weight = 0
    for each in array:
        if base_weight + each <= mid_value:
            base_weight += each
        else:
            curr_TAs += 1
            base_weight = each
    # curr_TAs += 1
    if curr_TAs <= TAs:
        return BinarySearchThing(array, min, mid_value, TAs)
    else:
        return BinarySearchThing(array, mid_value + 1, max, TAs)

def first_function(array, Shifts, TAs):
    min_shift_weight = max(array)
    max_shift_weight = sum(array)
    return BinarySearchThing(array, min_shift_weight, max_shift_weight, TAs)


# This reads in the input from stdin -- you can always assume that the input is valid
test_cases = int(input())
for _ in range(test_cases):
    [s, t] = [int(x) for x in input().split(" ")]
    arr = [int(x) for x in input().split(" ")]
    Shifts, TAs = int(s), int(t) #I added this here for my code
    value = first_function(arr,Shifts,TAs)
    print(value)

