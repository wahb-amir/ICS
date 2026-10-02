'''
Create a Python module named calculator.py ,
with two functions: add(a, b) and subtract(a, b). 
Then write a main.py script that imports the module.
(1) prints the result of adding 15 and 8
(2) prints the result of subtracting 10 from 25.
'''

from calculator import add, subtract


print(f"15 + 8 = {add(15, 8)}")
print(f"25 - 10 = {subtract(25, 10)}")


'''
Explanation:
	The calculator.py file is a Python module because it contains reusable
	functions that can be imported into another Python file.
'''


'''
Output:
	15 + 8 = 23
	25 - 10 = 15
'''

