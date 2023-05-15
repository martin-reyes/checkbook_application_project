# Python Checkbook App Project

**Project Requirements at the bottom of the page**

- MVP (Minimum Viable Product): [`py_project.py`](https://github.com/martin-reyes/checkbook_application_project/blob/main/py_project.py) meets minimum requirements. The balance is stored in `.txt` everytime the program is run. No historical record of previous balances or transactions are kept as the new balances overwrite the previous ones. 

- [`py_project_b.py`](https://github.com/martin-reyes/checkbook_application_project/blob/main/py_project_b.py) is an updated version that reads, stores, and saves transactions into a csv. The `pandas` and `numpy` libraries are used to make this process more efficient and visually pleasing.

- [`py_project_bonus.py`](https://github.com/martin-reyes/checkbook_application_project/blob/main/py_project_bonus.py) is an extension or `py_project_b.py` that includes bonus features listed below. Pandas DataFrame manipulation and indexing are primarily used to achieve this.


<div style="border: 1px solid black;"></div>



### Command Line Checkbook Application

You will create a command line checkbook application that allows users to track their finances with a command line interface.

### Project Requirements

- Build a .py file that will be run from the command line.

- When run, the application should welcome the user, and prompt them for an action to take:

    - view current balance
    - add a debit (withdrawal)
    - add a credit (deposit)
    - exit

- The application should notify the user if the input is invalid and prompt for another choice.

- The application should persist between times that it is run.

- Example, if you run the application, add some credits, exit the application and run it again, you should still see the balance that you previously created. In order to do this, your application will need to store its data in a text file. Consider creating a file where each line in the file represents a single transaction.

- Utilize functions to call the balance, debit, credit, and exit

### Bonus Features

**Attempt these features only if you have completed the basic application.**

In no particular order, things to try:

-  Add a menu item that allows the user to view all historical transactions
- Assign categories to each transaction
    - Add a menu item to allow the user to view all the transactions in a given category
    - Provide the user with summary statistics about the transactions in each category
- Keep track of the date and time that each transaction happened
    - Allow the user to view all the transactions for a given day
    - Hint: Make sure your list of previous transactions includes the timestamp for each
- Allow the user to optionally provide a description for each transaction
    - Allow the user to search for keywords in the transaction descriptions, and show all the transactions that match the user's search term
- Allow the user to modify past transactions