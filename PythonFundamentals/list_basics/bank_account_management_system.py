# Enhanced Bank Account Management System with Loan Feature

# Initialize lists to hold account data
account_holders = []  # List to store account holder names
balances = []  # List to store corresponding balances
transaction_histories = []  # List to store transaction histories
loans = []  # List to store outstanding loans for each account

MAX_LOAN_AMOUNT = 10000  # Maximum loan amount
INTEREST_RATE = 0.03  # Interest rate for loans


def create_account():
    """Create a new bank account."""
    # 1. Prompt the user for the account holder's name.
    name = input('Write your name: ')
    # 2. Add the new account holder to the list of account holders.
    if name in account_holders:
        return print(f'This name {name} is available')

    account_holders.append(name)
    new_index = account_holders.index(name)
    # 3. Initialize the balance to 0 for the new account.
    balances.insert(new_index, 0)
    # 4. Initialize an empty transaction history for the new account.
    transaction_histories.insert(new_index, [])
    # 5. Initialize the outstanding loan amount to 0.
    loans.insert(new_index, 0)
    # 6. Notify the user of the successful account creation.
    return print(f'Congratulations {name}, you are created your account.')


def deposit():
    """Deposit money into an account."""
    # 1. Prompt the user for the account holder's name.
    deposit_name = input('Write your account name')
    # 2. Check if the account exists in the system.
    if not deposit_name in account_holders:
        return print('Wrong account.')
    # 3. If the account exists, prompt the user for the amount to deposit.
    deposit_index = account_holders.index(deposit_name)
    deposit_sum = float(input('Write sum, which you would like to deposit: '))
    # 4. Update the account's balance with the deposited amount.
    balances[deposit_index] += deposit_sum
    # 5. Log the transaction in the account's transaction history.
    transaction_histories[deposit_index].append(deposit_sum)
    # 6. Display the updated balance to the user.
    return print(f'Your current balance is: {balances[deposit_index]}')
    # 7. If the account does not exist, inform the user.


def withdraw():
    """Withdraw money from an account."""
    # 1. Prompt the user for the account holder's name.
    withdraw_name = input('Write your account name')
    # 2. Check if the account exists in the system.
    if not withdraw_name in account_holders:
        return print('Wrong account.')
    # 3. If the account exists, prompt the user for the amount to withdraw.
    withdraw_index = account_holders.index(withdraw_name)
    withdraw_sum = float(input('Write your sum: '))
    # 4. Check if there are sufficient funds for the withdrawal.
    if withdraw_sum > balances[withdraw_index]:
        return print(f'{withdraw_name} you do not have available {withdraw_sum}')
    # 5. If funds are sufficient, update the balance and log the transaction.
    balances[withdraw_index] -= withdraw_sum
    # 6. Display the updated balance to the user.
    return print(f'{withdraw_name} you current account is {balances[withdraw_index]}')
    # 7. If insufficient funds, inform the user.
    # 8. If the account does not exist, inform the user.


def check_balance():
    """Check the balance of an account."""
    # 1. Prompt the user for the account holder's name.
    check_name = input('Write your account name: ')
    # 2. Check if the account exists in the system.
    if not check_name in account_holders:
        return print('Unknown account')
    # 3. If the account exists, display the current balance.
    return print(f'{check_name} your current balance is: {balances[account_holders.index(check_name)]}')
    # 4. If the account does not exist, inform the user.


def list_accounts():
    """List all accounts and their balances."""
    # 1. Check if there are any accounts in the system.
    if not account_holders:
        return 'There are not any accounts'
    # 2. If there are accounts, loop through each account holder.
    for x in range(len(account_holders)):
        print(f'{account_holders[x]}: balance: {balances[x]}, loan amount: {loans[x]}')
    return
    # 3. Display the account holder's name, balance, and outstanding loan amount.
    # 4. If there are no accounts, inform the user.


