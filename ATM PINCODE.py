# ATM Withdrawal 
Correct_pin = "1234"
balance = 5000
# Number of allowed attempts
Max_attempts= 3

def verify_pin():
    attempts = 0

    while attempts < Max_attempts:
        entered_pin = input("Please enter your PIN: ")

        if entered_pin == Correct_pin:
            print("PIN accepted. Access granted.")
            return True
        else:
            attempts += 1
            print(f"Incorrect PIN. You have {max_attempts - attempts} attempts left.")

    print("Too many incorrect attempts. Access denied.")
    return False

def withdraw_amount(balance):
    try:
        amount = float(input("Enter the amount to withdraw: "))

        if amount <= 0:
            print("Invalid amount entered. Please enter a positive amount.")
        elif amount > balance:
            print(f"Insufficient funds. Your current balance is {balance:.2f}.")
        else:
            balance -= amount
            print(f"Withdrawal successful! Your new balance is {balance:.2f}.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

    return balance

# Run the ATM process
if verify_pin():
    balance = withdraw_amount(balance)
