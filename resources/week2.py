"""Complexity
The complexity of an algorithm is a function describing the efficiency of the algorithm in terms of the amount of input data. There are two main complexity measures of the efficiency of an algorithm:

Space complexity

The space complexity of an algorithm is the amount of memory it needs to run to completion.

Generally, space needed by an algorithm is the sum of the following two components:

Fixed part() - Size of code

Variable Part() - Depend on input size, to store in memory

Total Space 

Time complexity

The time complexity of an algorithm is the amount of computer time it needs to run to completion. Computer time represents the number of operations executed by the processor.

Time complexity calculated in three types of cases:

Best case
Average case
Worst Case"""


"""
Growth rate of functions
The number of operations for an algorithm is usually expressed as a function of the input.

For Example:

s = 0 #1
for i in range(n): #n+1
    for j in range(n): #n(n+1)
        s = s + 1 #n^2
print(s)#1
Function for given code is :


Ignore all the constant and coefficient just look at the highest order term in relation to . So  is proportional to 

 

Notations to represent complexity
The notation are mathematical notations that are commonly used to describe the time complexity of an algorithm or the upper and lower bounds of how an algorithm's running time grows as the input size grows.

Big-Oh() - Upper bound:

Big  notation describes the upper bound of an algorithm's running time. Specifically, we use the notation  to describe the maximum growth rate of an algorithm's running time. This means that the algorithm's running time will not grow faster than some constant multiple of  as the input size grows.

Omega() - Lower bound:

Omega notation, on the other hand, describes the lower bound of an algorithm's running time. Specifically, we use the notation  to describe the minimum growth rate of an algorithm's running time. This means that the algorithm's running time will not grow slower than some constant multiple of as the input size grows.

Theta() - Tightly bound:

Theta notation describes both the upper and lower bounds of an algorithm's running time. Specifically, we use the notation  to describe the tight bound of an algorithm's running time. This means that the algorithm's running time will grow at the same rate as some constant multiple of  as the input size grows.
"""

