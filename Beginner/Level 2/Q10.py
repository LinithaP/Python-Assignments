'''
10. We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones.
If n is odd, all piles have an odd number of stones. Each pile must have more stones than the previous pile but as few as possible.
 Write a Python program to find the number of stones in each pile.
 Sample Input: n = 7 Sample Output: Stones in a single pile = [2, 4, 6]
'''

# TODO:the test case gives an odd number and even number of pile?

def stone_pile(n):
    if n % 2 == 0:
        i = 2 #even
    else:
        i = 1

    result = []
    total= n
    while total > 0:
        result.append(i)
        total -= i
        i += 2

    return result
print(stone_pile(8))