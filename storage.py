import json
from cryptography.fernet import Fernet


def load_key():
    with open("key.key", "rb") as file:
        return file.read()

key = load_key()
fernet = Fernet(key)


def load_data():
    try:
        with open("passwords.json", "r") as file:
            encrypted_data = json.load(file)

        decrypted_data = {}

        for service, enc_password in encrypted_data.items():
            decrypted_password = fernet.decrypt(enc_password.encode()).decode()
            decrypted_data[service] = decrypted_password

        return decrypted_data

    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_data(data):
    encrypted_data = {}

    for service, password in data.items():
        encrypted_password = fernet.encrypt(password.encode()).decode()
        encrypted_data[service] = encrypted_password

    with open("passwords.json", "w") as file:
        json.dump(encrypted_data, file, indent=4)