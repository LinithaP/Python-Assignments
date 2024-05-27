'''
7. Write a Python program to check if a string is an anagram of another string.
string1 = "listen", string2 = "silent" Output: True
'''

def anagram(string1, string2):

    # return sorted(string1) == sorted(string2)

    if len(string1) != len(string2):
        return False

    d1, d2 = {}, {}

    for i in string1:
        d1[i] = d1.get(i,0) +1

    for i in string2:
        d2[i] = d2.get(i,0) +1

    return d1 == d2
print(anagram("listen", "silent"))