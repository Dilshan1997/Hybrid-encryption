#import
import main as mn
import encodings as enc
#logical function


#move the text
def move_text_to_decrypt_box():
    empty_message="Error text box or shifted key is empty,\n"
    moving_text=encryption_box.get("1.0",mn.tkinter.END)
    shifter_key_text=shifter_key_box.get('1.0',mn.tkinter.END)
    if (len(moving_text)>1 and len(shifter_key_text)>1):
        decryption_box.insert("1.0",mn.encrypt(moving_text,int(shifter_key_text)))
        encryption_box.delete("1.0", mn.tkinter.END)

    else:
        decryption_box.insert("1.0", empty_message)

def move_text_to_encrypt_box():
    empty_message = "Error text box or shifted key is empty,\n"
    moving_text = decryption_box.get("1.0", mn.tkinter.END)
    shifter_key_text = shifter_key_box.get('1.0', mn.tkinter.END)
    #checking if the decryption box has an error message
    if empty_message in moving_text:
        decryption_box.delete("1.0",mn.tkinter.END)
    elif len(moving_text)>2:

        encryption_box.insert("1.0", mn.decrypt(moving_text, int(shifter_key_text)))
        decryption_box.delete("1.0", mn.tkinter.END)
    else:
        encryption_box.insert('1.0', empty_message)
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
#shifter_key
shifter_key=mn.tkinter.Label(text="shifter key", font=("time, 16"))
shifter_key.grid(row=1, column= 1)
shifter_key_box=mn.tkinter.Text(height=3,width=5, font=("time, 15"))
shifter_key_box.grid(row=2, column= 1)
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