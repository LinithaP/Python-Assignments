'''2. Write a program that accepts a string as input from the user and calculates the number of digits and letters.
Input: Hello123 Output: Alphabets: 5 & Number : 3'''

def summation(s):
    alphabets = 0
    number = 0
    for i in s:
        if i.isdigit():
            number+=1
        else:
            alphabets +=1
    # return ("Alphabers:", alphabets, " Number: ", number)
    print("Alphabets: ", alphabets)
    print('Number: ', number)
ip = input("Enter input")
(summation(ip))