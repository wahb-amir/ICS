'''
You are maintaining a list of favorite books: ["To Kill a Mockingbird", "1984", "The Great Gatsby", "Pride and Prejudice"]. 
(1) Add "Moby Dick". 
(2) Replace "1984" with "Brave New World". 
(3) Remove "The Great Gatsby". 
(4) Merge with ["War and Peace", "Hamlet"]. 
(5) Print the final list.
'''

books = ["To Kill a Mockingbird", "1984", "The Great Gatsby", "Pride and Prejudice"]

# 1) Adding another book by using the append method 

books.append("Moby Dick")

# 2) Replacing 1984 with Brave New World

# Approach 1 
books[1] = "Brave New World"

# Approach 2
target = "Brave New World"
idx = books.index(target)
books[idx] = target

# 3) Remove "The Great Gatsby" using the remove method

books.remove("The Great Gatsby")


# 4) Merge with ["War and Peace", "Hamlet"]

new_books =["War and Peace", "Hamlet"]

books += new_books

# 5) print the final list
print(books)


'''
Explanation:
	First create a list called books that contains the original favorite books.

	To add "Moby Dick" to the end of the list, use the append() method.
	The append() method adds one new item to a list.

	Next replace "1984" with "Brave New World" by using its index position.
	Since "1984" is the second item in the list, its index is 1 because Python
	starts counting list indexes from 0.
  NOTE:
    In the second Approach we are first finding the index for 1984 and then updating it 
    as it avoid guess the index of the item to the removed and help in a list were we don't
    know the index of the item to be removed beforehand
	Then remove "The Great Gatsby" by using the remove() method.
 

	Finally,create another list containing "War and Peace" and "Hamlet".
	merge both lists by using the += operator (list concatenation), which adds the items from the
	second list to the end of the books list.

	The print() function displays the final list of books.
'''

'''
Output:
    ['To Kill a Mockingbird', 'Brave New World', 'Pride and Prejudice', 'Moby Dick', 'War and Peace', 'Hamlet']
'''
