'''
Define functions that take a list of numbers and return the maximum value in the list.
'''

# Approach 1: Use Python's built-in max() function.

def find_max(nums):
    return max(nums)

# Approach 2: Find the maximum value manually.

def find_max_2(nums):
    maximum = float('-inf')
    for num in nums:
        if num > maximum:
            maximum = num
    return maximum


numbers = [1,2,-2,6.6]

print(f"The max number is : {find_max(numbers)}")
print(f"The max number is : {find_max_2(numbers)}")


'''
Output:
    The max number is : 6.6
    The max number is : 6.6
'''


'''
Explanation:
    max() is a built-in Python function that returns the largest item in an iterable.
    
    Examples:
     1)
        numbers = [1,2,-2,6.6]  
        max(numbers)
        returns 6.6.
     2)
        The max() function can also take multiple numbers (integers or floats) as arguments:
        max(12,6,3)
        It returns 12.
     3)
        The max() function can also take a string as input because strings are iterable:
        max("abc") 
        It returns 'c'.
        
        Python iterates over the characters in the string and compares them lexicographically.
        Since 'c' comes after 'a' and 'b', max("abc") returns 'c'.
        
        You can verify this using:
        print("a" > "b")
            False
        print("a" < "b")
            True

        
    In find_max_2(), we find the maximum value manually. First, we create a
        variable to store the current maximum value:
    
            maximum = float('-inf')
    
        float('-inf') represents negative infinity. Starting with this value
        ensures that any number in the list will be greater than the initial value.
    
        We then loop through the list. If the current number is greater than
        maximum, we update maximum with that number. After the loop finishes, we
        return maximum.
    
        For example, when we call find_max_2(numbers), Python passes the value of
        numbers to the nums parameter. The function then checks each number in the
        list and keeps the largest one.
'''
