'''
Write a Python program using a while loop.
prints even numbers and counts the odd numbers from 1 to 20.
'''


odd_counter = 0
n = 1
while n <= 20:
    if n%2==0:
        print(f"{n} is even")
    else:
        odd_counter +=1
    n +=1
    
print(f"There are {odd_counter} odd number from 1 to 20")


'''
output:
    2 is even
    4 is even
    6 is even
    8 is even
    10 is even
    12 is even
    14 is even
    16 is even
    18 is even
    20 is even
    There are 10 odd number from 1 to 20
'''


'''
Explanation:
    The odd_counter variable is responsible for counting the odd numbers.
    The variable n count the number of iteration for the while loop.
    
    in the while loop we check if n is still less then equal to 20 
    to make sure we only run till 20 iteration
    
    then using the if else structure we check if the number is even or odd
    if the number is even we print the value using the print statement 
    else we update the odd_counter and then print it at the end
    
NOTE:
    We can also update the value of n to control the range of the numbers
    
    
'''
