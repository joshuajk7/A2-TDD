def check_pwd(pwd):
    if len(pwd) > 7:
        return True
    
    if len(pwd) > 20:
        return False