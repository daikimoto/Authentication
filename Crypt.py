from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def encrypt_aes(key, plaintext):
    # Generate a random IV
    iv = os.urandom(16)  # AESブロックサイズは16バイト

    # Ensure the key is 32 bytes (AES-256)
    key = key.ljust(32, b'\0')

    # Pad the plaintext to be multiple of AES block size
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext.encode()) + padder.finalize()

    # Create an AES cipher with CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt the plaintext
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    # Return IV + ciphertext
    return iv + ciphertext

def decrypt_aes(key, ciphertext):
    # Extract IV from the ciphertext
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]

    # Ensure the key is 32 bytes (AES-256)
    key = key.ljust(32, b'\0')

    # Create an AES cipher with CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the ciphertext
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Unpad the plaintext
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext.decode()