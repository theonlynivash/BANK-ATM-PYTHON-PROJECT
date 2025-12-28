import csv
from datetime import datetime
#=======================================================================================================================
def today():
    return datetime.now().strftime("%d/%m/%Y")
#=======================================================================================================================
def check_user(user_name, password):
    with open('username_password.csv', 'r', newline='') as f:
        data = csv.reader(f)
        data1 = list(data)
        for i  in data1:
            if i[0] == user_name and i[1] == password:
                print('LOGIN SUCCESSFUL !')
                return True
    print("INVALID USERNAME OR PASSWORD!")
    return False
#=======================================================================================================================
def deposit(user_name):
    amount = int(input("ENTER AMOUNT TO DEPOSIT: "))

    with open('saving.csv', 'r', newline='') as f:
        data = list(csv.reader(f))

    for row in data:
        if row[0] == user_name:
            row[1] = str(int(row[1]) + amount)
            new_balance = row[1]
            break
    else:
        print("USER NOT FOUND")
        return

    with open('saving.csv', 'w', newline='') as f:
        csv.writer(f).writerows(data)

    with open(f'{user_name}_th.csv', 'a', newline='') as f:
        csv.writer(f).writerow([today(), "DEPOSIT", amount, new_balance])

    print("DEPOSITED SUCCESSFULLY :)")

#=======================================================================================================================  
def withdraw(user_name):
    amount = int(input("ENTER AMOUNT TO WITHDRAW: "))

    with open('saving.csv', 'r', newline='') as f:
        data = list(csv.reader(f))

    for row in data:
        if row[0] == user_name:
            balance = int(row[1])
            if balance < amount:
                print("INSUFFICIENT BALANCE")
                return
            row[1] = str(balance - amount)
            new_balance = row[1]
            break
    else:
        print("USER NOT FOUND")
        return

    with open('saving.csv', 'w', newline='') as f:
        csv.writer(f).writerows(data)

    with open(f'{user_name}_th.csv', 'a', newline='') as f:
        csv.writer(f).writerow([today(), "WITHDRAW", amount, new_balance])

    print("WITHDRAW SUCCESSFUL :)")

#=======================================================================================================================   
def transfer(sender, receiver):
    amount = int(input("ENTER AMOUNT TO TRANSFER: "))

    with open('saving.csv', 'r', newline='') as f:
        data = list(csv.reader(f))

    sender_found = False
    receiver_found = False

    for row in data:
        if row[0] == sender:
            sender_balance = int(row[1])
            sender_row = row
            sender_found = True
        if row[0] == receiver:
            receiver_balance = int(row[1])
            receiver_row = row
            receiver_found = True

    if not sender_found or not receiver_found:
        print("USER NOT FOUND")
        return

    if sender_balance < amount:
        print("INSUFFICIENT BALANCE")
        return

    sender_row[1] = str(sender_balance - amount)
    receiver_row[1] = str(receiver_balance + amount)

    with open('saving.csv', 'w', newline='') as f:
        csv.writer(f).writerows(data)

    with open(f'{sender}_th.csv', 'a', newline='') as f:
        csv.writer(f).writerow(
            [today(), f"TRANSFER TO {receiver}", amount, sender_row[1]]
        )

    with open(f'{receiver}_th.csv', 'a', newline='') as f:
        csv.writer(f).writerow(
            [today(), f"RECEIVED FROM {sender}", amount, receiver_row[1]]
        )

    print("TRANSFER SUCCESSFUL")

#=======================================================================================================================
def view_transaction_history(user_name):
    try:
        with open(f'{user_name}_th.csv', 'r', newline='') as f:
            th = csv.reader(f)
            print("\nDATE | DETAILS | AMOUNT | BALANCE")
            print("-" * 35)
            for row in th:
                print(" | ".join(row))
    except FileNotFoundError:
        print("\nNO TRANSACTION HISTORY FOUND\n")
#=======================================================================================================================
def change_pin(user_name, password):
    old = input('\nENTER YOUR "OLD" PASSWORD : ')
    if old != password:
        print("WRONG OLD PASSWORD")
        return

    new_pass = input('ENTER YOUR "NEW" PASSWORD : ')

    with open('username_password.csv', 'r', newline='') as f:
        data = list(csv.reader(f))

    for row in data:
        if row[0] == user_name:
            row[1] = new_pass
            break
    else:
        print("USER NOT FOUND")
        return

    with open('username_password.csv', 'w', newline='') as f:
        csv.writer(f).writerows(data)

    print("PIN CHANGED SUCCESSFULLY")
from datetime import datetime
#=======================================================================================================================
def check_balance(user_name):
    with open('saving.csv', 'r', newline='') as f:
        data = list(csv.reader(f))

    for row in data:
        if row[0] == user_name:
            balance = row[1]

            with open(f'{user_name}_th.csv', 'a', newline='') as th:
                csv.writer(th).writerow(
                    [datetime.now().strftime("%d/%m/%Y"),
                     "CHECK BALANCE",
                     "-",
                     balance]
                )

            print("\nYOUR CURRENT BALANCE IS : Rs", balance, "\n")
            return

    print("USER NOT FOUND")
#=======================================================================================================================
def main():
    print('\nWELCOME TO ATM SYSTEM\n')
    is_running = 1
    while is_running:
        user_name = input('ENTER USERNAME : ')
        password = input('ENTER PASSWORD : ')
        user_found = check_user(user_name,password)
        if user_found == True :
            ch = int(input('\n 1) DEPOSIT \n 2) WITHDRAW \n 3) CHECK BALANCE \n 4) TRANSFER \n 5) TRANSACTION HISTORY \n 6) CHANGE PIN \n 7) EXIT \n\n ENTER YOUR CHOICE : '))
            if ch == 1:
                deposit(user_name)
            elif ch == 2:
                withdraw(user_name)
            elif ch == 3:
                check_balance(user_name)
            elif ch == 4 :
                transfer(user_name,input('\nENTER RECIPIENT USERNAME : \n'))
            elif ch == 5:
                view_transaction_history(user_name)
            elif ch == 6:
                change_pin(user_name,password)
            elif ch == 7:
                print('\nTHANK YOU HAVE A BAD DAY :(\n')
                is_running = 0
            else:
                print('\nINVALID CHOICE\n')          
main()