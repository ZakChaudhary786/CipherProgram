from tkinter import *
from math import gcd

# Define alphabet
alphabet_e = {'a': '01', 'b': '02', 'c': '03', 'd': '04', 'e': '05', 'f': '06', 'g': '07', 'h': '08', 'i': '09',
              'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18',
              's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26', ' ': '32'}

# Define alphabet for decryption
alphabet_d = {n: c for c, n in alphabet_e.items()}


# Generate encryption keys, e, and d
def generate_keys(p, q):
    # Part of public key
    n = p * q

    # Part of private key
    N0 = (p-1) * (q-1)

    # Part of public key
    # Find e: first integer relatively prime to N0
    for i in range(2, N0):
        if gcd(i, N0) == 1:
            e = i
            break

    # Part of private key
    # Find d: multiplicative inverse of e % N0
    for i in range(0, N0):
        if ((e * i) % N0) == 1:
            d = i
            break

    return n, e, d


# Encrypt character
def encrypt(char, N, e):
    return str((int(char) ** e) % N).zfill(2)


# Decrypt character
def decrypt(char, N, d):
    return str((int(char) ** d) % N).zfill(2)


# Split word into characters
def split(word):
    return [char for char in word]


# Encrypt message
def encrypt_message(msg, N, e):
    # Messages
    plaintext = msg.lower().split()
    encrypted = []

    # Encrypt message
    for word in plaintext:
        # Split word into characters
        chars = split(word)

        # Create list of encrypted characters
        encrypted_chars = [encrypt(alphabet_e[char], N, e) for char in chars]

        # Add encrypted word to list
        encrypted_word = " ".join(encrypted_chars)
        encrypted.append(encrypted_word)

    # Join encrypted words with space characters
    encrypted = f" {encrypt(alphabet_e[' '], N, e)} ".join(encrypted)

    return encrypted


# Decrypt message
def decrypt_message(msg, N, d):
    # Messages
    encrypted = msg.split()
    decrypted = []
    plaintext = []

    # Decrypt
    for char in encrypted:
        decrypted.append(decrypt(char, N, d))

    # Decipher message
    for char in decrypted:
        plaintext.append(alphabet_d[char])

    plaintext = "".join(plaintext)

    return plaintext

def encrypt_message_button():
    # Get values from plaintext textbox
    plaintext = plaintext_textbox.get("1.0", END)

    # Generate keys
    p = 101
    q = 211
    N, e, d = generate_keys(p, q)

    # Encrypt message
    encrypted = encrypt_message(plaintext, N, e)

    # Output encrypted message to ciphertext textbox
    ciphertext_textbox.delete("1.0", END)
    ciphertext_textbox.insert("1.0", encrypted)


# Decrypt message button function
def decrypt_message_button():
    # Get values from ciphertext textbox
    ciphertext = ciphertext_textbox.get("1.0", END)

    # Generate keys
    p = 101
    q = 211
    N, e, d = generate_keys(p, q)

    # Decrypt message
    decrypted = decrypt_message(ciphertext, N, d)

    # Output decrypted message to plaintext textbox
    plaintext_textbox.delete("1.0", END)
    plaintext_textbox.insert("1.0", decrypted)


# Create GUI
root = Tk()
root.title("RSA Cipher")

# Create labels
plaintext_label = Label(root, text="Plaintext:")
plaintext_label.grid(row=0, column=0, padx=10, pady=10)

ciphertext_label = Label(root, text="Ciphertext:")
ciphertext_label.grid(row=1, column=0, padx=10, pady=10)

# Create text boxes
plaintext_textbox = Text(root, height=10, width=50)
plaintext_textbox.grid(row=0, column=1, padx=10, pady=10)

ciphertext_textbox = Text(root, height=10, width=50)
ciphertext_textbox.grid(row=1, column=1, padx=10, pady=10)

# Create buttons
encrypt_button = Button(root, text="Encrypt", command=encrypt_message_button)
encrypt_button.grid(row=2, column=0, padx=10, pady=10)

decrypt_button = Button(root, text="Decrypt", command=decrypt_message_button)
decrypt_button.grid(row=2, column=1, padx=10, pady=10)

# Run GUI
root.mainloop()
