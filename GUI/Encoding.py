#my_str = "hello world"
#my_str_as_bytes = str.encode(my_str)
#print(type(my_str_as_bytes) )# ensure it is byte representation
#my_decoded_str = my_str_as_bytes.decode()
#type(my_decoded_str) # ensure it is string representation
#print(my_str_as_bytes)

#print(ord("b"))#ASCII(only character) - ord function
#print(ord("A"))

# Add each character, and it's ordinal, of user's text input, to two lists
#s = input("Enter value: ")  # this line requires Python 3.x, use raw_input() instead of input() in Python 2.x

#l1=[c for c in s]   # in Python, a string is just a sequence, so we can iterate over it!
#l2=[ord(c) for c in s]

#print(l1)
#print(l2)
def encrypt(message,shift_key):

    result=''
    print('leangth :',len(message))
    for i in range(len(message)):
        letter=message[i]

        if letter.isupper():
            result+=chr((ord(letter)+shift_key-65)%26+65)
        else:
            result += chr((ord(letter) + shift_key - 95) % 26 + 95)
    return result


