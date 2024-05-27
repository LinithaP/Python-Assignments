'''4. Write a Python program to find the sum of all odd numbers between two given numbers.
Start = 1, stop = 10 Sum of odd numbers: 25'''

def odd_sum(start,stop):
    result = 0

    for i in range(start,stop+1):
        if i % 2 !=0:
            result +=i
    print(result)
odd_sum(1,10)