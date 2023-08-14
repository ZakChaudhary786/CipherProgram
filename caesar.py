import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
 
root = tk.Tk()
root.title("Caesar Cipher")
 
def encrypt():
    message = msg_entry.get("1.0", tk.END)
    shift = int(shift_entry.get())
    ciphertext = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            ciphertext += char
    result_entry.delete("1.0", tk.END)
    result_entry.insert("1.0", ciphertext)
 
def decrypt():
    ciphertext = msg_entry.get("1.0", tk.END)
    shift = int(shift_entry.get())
    message = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                message += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                message += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            message += char
    result_entry.delete("1.0", tk.END)
    result_entry.insert("1.0", message)
 
# Create the GUI widgets
msg_label = tk.Label(root, text="Message:")
msg_entry = tk.Text(root, height=5, width=50)
shift_label = tk.Label(root, text="Shift:")
shift_entry = tk.Entry(root)
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
result_label = tk.Label(root, text="Result:")
result_entry = tk.Text(root, height=5, width=50)
 
# Add the widgets to the GUI
msg_label.grid(row=0, column=0)
msg_entry.grid(row=0, column=1)
shift_label.grid(row=1, column=0)
shift_entry.grid(row=1, column=1)
encrypt_button.grid(row=2, column=0)
decrypt_button.grid(row=2, column=1)
result_label.grid(row=3, column=0)
result_entry.grid(row=3, column=1)
 
# Start the GUI
root.mainloop()