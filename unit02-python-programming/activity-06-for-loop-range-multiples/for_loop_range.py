'''
(1) Write a for loop using range() to print the even numbers from 2 to 10.

(2) Write a program that prints the first 10 multiples of 3 using a for loop and range().
'''


# Part 1: Using the range() function

# Approach 1
for i in range(2,11):
    if(i%2==0):   
        print(f"{i} is even")

# Approach 2
for i in range(2,11,2):
    print(f"{i} is even")

# Part 2: Print the first 10 multiples of 3
        
for i in range(1,11):
    print(f"3*{i} = {i*3}")



'''
Explanation:
    range() is a built-in Python function used to create a sequence of numbers.
    
    It can take three arguments: range(start, stop, step).
    
    The stop value is not included in the output.
    
    for example :
        range(0,3,1)
    
    will give :
        0
        1
        2
    There are three different ways to use range(), depending on how many arguments are passed.
    
    1) If we pass one argument, it is used as stop.
        example:
            range(2)
            
            output:
                0
                1
        Here, Python automatically sets start to 0 and step to 1.
    
    2) If we pass two arguments, they are used as start and stop, respectively.
        example:
            range(-1,2)
            
            output:
                -1
                 0
                 1
        Here, Python uses -1 as start and 2 as stop.
    
    3) If all three arguments are given, they are used as start, stop, and step, respectively.
        example:
            range(-1,4,2)
            
            output:
                -1
                 1
                 3 
        
    
'''


'''
Output:
    2 is even
    4 is even
    6 is even
    8 is even
    10 is even
    
    2 is even
    4 is even
    6 is even
    8 is even
    10 is even

    3*1 = 3
    3*2 = 6
    3*3 = 9
    3*4 = 12
    3*5 = 15
    3*6 = 18
    3*7 = 21
    3*8 = 24
    3*9 = 27
    3*10 = 30
'''


'''
NOTE:
    The question does not explicitly define the starting point for n. This solution assumes n = 1.
'''
