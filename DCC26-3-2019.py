#Created By Akshay Shenvi

arr=[10, 15, 3, 7]
k=10
diff_set=set()
# def funct():
#     for i in arr:
#         for j in range(arr.index(i)+1,len(arr)):
#                 if i+arr[j]==k:
#                     print(i+arr[j])
#                     return True
# funct()

def funct():
    for i in arr:
        diff=abs(i-k)
        if diff in diff_set:
            print(i,diff)
            return True
        else:
            diff_set.add(i)




funct()