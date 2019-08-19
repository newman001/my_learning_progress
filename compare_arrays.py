"""
Description
There is an array of n integers. There are also 2 disjoint sets, A and B, each containing
m integers. You like all the integers in set A and dislike all the integers in set B. Your initial
happiness is 0. For each i integer in the array, if i in A, you add 1 to your happiness. If i in B,
you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness
at the end

Note
Since A and B are sets, they have no repeated elements. However, the array might contain duplicate
elements.

Input format
The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.

Output format
Output a single integer, your total happiness

Sample input
3 2
1 5 3
3 1
5 7

Sample output
1

Explanation
You gain 1 unit of happiness for elements 3 and 1 in set A. You lose 1 unit for 5 in set B.
The element 7 in set B does not exist in the array so it is not included in the calculation:
Hence, the total happiness is 2 - 1 = 1.
"""
n, m = input().split()
array = list(map(int, input().split()[:int(n)]))
A, B = list(map(int, input().split()[:int(m)])), list(map(int, input().split()[:int(m)]))
happiness = 0
for i in array:
    if i in list(set(A) - set(B)):
        happiness += 1
    if i in list(set(B) - set(A)):
        happiness -= 1
print(happiness)
