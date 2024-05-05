# Programm to solving study exercises
##### To test program you should install librarries used in project
1. get to your IDE terminal
2. write `pip install -r requirements.txt `
3. start `kt3.py`

### Given:

The books.csv file contains a catalog of products in CSV format:

`isbn|title|author|quantity|price `

`978-1-43545-500-9|Python Program for the Absolute Beginner|Michael Dawson|10|18.90
`

`978-0-59600-372-2| XSLT Cookbook|Sal Mangano|15|34.60`

`978-0-32168-056-3| Programming in Python 3|Mark Summerfield|8|27.28`

`978-1-44935-573-9| Learning Python|Mark Lutz|21|34.20`

`978-0-47178-597-2| Ajax For Dummies|Steve Holzner|32|11.80`

`978-1-78439-700-5|Mastering Python Networking|Eric Chou|23|31.49`

`978-8-59037-986-7| Programming in Lua|Roberto Ierusalimschy|12|37.10`

`978-1-78439-658-9| Machine Learning in Java|Bostjan Kaluza|45|34.99`
 
### Task 1
 

It is necessary to implement a function that selects data from the specified file and returns a list of lists of the form:

`[ ['isbn', 'title', 'author', quantity, price], [...], ... ]`
 

**For example, calling a function as:** 

`get_books("books.csv") `
 

**should return the following list of lists:**

 

`[['978-1-43545-500-9', 'Python Code for the Absolute Beginner', 'Michael Dawson', 10, 18.9], [...], ...]
` 

 
### Task 2
 

It is necessary to implement a function that receives the list created in the previous task, selects books with the specified parameter in the name and returns a list of lists of the form:

 

`[ ['isbn', 'title, author', quantity, price], [...], ... `]
 

**For example, calling a function as:** 

`filtered_books(books, "python") `
 

should return the following list of lists (books are selected where there is a python substring in the title):

 

`[['978-1-43545-500-9', 'Python Code for the Absolute Beginner, Michael Dawson', 10, 18.9], [...], ...]
( Note that title and author now represent the same element!)`

 
 
### Task 3
 

Write a function that should take a list as a parameter (the result of the function from the previous task) and return a list of tuples of the form: 

`("isbn", quantity*price)`
 

**For example:**

`[('978-1-43545-500-9', 189.0), ('978-0-59600-372-2', 519.0), (...), ...]`