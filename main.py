import tkinter as tk
import subprocess

# Define the GUI window
window = tk.Tk()
window.title("Cipher Program Selector")

# Define the button functions
def caesar_cipher():
    subprocess.Popen(["python", "caesar.py"])

def vernam_cipher():
    subprocess.Popen(["python", "vernam.py"])

def rsa_cipher():
    subprocess.Popen(["python", "rsaprogram.py"])

def aes_cipher():
    subprocess.Popen(["python", "aes.py"])

# Define the buttons
caesar_button = tk.Button(window, text="Caesar Cipher", command=caesar_cipher)
vernam_button = tk.Button(window, text="Vernam Cipher", command=vernam_cipher)
rsa_button = tk.Button(window, text="RSA Cipher", command=rsa_cipher)
aes_button = tk.Button(window, text="AES Cipher", command=aes_cipher)

# Add the buttons to the window
caesar_button.pack()
vernam_button.pack()
rsa_button.pack()
aes_button.pack()

# Start the GUI loop
window.mainloop()