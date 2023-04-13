# imports
import sys
import connect
import hashpass

while True:
    inicio = input("""Welcome to GerenciaKey!
    1 - Login
    2 - Sign in
    3 - Exit
    Make your choice: """)
    if inicio == '1':
        break
    elif inicio == '2':
        print("Escolheu 2!")
        pass
    else:
        print("Good bye!")
        sys.exit()

# auth user
auth = False
users = ["admin", "aaa"]
pswds = ["12345", "111"]
user = input("User: ")
if user in users:
    main_pswd = input("Password for ({}): ".format(user))
    if main_pswd in pswds:
        auth = True
        print("You are now logged in!")
    else:
        auth = False
        print("Incorrect password!")
else:
    auth = False
    print("The user does not exist!")

# accessing program functions
master = hashpass.genmaster()
enc_teste = []
if auth:
    enc_teste.append(hashpass.encrypt(pswds[0], master))
    print(enc_teste)
    dec_teste = hashpass.decrypt(enc_teste[0], master)
    print(dec_teste)
else:
    print("Program closed!")