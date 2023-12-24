
# Alt School Fall Semester DE Exams Hands on Project


## Overview:

This Python script provides a simple implementation of an Expense Tracker using classes. This consist of two main classes: Expense and ExpenseDatabase. The Expense class represents an individual expense, while the ExpenseDatabase class manages a collection of expenses.


### Expense Class:
#### Attributes:

     id : A unique identifier generated using the uuid module.
*

    title :  The title or description of the expense.
    
*

    amount : The timestamp of when the expense was created in UTC format.

*

    created_at : The timestamp of when the expense was created in UTC format.

*
  
    updated_at : The timestamp of when the expense was last updated in UTC format.  


#### Methods :

	   __init__(self, title, amount):

•	Initializes a new Expense instance with the provided title and amount.

•	Generates a unique ID.

•	Sets created_at and updated_at timestamps to the current UTC time.

        update(self, title=None, amount=None):

•	Updates the expense with the provided title and/or amount.

•	Updates the updated_at timestamp.

•	Returns a message indicating the successful update.

•	to_dict(self):

•	Returns a dictionary representation of the expense.

         __repr__(self):

•	Returns a string representation of the expense.


### ExpenseDatabase Class:

#### instance of the class: 

•	expenses: A list to store instances of the Expense class.
Methods

•	__init__(self):

•	Initializes an empty list to store expenses.


•	Adds an expense to the list.

    add_expense(self, expense):

•	Prints a success message.


•	Removes an expense with the specified ID from the list.

    remove_expense(self, expense_id):

•	Prints a success message.

•	Retrieves an expense by its ID.

    get_expense_by_id(self, expense_id):

•   Retrieve an expense by title.

    get_expense_by_title(self, expense_title):

Returns a dictionary representation of the expense.

•	Retrieves expenses with a specific title.

•	Returns a list of dictionary representations of matching 
expenses.

    to_dict(self):

•	Returns a list of dictionary representations of all expenses.






## installations:

* Python 3 was installed as this code is compatible with it.
* Vscode (visual enviroment) was choosen for easy implementation of the code.
* Git was easily installed for smooth remote repository to github.

## Usage:

This demonstrates creating an expenses, adding them to the ExpenseDatabase, updating an expense, removing an expense, and retrieving expenses from the database.This can be adapted and integrated, more functionality can be added based on specific requirements.


## Clone:
Repository can be clone to youyr local machine with the following steps:
* Open your terminal or command prompt
* Type the 'cd' command on the terminal to navigate ( or specify a local where repository will be clone to on the local machine)

      cd [location on local machine]   

* type the git clone command, space and Path to the repository to be clone on the local machine

      git clone [Path for the repository]

This is authomatically clone as required.


## Run Code:

Steps to run the code:

* Python is installed on the machine.

* Installed Visual Studio Code, from VSCode's official website.

* Installed python Extensions view 


* Open the Python file (with the code for the poject)to run in VSCode.

* In the top menu, find the Run option. This will run your Python script.

* The output of your code will be displayed in the "Terminal" tab at the bottom of VSCode


## License:

MIT License

Copyright (c)   [2023]   [Idiyeli Sunday]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

### Author Info: 

Twitter : https://twitter.com/idiyeli

linkedin : https://www.linkedin.com/in/idiyeli-sunday-8182b259/



