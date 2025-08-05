'''Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
'''
file_name = 'output.txt'
with open(file_name,'w') as fi_write:
    fi_w = fi_write.write(input("Enter the text write to the file: "))
    msg = (f'Data successfully written to {file_name}.') if fi_w > 0 else ""
    print(msg)
    
with open(file_name,'a+') as fi_app:
    fi_app.write("\n")
    fi_a = fi_app.write(input("\n\nEnter additional text to append: "))
    msg = "Data successfully appended." if fi_a > 0 else ""

with open(file_name,'r') as fi_read:
    fi_r = fi_read.read()
    print(f'\n\nFinal content of {file_name}:\n{fi_r}')
