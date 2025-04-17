from cryptography.fernet import Fernet

# Generate and store the key
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt the message
message = input("Enter a message to encrypt: ").encode()
encrypted_message = cipher.encrypt(message)
print(f"Encrypted: {encrypted_message.decode()}")

# Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message).decode()
print(f"Decrypted: {decrypted_message}")