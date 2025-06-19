from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# Khóa bí mật cố định 16 bytes (AES-128)
KEY = b'ThisIsASecretKey'

def encrypt_message(message):
    cipher = AES.new(KEY, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    # Gộp IV và ciphertext, mã hóa base64 để gửi đi
    result = base64.b64encode(cipher.iv + ct_bytes).decode('utf-8')
    return result

def decrypt_message(data):
    raw = base64.b64decode(data)
    iv = raw[:AES.block_size]
    ct = raw[AES.block_size:]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')
    return pt