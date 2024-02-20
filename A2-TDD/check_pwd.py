def check_pwd(pwd):
    if len(pwd) > 7 and len(pwd) < 21:
        
        lowercase_found = False

        for char in pwd:
            if char.islower():
                lowercase_found = True
                break
        
        return lowercase_found
    
    else:
        return False

    