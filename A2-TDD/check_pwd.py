def check_pwd(pwd):
    if len(pwd) > 7 and len(pwd) < 21:
        
        lowercase_found = False
        uppercase_found = False

        for char in pwd:
            if char.islower():
                lowercase_found = True
            if char.isupper():
                uppercase_found = True
                break
        
        if not uppercase_found or not lowercase_found:
            return False
        
        return True
    
    else:
        return False

    