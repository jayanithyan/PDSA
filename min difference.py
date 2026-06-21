"""Write a function find_Min_Difference(L, P) that accepts a list L of integers and P (positive integer) where the size of L is greater than P. The task is to pick P different elements from the list L, where the difference between the maximum value and the minimum value in selected elements is minimum compared to other differences in possible subset of p elements. The function returns this minimum difference value.
Note - The list can contain more than one subset of p elements that have the same minimum difference value."""


def find_Min_Difference(L, P):
    L.sort()  # Sort the list
    
    min_diff = float('inf')
    
    for i in range(len(L) - P + 1):
        diff = L[i + P - 1] - L[i]
        min_diff = min(min_diff, diff)
    
    return min_diff
L=eval(input(strip()))
P=int(input())
result=find_Min_Difference(L,P)
print(result)