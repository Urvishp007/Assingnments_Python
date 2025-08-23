'''Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.'''
std_mrk = {'Ram' : 32,
           'Ravan' : 45}
nm = input("Enter the the student's name: ")
marks = int(input(f"{nm}'s marks: "))
std_mrk[nm] = marks
find = input("Enter the the student's name: ")
check = find in std_mrk
if(check == True):
    print('Student Found.')
else:
    print('Student not found.')