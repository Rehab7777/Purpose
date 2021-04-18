#create record
#update record
#read record
#delete record
#CRUD
#find a user

import os
user_db_path = "data/user_records/"


def create():
    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(0)
    if does_account_number_exist(account_number):
        return False
    if does_email_exist(email):
        print("User already exists")
        return False
    completion_state=False
    try:
        f = open(user_db_path + str(user_account_number) + ".txt","x")
    except FileExistsError:
        does_file_contain_data = read(user_db_path + str(user_account_number) + ".txt")
        if not does_file_contain_data:
            delete(user_account_number)
        #delete the created file, and print out error then return false
        #print("User already exists")
        #delete(account_number)
    else:
        f.write(str(user_data))
        completion_state=True
    finally:
        f.close()
        return completion_state
    #create a file in the data folder for each user and name it account_number.txt
    #add user details to that file
    #return true
    #if saving to file failed then delete created file

def update(user_account_number):
    print("Update user records.")
    #find user file in the data folder
    #fetch the content of the file
    #update the content of the file
    #save the file
    #return true

def read(user_account_number):
    #find user with the account number & fetch content of the file
    is_valid_account_number = validation.account_number_validation(user_account_number)
    try:
        if is_valid_account_number:
            f = open(user_db_path + str(user_account_number) + ".txt","r")
        else:
            f = open(user_db_path + user_account_number,"r")
    except FileNotFoundError:
        print("The user was not found.")
    except FileExistsError:
        print("The user does not exist.")
    except TypeError:
        print("Invalid account number format.")
    else:
        return f.readline()
    return False
    

def delete(user_account_number):
    print("Delete user account.")
    #find a user with account number & delete the records
    is_deletion_successful = False
    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):
        try:
            os.remove(user_db_path + str(user_account_number) + ".txt")
            is_deletion_successful = True
        except FileNotFoundError:
            print("User was not found.")
        finally:
            return is_deletion_successful
            

def does_email_exist(email):
    #find user's email in the data folder
    all_users = os.listdir(user_db_path)
    for user in all_users:
        user_list = (str.split(read(user, ',')))
        #print(read(user))
        #print("\n")
        if email in user_list:
            return True
    return False

def does_account_number_exist(account_number):
    #find user's account number in the data folder
    all_users = os.listdir(user_db_path)
    for user in all_users:
        if user == str(account_number) + '.txt':
            return True
    return False
    

#create(3011703521,['Rehab' , 'Farag' , 'faragrehab77@yahoo.com' , 'rehab77' , 200])

def authenticated_user(account_number, password):
    if does_account_number_exist(account_number):
        str.split(read(account_number), ',')
    if password == user[3]:
        return user
    return False

#print(read(specific user account to be added))
    
#print(find_email('specific email'))

#prinr(find_account_number(specific number))

#print(read(['one','two'])) #list #gives type error

#print(read({'one':'two'})) #dictionary #returned---> invalid account number, account number has to be 10 digits (from validation)
