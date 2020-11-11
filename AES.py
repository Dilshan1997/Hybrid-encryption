from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
message=input("plz enter the message:")
data= bytes(message,'utf-8')
key = b'Sixteen byte key'
cipher = AES.new(key, AES.MODE_EAX)
# a nonce is an arbitrary number that can be used just once in a cryptographic communication. It is similar in spirit to a nonce word, hence the name. It is often a random or pseudo-random number issued in an authentication protocol to ensure that old communications cannot be reused in replay attacks. They can also be useful as initialisation vectors and in cryptographic hash functions.
nonce = cipher.nonce
#print(nonce)
ciphertext, tag = cipher.encrypt_and_digest(data)
#enryption
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
#decrypted
plaintext = cipher.decrypt(ciphertext)


try:
    cipher.verify(tag)

except ValueError:
    print("Key incorrect or message corrupted")