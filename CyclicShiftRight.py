# CyclicShiftRight.py
# by Prometheus111
value = input("Integer data only: ")    #type the integer data
N = int(value)                          #your input data to variable N
A = [number for number in range(0, N)]  #filling the array A from 0 to the specified variable minus 1
print('Source array:', A)               #output the source array
number = 0                              #cyclic shift right algorithm
while number < len(A) / 2:
    temp = A[number]
    A[number] = A[-number - 1]
    A[-number - 1] = temp
    number = number + 1
print('Final array:', A)                #output the final array
# Enjoy learning new things! Prometheus111 helps you with your studying!
# https://github.com/Prometheus111 
