# imports
# identifying user
users = ["admin"]
pswds = ["12345"]
user = input("User: ")
# auth user
if user in users:
    main_pswd = input("Password for ({}): ".format(user))
    if main_pswd == pswds[0]:
        auth = True
        print("You are now logged in!")
    else:
        auth = False
        print("Incorrect password!")
else:
    auth = False
    print("The user does not exist!")
# accessing program functions
if auth:
    pass
else:
    print("Program closed!")