"""
Question 1: Manual List Operations
Write a Python program to perform basic list operations WITHOUT using built-in functions:
- Find length, append, insert, remove, search, max/min
"""

# Write your solution here

def length_of_list(lst):
    count=0
    for _ in lst:
        count+=1
    return count

def add_in_list(lst, n):
    lst[length_of_list(lst)+1]=n

def insert_in_list(lst, pos, n):
    new_list=lst+[0]
    for i in range(length_of_list(new_list)):
        if i<pos:
            new_list[i]=lst[i]
        elif i==pos:
            new_list[i]=n
        else:
            new_list[i]=lst[i-1]
    lst[:]=new_list

def remove_from_list(lst, n):
    pos=0
    for i in range(length_of_list(lst)):
        if lst[i]==n:
            pos=i
            break
    new_list=lst[:pos]+lst[pos+1:]
    lst[:]=new_list

def search(lst, n):
    for i in range(length_of_list(lst)):
        if lst[i]==n:
            return i

def maxima(lst):
    high=0
    for i in range(length_of_list(lst)):
        if lst[i]>high:
            high=lst[i]
    return high

def minima(lst):
    low=lst[0]
    for i in range(length_of_list(lst)):
        if lst[i]<low:
            low=lst[i]
    return low

# Test your functions with sample lists


