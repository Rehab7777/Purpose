#validation
def account_number_validation (account_number_from_user):
    if account_number_from_user:
        
            try:
                int(account_number_from_user)
                if len(str(account_number_from_user))==10:
                    return True
                #else:
                    #print("Account number has to be 10 digits.")
                    #return False 
            except ValueError:
                #print("Invalid account number. Account number should be integer.")
                return False
            except TypeError:
                #print("Invalid account number.")
                return False
        

    #else:
       #print("Account number is a required field.")
    return False 
    
