'''
Write an if-elif-else statement to check if a number is positive, negative, or zero.
'''


num = int(input("Enter a number: "))

if num > 0:
    print(f"{num} is a positive number")
elif num == 0:
    print(f"{num} is zero")
else:
    print(f"{num} is negative")
    

'''
output:

activity-04-sign-checker $ python3 sign_checker.py 
    Enter a number: 2
    2 is a positive number
    
activity-04-sign-checker $ python3 sign_checker.py 
    Enter a number: 0
    0 is zero
    
activity-04-sign-checker $ python3 sign_checker.py 
    Enter a number: -12
    -12 is negative
'''
