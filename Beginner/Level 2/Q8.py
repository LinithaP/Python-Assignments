"""
8. Write a Python function that counts the number of vowels in a given string.
 Sample Input: string = "Hello, World!" Sample Output: Number of vowels: 3
"""

def count_vowels(st):
    vowels ="aeiouAEIOU"

    v = [i for i in st if i in vowels]

    return ("Number of volwes: ", len(v))
print(count_vowels("Hello, World!" ))