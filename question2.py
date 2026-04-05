"""
Question 2: Fibonacci 
Write a program to find nth Fibonacci number OR generate series up to n terms
- Handle n=0, n=1, negative inputs
- Show time/space complexity in comments
"""

# Write your solution here

def iterative_fibonacci(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    a,b=0,1
    for _ in range(2,n+1):
        a,b=b,a+b
    return b

def recursive_fibonacci(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

# Accept n from user input

n = int(input("Enter a Number for the Fibonacci Series: "))
print(iterative_fibonacci(n))
