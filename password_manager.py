from cryptography.fernet import Fernet
import os
import json

KEY_FILE = "secret.key"
DATA_FILE = "passwords.json"

# Generate and save encryption key if it doesn't exist
def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)

# Load the encryption key
def load_key():
    return open(KEY_FILE, "rb").read()

# Load encrypted password database
def load_passwords(cipher):
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "rb") as f:
        encrypted_data = f.read()
        if not encrypted_data:
            return {}
        decrypted_data = cipher.decrypt(encrypted_data)
        return json.loads(decrypted_data)

# Save encrypted password database
def save_passwords(passwords, cipher):
    data = json.dumps(passwords).encode()
    encrypted_data = cipher.encrypt(data)
    with open(DATA_FILE, "wb") as f:
        f.write(encrypted_data)
