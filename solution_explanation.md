# Solution Explanation - [YOUR NAME]

## Question 1: Manual List Operations
**Approach**: 
Length of List: a "for loop" iterates over the list and a counter counts for every iteration

Add in List: create a new list and add the old list and the new item

Insert in List: - create a new list with an additional element
- insert elements into the new list from the original list till the insert position
- for the position of insertion, insert the needed element
- for the iterations after the inserted position, copy out the remaining elements from the original list

Remove from List: - find the position of element to be removed 
- use list slicing to slice till the position and skip it

Search: - use iterations to find the position

Maxima: - iterate over all the numbers and check for the larger value

Minima: - iterate over all the numbers and check for the lower value

**Time Complexity**: 
- Length: O(n)
- Append: O(1) 
- Insert: O(n)
- etc...

**Space Complexity**: O(1)

**Edge Cases**: 
- Empty list
- Single element
- Not found

## Question 2: Fibonacci
**Approach**: 
Iterative: - store a and b values as 0 and 1
- for every iteration change a into b and b into a+b
- at the end of all the iterations it prints the required fibonacci series

Recursive: - call the funciton till the number is turned into either addition of 0 or 1 in the decision tree

**Time Complexity**: O(n)
**Space Complexity**: O(1)

**Edge Cases**: n=0, n=1, negative n

## Question 3: My Original Problem
**Problem**: 
Reverse Integer. If the integer is negative then the negative of reverse of it's absolute value is the answer 

**Sample Input**:


**Sample Output**:


**Approach**: 
If a negative number is input -> it first takes the integers absolute value, turns it into a string, reverses the string and again turns it into an integer and multiplies the final answer with -1

If positive number is input -> turns the integer into a string and then reverse it and again turn it into an integer 

**Time**: O(?), **Space**: O(?)

**Why Original**: 
Not unique, solved it on Leetcode but it had a 32 bit signed integer unit case also. Not for this level. I took just the reversing part. 
