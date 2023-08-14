import random
import tkinter as tk

def encrypt(message, key):
    ciphertext = ""
    for i in range(len(message)):
        if message[i].isalpha():
            letter = message[i].upper()
            ciphertext += chr((ord(letter) + ord(key[i]) - 130) % 26 + 65)
        else:
            ciphertext += message[i]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            letter = ciphertext[i].upper()
            plaintext += chr((ord(letter) - ord(key[i]) + 26) % 26 + 65)
        else:
            plaintext += ciphertext[i]
    return plaintext

def generate_key(length):
    key = ""
    for i in range(length):
        key += chr(random.randint(65, 90))
    return key

def encrypt_message():
    message = entry_message.get().strip()
    if not message.isalpha():
        label_result.config(text="Error: message must only contain alphabetic characters.")
        return
    
    key = generate_key(len(message))
    label_key.config(text="Key: " + key)
    
    ciphertext = encrypt(message, key)
    label_result.config(text="Ciphertext: " + ciphertext)

def decrypt_message():
    ciphertext = entry_message.get().strip()
    if not ciphertext.isalpha():
        label_result.config(text="Error: ciphertext must only contain alphabetic characters.")
        return
    
    key = entry_key.get().strip()
    if len(key) != len(ciphertext):
        label_result.config(text="Error: key must be the same length as the ciphertext.")
        return
    
    plaintext = decrypt(ciphertext, key)
    label_result.config(text="Plaintext: " + plaintext)

# create the main window
root = tk.Tk()
root.title("Encryption/Decryption Program")

# create the message label and entry
label_message = tk.Label(root, text="Message:")
label_message.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
entry_message = tk.Entry(root)
entry_message.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

# create the key label and entry
label_key = tk.Label(root, text="Key:")
label_key.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
entry_key = tk.Entry(root)
entry_key.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

# create the encrypt and decrypt buttons
button_encrypt = tk.Button(root, text="Encrypt", command=encrypt_message)
button_encrypt.grid(row=2, column=0, padx=5, pady=5)
button_decrypt = tk.Button(root, text="Decrypt", command=decrypt_message)
button_decrypt.grid(row=2, column=1, padx=5, pady=5)

# create the result label
label_result = tk.Label(root, text="")
label_result.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# start the main event loop
root.mainloop()