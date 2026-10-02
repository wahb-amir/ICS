'''
Given a list [10, 20, 30, 40, 50, 60, 70, 80]
a tuple ("Math", "Science", "English", "History", "Geography")
and a string "Python Programming":
(1) access & print the third element of each;
(2) slice elements index 2-5 from the list and tuple; 
(3) slice characters index 7 to end of the string; 
(4) use negative indexing to print the last two elements of the list and tuple;
(5) use negative slicing to print characters from the second-last to the last character of the string
'''

num = [10, 20, 30, 40, 50, 60, 70, 80]
subjects = ("Math", "Science", "English", "History", "Geography")
s = "Python Programming"

# 1) print the third elm of each
print("Step 1\n")
print(num[2])
print(subjects[2])
print(s[2])
print("\nStep 2\n")
# 2) slice from 2-5 in list and tup 
print(num[2:6])
print(subjects[2:6])
print("\nStep 3\n")
# 3) index 7 to end of the string
print(s[7:])

# 4) last two elm of list and tup using negative idx
print("\nStep 4\n")
print(num[-2:])
print(subjects[-2:])

# 5) print second-last and last char from the string
print("\nStep 5\n")
print(s[-2:])


'''
Explanation:
	Python starts counting indexes from 0. This means the third element has
	index 2, so num[2], subjects[2], and s[2] print the third element of each
	sequence.

	Slicing is written as [start, stop, step].

	start is the index where the slice begins. The item at this index is
	included in the result.

	stop is the index where the slice ends. The item at this index is not
	included in the result. Therefore, [2:6] includes indexes 2, 3, 4, and 5.
	This is why [2:6] is used to get the elements from index 2 through index 5.

	step tells Python how many positions to move each time. If step is not
	written, Python uses a default step of 1 and moves one position at a time.
	For example, [2:6:1] gives the same result as [2:6].

	The start and stop values can be left out. In s[7:], the slice starts at
	index 7 and continues to the end of the string. In num[-2:] and
	subjects[-2:], the slice starts at the second-last element and continues
	to the end, so it prints the last two elements.

	Negative indexes count from the end of a sequence. The index -1 refers to
	the last element, and -2 refers to the second-last element. Therefore,
	s[-2:] prints the second-last and last characters of the string.
'''


'''
Output:
	Step 1

    30
    English
    t

    Step 2

    [30, 40, 50, 60]
    ('English', 'History', 'Geography')

    Step 3

    Programming

    Step 4

    [70, 80]
    ('History', 'Geography')

    Step 5

    ng
'''
