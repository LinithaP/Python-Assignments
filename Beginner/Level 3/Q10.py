'''
10. A cafe has N computers. Several customers come to the cafe to use these computers.
 A customer will be serviced only if there is any unoccupied computer at the moment the customer visits the cafe.
 If there is no unoccupied computer, the customer leaves the cafe.
 You are given an integer N representing the number of computers in the cafe and a sequence of uppercase letters S.
  Every letter in S occurs exactly two times.
  The first occurrence denotes the arrival of a customer and the second occurrence denotes the departure of the same customer if he gets allocated the computer.
  You have to find the number of customers that walked away without using a computer.
'''
def customer_count(N,S):
    max_char = 26
    status = [0] * max_char
    result = 0
    occupied = 0

    for i in S:
        idx = ord(i) - ord('A')
        if status[idx] == 0:
            status[idx] = 1
            if occupied < N:
                occupied += 1
                status[idx] = 2
            else:
                result += 1
        else:
            if status[idx] == 2:
                occupied -= 1
            status[idx] = 0

    return result

print(customer_count(3, "GACCBDDBAGEE"))
print(customer_count(1, "ABCBAC"))


