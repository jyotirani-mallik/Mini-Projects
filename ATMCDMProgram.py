balance=10000
pin=1234
name="Jyoti"

# Function for balance check
def check_balance():
    print(f"Your Present acount balance is : Rs {balance}")

#Function for deposit
def deposit():

    global balance

    deposit_amount=float(input("Enter the amount which you want to deposit : "))

    if deposit_amount >= 0:
        balance += deposit_amount
        print(f"Rs {deposit_amount} Successfully deposited !!!") 

        view=input("do you want to see your updated balance(yes/no) :")
        if view == "yes":
            print(f"Your updated acount balance is {balance}")
        elif view =="no":
            print(" ")
        else:
            print("INVALID INPUT !!!")

# Function for withdrawal           
def withdrawal():

    global balance

    withdrawal_amount=int(input("Enter the amount which you want to withdraw : "))

    if withdrawal_amount <= 0:
        print("invalid amount !!!")
    elif withdrawal_amount > balance :
        print("INSUFFICIENT BALANCE")
    else:
        balance -=withdrawal_amount
        print(f"{withdrawal_amount} Successfully withdrawn")
        check=input("do you want to see your updated balance(yes/no) :")
        if check == "yes":
            print(f"Your updated acount balance is {balance}")
        elif check =="no":
            print(" ")
        else:
            print("INVALID INPUT !!!")

#Function for menu            
def menu():
    print("\n======= ATM / CDM Menu =======")
    print("1. Check Balance")
    print("2. Deposit Balance")
    print("3. Withdrawal Balance")    
    print("4. Exit")
    print("=============================")

#Display
print("**********************************")
print("   Welcome to ATM/CDM Machine   ")
print("**********************************")

pin_entered=int(input("Enter your four digit PIN : "))

if pin==pin_entered:
    print(f"Welcome {name}, you have logged in successfully !!!")
    while True:
        menu()
        choice=int(input("Enter the serial number of the transaction you want to perform : "))
        if choice==1:
            check_balance()
        elif choice==2:
            deposit()
        elif choice==3:
            withdrawal()
        elif choice==4:
            print("\n Thank you for using our ATM/CDM \n visit us again ")
            break
        else:
            print("Invalid Choice and Try it again !!!")
else:
    print("Incorrect PIN !!!")    
        
