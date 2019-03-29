# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?
#Created By Akshay Shenvi

arr=[10, 15, 3, 7]
k=10
diff_set=set()
#-----------Brute Force Method with Time Complexity O(n)^2--------
# def funct():
#     for i in arr:
#         for j in range(arr.index(i)+1,len(arr)):
#                 if i+arr[j]==k:
#                     print(i+arr[j])
#                     return True
# funct()
#----------Optimized with Time Complexity O(n)
def funct():
    for i in arr:
        diff=abs(i-k)
        if diff in diff_set:
            print(i,diff)
            return True
        else:
            diff_set.add(i)




funct()