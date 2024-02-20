def check_pwd(pwd):
    if len(pwd) > 7 and len(pwd) < 21:
        return True
    else:
        return False
