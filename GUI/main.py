import tkinter
#encryption function
def encrypt(message,shift_key):

    result='\n'
    print('length :',len(message))
    for i in range(len(message)):
        letter=message[i]
        if letter.isupper():

            result += chr((ord(letter) + shift_key - 65) % 26 + 65)

        else:
            result += chr((ord(letter) + shift_key - 95) % 26 + 95)
    return result

#decryption function
def decrypt(message,shift_key):

    result='\n'
    print('length :',len(message))
    for i in range(len(message)):
        letter=message[i]

        if (letter.isupper()):
            result += chr((ord(letter) - shift_key - 65) % 26 + 65)
        else:
            result += chr((ord(letter) - shift_key - 95) % 26 + 95)
    return result
class MainWindow(tkinter.Tk):

    """" This is the main window, a child class of tkinter"""
    def __init__(self):
        super().__init__()
        """"The main window properties"""
        # main window title
        self.title('hyc')
        # main window size
        self.geometry('900x500')
        # main window colour
        self.configure(background='light grey')


root_window = MainWindow()
if __name__== "__main__":
    root_window.mainloop()


