#! usr/bin/python3

# Python program to demonstrate
# sys.argv
import sys

add = 0.0

# Getting the length of command
# line arguments
n = len(sys.argv)

for i in range(1, n):
    add += float(sys.argv[i])

print ("the sum is :", add)
