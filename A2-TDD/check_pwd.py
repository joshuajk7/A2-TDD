def check_pwd(pwd):
    if len(pwd) > 7 and len(pwd) < 21:
        
        lowercase_found = False
        uppercase_found = False
        digit_found = False

        for char in pwd:
            if char.islower():
                lowercase_found = True
            elif char.isupper():
                uppercase_found = True
            elif char.isdigit():
                digit_found = True
                
         
        if not (lowercase_found and uppercase_found and digit_found):
            return False
        
        return True
    
    else:
        return False

    