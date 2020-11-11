#import
import main as mn
import hybrid as hy
import secrets
import random
import sys
from Crypto.Cipher import AES


def encryptAES(cipherAESe, plainText):
    return cipherAESe.encrypt(plainText.encode("utf-8"))

def decryptAES(cipherAESd, cipherText):
    dec = cipherAESd.decrypt(cipherText).decode('utf-8')
    print('dec=',dec)
    return dec

def move_text_to_decrypt_box():
    pub, pri = hy.KeyGeneration()
    key = secrets.token_hex(16)
    KeyAES = key.encode('utf-8')
    movingText = encryption_box.get("1.0", mn.tkinter.END)
    cipherAESe = AES.new(KeyAES, AES.MODE_GCM)
    nonce = cipherAESe.nonce
    cipherKey = hy.encrypt(pub, key)
    cipherText = encryptAES(cipherAESe, movingText)

    empty_message="Plz enter something"
    if (len(movingText)>1 ):
        decryption_box.insert("1.0",cipherText)
        encryption_box.delete("1.0", mn.tkinter.END)

    else:
        decryption_box.insert("1.0", empty_message)

    return cipherText,cipherKey,nonce,pri

def move_text_to_encrypt_box():
    cipherText,cipherKey,nonce,pri = move_text_to_decrypt_box()
    print("nonce",nonce)
    print("dec=",cipherText)
    #print("decrypted key=",decriptedKey)
    decryptedKey = ''.join(hy.decrypt(pri, cipherKey))
    encodedDecryptedKey = decryptedKey.encode('utf-8')
    #print("endi code=",encodedDecriptedKey)
    cipherAESd = AES.new(encodedDecryptedKey, AES.MODE_GCM, nonce=nonce)
    #print(cipherAESd)
    decrypted = decryptAES(cipherAESd, cipherText)
    print("Decrypting the message using the AES symmetric key.....")
    print("decrypted message: ")
    print(decrypted)
    encryption_box.insert("1.0",decrypted)
    decryption_box.delete("1.0", mn.tkinter.END)

    #print(len(moving_text))
#create a title
title_label=mn.tkinter.Label(text='                                                           ', font=('times',20 ))
title_label.grid(row=0, column=0)
title_label=mn.tkinter.Label(text='HYC', font=('times',20 ))
title_label.grid(row=0, column=1)
title_label=mn.tkinter.Label(text='                                                            ', font=('times',20 ))
title_label.grid(row=0, column=2)
#encryption_message
encryption_message=mn.tkinter.Label(text='Encryption', font=('times',17),pady=20)
encryption_message.grid(row=1, column=0, sticky=mn.tkinter.W)
#decryption_message
decryption_message=mn.tkinter.Label(text='Decryption', font=('times',17),pady=20)
decryption_message.grid(row=1, column=2, sticky=mn.tkinter.E)

#encryption_box
encryption_box=mn.tkinter.Text(height=10,width=50)
encryption_box.grid(row=2, column=0, sticky=mn.tkinter.W)

#encryption_button
encryption_button=mn.tkinter.Button(text='Encrypt', font=('times',15),pady=10,padx=165,command=move_text_to_decrypt_box)
encryption_button.grid(row=3, column=0, sticky=mn.tkinter.W)
#decryption_box
decryption_box=mn.tkinter.Text(height=10,width=50)
decryption_box.grid(row=2, column=2, sticky=mn.tkinter.E)
#decryption_button
decryption_button=mn.tkinter.Button(text='Decrypt', font=('times',15),pady=10,padx=162,command=move_text_to_encrypt_box)
decryption_button.grid(row=3, column=2, sticky=mn.tkinter.E)
#loop the program
if __name__ == '__main__':
    mn.root_window.mainloop()