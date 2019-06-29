#Good morning! Here's your coding interview problem for today.

#This problem was asked by Apple.

#Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
from threading import Timer
def job_scheduler(f,n):
    t = Timer(n, f)
    t.start()

def f():
    print("Some Function")

n=10
n=n/1000
job_scheduler(f,n)