#initializing the system
import random
import validation
import database
from getpass import getpass

database = {}

#user_details = [first_name, last_name, email, password1, 0]

#database={3011703521:['Rehab' , 'Farag' , 'faragrehab77@yahoo.com' , 'rehab77' , 200]}


def account_number_generation():
    return random.randrange(1111111111, 9999999999)
    try:
        account_number = account_number_generation()
    except:
        print("Account generation failed")
        init()





def login():
    print("Login to your account.")
    account_number_from_user =(input("What is your account number?\n"))
    is_account_number_valid= validation.account_number_validation(account_number_from_user)
    if is_account_number_valid:
        #password = input("What is your password?\n")
        password = getpass("What is your password?\n")
        user= database.authenticated_user(account_number_from_user, password)
        #for account_number, user_details in database.items():
            #if (account_number == account_number_from_user)and(user_details[3] == password):
                #bank_operations()
        if user:
            bank_operation(user)
        else:
            print("Invalid account number or password")
            login ()
    else:
        print("Account number is invalid. Make sure your account number is 10 digits and only integers.")
        init()


def init():
    print("Welcome to bank of Rehab!")
    account = int(input("Do you have an account with us? Choose 1 for Yes and 2 for NO\n"))
    if account == 1:
      login()
    elif account == 2:
      registeration()
    else:
      print("You have selected an invalid option.")
      init()

def registeration():
    print("Please create an account.")
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    email = input("What is your email address?\n")
    #password = input("Create a password.\n")
    password = getpass("Create a password.\n") 
    account_number_generation()
    #database[account_number]=[first_name, last_name, email, password1, 0]
    
    is_user_created=database.create()
    if is_user_created:
        print(f"Your account number is {account_number}")
        print("You have created an account successfully!")
        login()
    else:
        print("Something went wrong, please try again")
        registeration()


def get_current_balance (user_details):
    return user_details[4]


def bank_operations(user):
    print("Welcome %s %s " % (database[0], database[1]))
    selected_option = int(input("What would you like to do?(1) Deposit, (2)Withdrawal, (3)Logout, (4) Exit.\n"))
    
    if selected_option == 1:
      deposit_operation ()
    elif selected_option == 2:
      withdrawal_operation ()
    elif selected_option == 3:
      logout()
    elif selected_option == 4:
      exit()
    else:
      print("Invalid option selected")
      bank_operations()

def deposit_operation():
  print(f"Your current balance is ${get_current_balance (user_details)}")
  new_deposit=int(input("How much would you like to deposit?\n"))
  new_balance= new_deposit + get_current_balance(user_details)
  print(f"Your new balance is ${new_balance}")
  bank_operations()

def withdrawal_operation():
  print(f"Your current balance is ${get_current_balance (user_details)}") 
  new_withdrawal=int(input("How much would you like to withdraw?\n"))
  new_balance= get_current_balance(user_details) - new_withdrawal
  print(f"Your new balance is ${new_balance}")
  bank_operations() 

def logout ():
  login ()

def exit():
  print("Thank you for choosing our service.")

init ()

