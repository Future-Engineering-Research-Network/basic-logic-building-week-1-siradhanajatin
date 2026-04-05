"""
Question 3: YOUR ORIGINAL PROBLEM (Bonus 30 points)
Create your own problem of similar difficulty to Q1 & Q2
Rules:
1. Must be 100% original (no copying from anywhere)
2. Same difficulty level  
3. Include clear problem statement + sample I/O
4. Best 3 creative problems get bonus points!

Problem: Reverse Integer. If the integer is negative then the negative of reverse of it's absolute value is the answer 

Write your original problem + solution below:
"""

def reverse_integer(n):
    res=0
    if n<0:
        res = int(str(n)[1:][::-1]) * -1
    else:
        res = int(str(n)[::-1])
    return res
