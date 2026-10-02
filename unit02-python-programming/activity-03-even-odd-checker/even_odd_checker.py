'''
Write an if-else statement and a short-hand if-else statement.
check if a number is even or odd, and print the appropriate message.
'''

num = int(input("Enter a number: "))

# Using if-else statment

if (num%2==0):
    print(f"{num} is a even number")
else:
    print(f"{num} is a odd number")
    
# Using short hand if-else statment

print(f"{num} is a even number") if (num%2==0) else print(f"{num} is a odd number")


'''
Output:

Enter a number: 58
    58 is a even number
    58 is a even number
    
activity-03-even-odd-checker $ python3 even_odd_checker.py 

Enter a number: 27
    27 is a odd number
    27 is a odd number
'''
