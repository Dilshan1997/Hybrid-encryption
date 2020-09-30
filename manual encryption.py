def machine():
    key='abcdefghijklmnopqrtuvwxyz !'
    value=key[-1]+key[0:-1]
    print(value)
    encryptDict = dict(zip(key,value))
    print(encryptDict)
    decryptDict=dict(zip(key,value))
    message=input('enter the message:')
    mode=input("plz enter the mode:Encrypt(E) or Decrypt(D)")
    if mode.upper()=='E':
        newMessage=''.join([encryptDict[letter] for letter in message.lower()])
    elif mode.upper()=='D':

        newMessage = ''.join([decryptDict[letter] for letter in message.lower()])

    else:
        print("plz enter a correct choice")

    return newMessage

print(machine())