'''
2. Write a program to count the lines in a file “demo.txt”
'''

def count_lines(file_path):
    with open(file_path, 'r') as file:
        count = 0
        for i in file:
            count +=1
    return count
file_path = 'C:/Users/linitha/Desktop/doc.txt'
print(count_lines(file_path))