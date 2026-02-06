from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
import os

from security.keys import derive_key, get_secret_key


def encrypt_watermark(data: bytes) -> bytes:
    key = derive_key(get_secret_key())
    iv = os.urandom(16)

    padder = PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv),
                    backend=default_backend())
    encryptor = cipher.encryptor()

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return iv + ciphertext


def decrypt_watermark(ciphertext: bytes) -> bytes:
    key = derive_key(get_secret_key())
    iv = ciphertext[:16]
    ct = ciphertext[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv),
                    backend=default_backend())
    decryptor = cipher.decryptor()

    padded = decryptor.update(ct) + decryptor.finalize()

    unpadder = PKCS7(128).unpadder()
    return unpadder.update(padded) + unpadder.finalize()
