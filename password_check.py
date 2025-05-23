"""def strong_password(s):

    if len(s) < 8:
        return False
    if not any(char.isdigit() for char in s):
        return False
    if not any(char.islower() for char in s):
        return False
    if not any(char.isupper() for char in s):
        return False
    if not any(char in "~!@#$%^&*()" for char in s):
        return False
    else:
        return True
print(strong_password("Vampire17"))

       """

"""
def is_present(s):
    if any(char.isdigit() for char in s):
       return True
    else:
        return False
print(is_present("71"))
"""
def is_present(s):
    if any(char in "abcdefgh" for char in s):
        return True
    else:
        return False
print(is_present("vAmshi"))    