def transfer_funds():
    """Transfer funds between two accounts."""
    # 1. Prompt the user for the sender's and recipient's account holder names.
    sender = input('Write your account name')
    if not sender in account_holders:
        return print('Unknown name')
    recipient = input('Write name of recipient')
    if not recipient in account_holders:
        return print('Unknown name')
    # 2. Check if both accounts exist in the system.
    # 3. If both accounts exist, prompt the user for the amount to transfer.
    transfer_sum = float(input('Enter your amount: '))
    # 4. Check if the sender has sufficient funds for the transfer.
    if transfer_sum > balances[account_holders.index(sender)]:
        return print('You do not have enough money')
    # 5. If funds are sufficient, update both balances and log the transactions.
    balances[account_holders.index(sender)] -= transfer_sum
    balances[account_holders.index(recipient)] += transfer_sum
    # 6. Inform the user of the successful transfer.
    return print('Your transaction is successful')
    # 7. If insufficient funds or if either account does not exist, inform the user.


def view_transaction_history():
    """View transaction history for a specific account."""
    # 1. Prompt the user for the account holder's name.
    view_name = input('Write your name: ')
    # 2. Check if the account exists in the system.
    if not view_name in account_holders:
        return print('Unknown name!')
    # 3. If the account exists, display the transaction history.
    if not transaction_histories[account_holders.index(view_name)]:
        return print('You have not transactions')

    return print(f'{view_name} your transaction are: {str.join(', ', transaction_histories[account_holders.index(view_name)])}')
    # 4. If there are no transactions, inform the user.
    # 5. If the account does not exist, inform the user.


def apply_for_loan():
    """Apply for a loan."""
    name = input("Enter the account holder's name: ")

    # Check if the account exists in the system
    if name in account_holders:
        index = account_holders.index(name)  # Find the account index

        # Prompt user for the loan amount they wish to apply for
        loan_amount = float(input(f"Enter the loan amount (max {MAX_LOAN_AMOUNT} leva): "))

        # Check if the loan amount is within the limit
        if loan_amount <= MAX_LOAN_AMOUNT:
            # Update balance and loan amount
            balances[index] += loan_amount
            loans[index] += loan_amount * (1 + INTEREST_RATE)  # Calculate total loan with interest

            print(f"Loan of {loan_amount:.2f} leva approved for {name}. New balance: {balances[index]:.2f} leva.")
        else:
            print(f"Loan amount exceeds maximum limit of {MAX_LOAN_AMOUNT} leva.")
    else:
        print("Account not found.")


def repay_loan():
    """Repay a loan."""
    name = input("Enter the account holder's name: ")

    # Check if the account exists in the system
    if name in account_holders:
        index = account_holders.index(name)  # Find the account index

        # Prompt user for repayment amount
        repayment_amount = float(input(f"Enter repayment amount (Outstanding loan: {loans[index]:.2f} leva): "))

        # Check if the repayment amount is valid
        if repayment_amount <= loans[index]:
            # Update balance and outstanding loan amount
            balances[index] -= repayment_amount
            loans[index] -= repayment_amount

            print(
                f"Repayment of {repayment_amount:.2f} leva accepted for {name}. Remaining loan: {loans[index]:.2f} leva.")
        else:
            print("Repayment amount exceeds outstanding loan.")
    else:
        print("Account not found.")


def display_menu():
    """Display the main menu."""
    print("\n--- Bank Account Management System ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. List Accounts")
    print("6. Transfer Funds")
    print("7. View Transaction History")
    print("8. Apply for Loan")
    print("9. Repay Loan")
    print("10. Exit")

    # Prompt user for their choice
    choice = int(input("Enter your choice: "))
    return choice


def main():
    """Main function to run the banking system."""
    while True:
        choice = display_menu()  # Display the menu and get user choice

        # Process user input based on their choice
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            print("Exiting the system. Goodbye!")
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

    main()


    main()



