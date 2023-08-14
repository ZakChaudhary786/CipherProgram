from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Generate a random key
key = get_random_bytes(16)

# Create an AES cipher object
cipher = AES.new(key, AES.MODE_EAX)

# Encrypt the plaintext message
message = b'This is a secret message'
ciphertext, tag = cipher.encrypt_and_digest(message)

# Decrypt the ciphertext message
cipher = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
plaintext = cipher.decrypt_and_verify(ciphertext, tag)

print(plaintext)