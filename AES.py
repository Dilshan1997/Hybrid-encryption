from Crypto.Cipher import AES
key = b'Sixteen byte key'
cipher = AES.new(key, AES.MODE_EAX)
