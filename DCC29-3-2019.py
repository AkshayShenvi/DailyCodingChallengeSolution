# This problem was asked by Stripe.
#
# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.
import  sys
arr = [1, 2, 0]

def lowestElement(arr):
    arr_set = set()
    max = 0
    low = sys.maxsize
    for i in arr:
        if i<0:
            continue
        if i>max:
            max=i
        if i not in arr_set:
            if i<low:

                if abs(i-low)>1:
                    missingElement=abs(i-low)
                low = i
                arr_set.add(i)

    if missingElement<max:
        print(missingElement)
    else:
        print(max+1)

lowestElement(arr)