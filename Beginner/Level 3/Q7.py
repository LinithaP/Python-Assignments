'''
7. Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects.
The dictionary should map the students with their respective subjects.
Let’s see how to do this using for loops and dictionary comprehension.
Input:       [Sam, Alice, Mona] , [Commerce, Science, Computer] Output:   [Sam: Commerce,  Alice: Science , Mona: Computer]
'''

# using for loop

def name_map(student, sub):
    student_sub = {}
    for student, sub in zip(student,sub):
        student_sub[student] = sub
    return student_sub

print(name_map(["Sam", "Alice", "Mona"],["Commerce", "Science", "Computer"]))


#using dictionary comprehension:

def name_mapping(student, sub):
    return {student: sub for student, sub in zip(student, sub)}

print(name_mapping(["Sam", "Alice", "Mona"],["Commerce", "Science", "Computer"]))