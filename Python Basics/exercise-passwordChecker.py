username = input("what is your username? ")
password = input("choose a password ")

password_length = len(password)
hidden_password = '*' * password_length

print(f'{username}, your password {password} is {hidden_password} letters long ')

