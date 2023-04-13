def genmaster():
    from cryptography.fernet import Fernet
    master =  Fernet.generate_key() # Generating new master_key
    return master

def encrypt(psswd, master):
    from cryptography.fernet import Fernet
    fernet = Fernet(master) # creating fernet object.
    enc_psw = fernet.encrypt(bytes(psswd, 'utf-8')) # encrypting password.
    return enc_psw.decode('utf-8')

def decrypt(dec, master):
    from cryptography.fernet import Fernet
    fernet = Fernet(master)
    dec_psw = fernet.decrypt(bytes(dec, 'utf-8'))
    return dec_psw.decode('utf-8')