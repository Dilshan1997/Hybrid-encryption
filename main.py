import secrets
import RSA
def main():
    print("Genarate RSA public and private key")
    pub=RSA.keyGenaration()
    print(pub)