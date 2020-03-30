import random, sys, os, math

def collatz(num):
    if num % 2 == 0:
        print(num // 2)
        return(num // 2)
    else:
        print(3*num + 1)
        return(3*num + 1)

print("Enter a number")
num = int(input())

i=0

ret = collatz(num)

while i==0:
    if ret == 1:
        i=1
    else:
        ret = collatz(ret)
        i=0

print("Maths is Fun!")