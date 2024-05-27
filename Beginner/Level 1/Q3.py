'''. Write a Python program to input marks for five subjects Physics, Chemistry, Biology, Mathematics, and Computer.
Calculate the percentage and grade according to the following:
Percentage >= 90% : Grade A Percentage >= 80% : Grade B Percentage >= 70% : Grade C
Percentage >= 60% : Grade D Percentage >= 40% : Grade E Percentage < 40% : Grade '''

def percentage_calc(marks):
    total = sum(marks)
    percentage = (total/500)*100 #len(marks) in case there are more than 5 subjects

    if percentage >= 90:
        print ("Grade: A Percentage ", percentage)
    elif percentage >= 80:
        print ("Grade: B Percentage ", percentage)
    elif percentage >= 70:
        print ("Grade: C Percentage ", percentage)
    elif percentage >= 60:
        print ("Grade: D Percentage ", percentage)
    elif percentage >= 40:
        print ("Grade: E Percentage ", percentage)
    else:
        print ("Grade: F Percentage ", percentage)

physics = float(input("Enter marks for Physics: "))
chemistry = float(input("Enter marks for Chemistry: "))
biology = float(input("Enter marks for Biology: "))
mathematics = float(input("Enter marks for Mathematics: "))
computer = float(input("Enter marks for Computer: "))

marks = [physics, chemistry, biology, mathematics, computer]
(percentage_calc(marks))
