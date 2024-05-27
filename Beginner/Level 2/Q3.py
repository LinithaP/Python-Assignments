'''
3. Given an array of N integers and an integer K,
find the number of pairs of elements in the array whose sum is equal to K.
Sample Input: arr = [1, 2, 3, 4, 5], k = 6 Sample Output: Pair count: 2
'''

def pair_count(arr, k):
    d = {}
    count = 0

    for i in arr:
        pair = k -i
        if pair in d:
            count+= d[pair]

        d[i] = d.get(i,0) +1

    return count
print(pair_count([1, 2, 3, 4, 5],6))

