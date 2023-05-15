# In this version I add bonus features
# Add a menu item that allows the user to view all historical transactions
# Assign categories to each transaction
# Add a menu item to allow the user to view all the transactions in a given category
# Provide the user with summary statistics about the transactions in each category
# Keep track of the date and time that each transaction happened
# Allow the user to view all the transactions for a given day
# Hint: Make sure your list of previous transactions includes the timestamp for each
# Allow the user to optionally provide a description for each transaction
# Allow the user to search for keywords in the transaction descriptions, and show all the transactions that match the user's search term
# Allow the user to modify past transactions


import os
import pandas as pd
import numpy as np

def main():

    # initialize balance
    transactions = initialize_transactions()

    # greeting
    print("~~~ Welcome to your terminal checkbook! ~~~\n")

    # run options until user exits
    while True:
        print(
            """What would you like to do?\n
                1) view current balance\n
                2) record a debit (withdraw)\n
                3) record a credit (deposit)\n
                4) exit\n""")
        
        # get and validate input
        while True:

            usr_input = input('Your choice? ')

            if 1 <= int(usr_input) <= 4:
                usr_input = int(usr_input)
                break
            else:
                print(f'Invalid choice: {usr_input}\n')
        
        # run option
        if usr_input == 1:
            view_balance(transactions['balance'])
        elif usr_input == 2:
            withdraw(transactions)     
        elif usr_input == 3:
            deposit(transactions)
        elif usr_input == 4:
            exit_farewell()
            break

    # save_balance into 'balance.txt'
    save_transactions(transactions)

    # exit app
    exit()


# function to intitialize transactions DataFrame
def initialize_transactions():
    # if csv of transactions exists, initialize transactions DataFrame with it
    if os.path.exists('transactions.csv'):
        df = pd.read_csv('transactions.csv')
        return df
    # else initialize transactions DataFrame with balance of 0
    else:
        cols = ['transaction','amount','balance']
        # first row data
        data = pd.Series( np.array([np.nan, np.nan, 0.0]), index=cols) 
        df = pd.DataFrame(columns=cols)
        # Add the row to the DataFrame
        df.loc[0] = data
        return df


# save transactions to csv
def save_transactions(df):
        df.to_csv('transactions.csv', index=False)

# option 1 function: view balance
def view_balance(bal_series, current=True):
    # view current balance
    if current:
        # get last (most recent) balance value
        bal = bal_series[len(bal_series)-1]
        # display balance
        bal_disp = '\nYour current balance is ${:.2f}.\n'.format(\
                        round(abs(bal_series[len(bal_series)-1]), 2))

    # insert '-' if balance is negative
    if bal < 0:
        bal_disp = bal_disp[:25] + '-' + bal_disp[25:]
    print(bal_disp)

# option 2 function: make withdrawal, updates dataframe without assignment
def withdraw(df):
    # withdrawal prompt
    debit = float(input('\nHow much is the debit? $'))
    # calculate new balance
    new_bal = df['balance'][len(df)-1] - debit
    # create row of data for transaction
    data = pd.Series( ['withdrawal', debit * -1, new_bal], index=df.columns)

    # add data to end of transactions
    df.loc[len(df)] = data
    return df

# option 3 function: make deposit, similar to withdraw function, 
# except we add from balance
def deposit(df):
    credit = float(input('\nHow much is the credit? $'))
    new_bal = df['balance'][len(df)-1] + credit
    data = pd.Series( ['deposit', credit, new_bal], index=df.columns) 

    df.loc[len(df)] = data
    return df

# option 4 function: exit app
def exit_farewell():
    # farewell
    print("\nThanks, have a great day!\n")

main()