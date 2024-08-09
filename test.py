from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# Frase a ser criptografada
frase = (input("Digite uma frase para ser criptografada: "))

# Gerar chave de criptografia (32 bytes para AES-256)
key = os.urandom(32)

# Gerar vetor de inicialização (IV) (16 bytes)
iv = os.urandom(16)

# Função para criptografar
def encrypt(message, key, iv):
    # Adicionar padding à mensagem
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()
    
    # Configurar a cifra AES-CBC
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Criptografar a mensagem
    encrypted_message = encryptor.update(padded_data) + encryptor.finalize()
    return encrypted_message

# Criptografar a frase
encrypted_message = encrypt(frase, key, iv)

# Resultados
print(f"Mensagem criptografada: {encrypted_message.hex()}")
