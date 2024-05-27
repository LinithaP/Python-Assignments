'''
9. Given an input string, write a function that returns the run length encoded string for the input string.
For Example: Input: wwwwaaadebbbbbw Output: w4a3d1e1b5w1
'''

def run_length(st):
    result = ""
    n = len(st)
    i = 0
    while i < n - 1:
        count = 1
        while i < n - 1 and st[i] == st[i + 1]:
            count += 1
            i += 1
        i += 1

        result += st[i - 1] + str(count)
    if i == n - 1:
        result += st[-1] + "1"

    return result

print(run_length('wwwwaaadebbbbbw'))

