import os

def main():

    # initialize balance
    balance = initialize_balance()

    # greeting
    print("~~~ Welcome to your terminal checkbook! ~~~\n")

    # run app (options) until user exits
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
            view_balance(balance)
        elif usr_input == 2:
            balance = withdraw(balance)     
        elif usr_input == 3:
            balance = deposit(balance)
        elif usr_input == 4:
            exit_farewell()
            break

    # save_balance into 'balance.txt'
    save_balance(balance)

    # exit app
    exit()


# check if string is a float
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


# if balance saved (in .txt), initialize balance to this, 
# else it equals 0. Function returns balance
def initialize_balance():
    if os.path.exists('balance.txt'):
        with open('balance.txt', 'r') as f:
            text = f.read()
            if is_float(text):
                return float(text)
            else:
                return 0
    else:
        return 0


# new balance saved and overwrites previous
def save_balance(balance):
    with open('balance.txt', 'w') as f:
        f.write('{:.2f}'.format(round(balance, 2)))

# option 1 function: view balance
def view_balance(balance):
    bal_disp = '\nYour current balance is ${:.2f}.\n'.format(round(abs(balance), 2))
    if balance < 0:
        bal_disp = bal_disp[:25] + '-' + bal_disp[25:]
    print(bal_disp)

# option 2 function: make deposit
def deposit(balance):
    credit = float(input('\nHow much is the credit? '))
    balance += credit
    return balance

# option 3 function: make withdrawal
def withdraw(balance):
    debit = float(input('\nHow much is the debit? '))
    balance -= debit
    return balance

# option 4 function: exit app
def exit_farewell():
    # farewell
    print("\nThanks, have a great day!\n")


# The application should persist between times that it is run.

#  Consider creating a file where each line in the file
#  represents a single transaction

main()