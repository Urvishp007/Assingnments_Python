'''Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
'''
try:
    file_name = 'sample.txt'
    with open(file_name,'r') as fi:
        fi_read = fi.readlines()
        n = 1
        for i in fi_read:
            print(f'Line {n}: {i.strip()}')
            n += 1
except FileNotFoundError:
    print(f'Error: The file {file_name} was not found')
