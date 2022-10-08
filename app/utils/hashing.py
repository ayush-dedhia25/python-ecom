import os
from hashlib import pbkdf2_hmac
from hmac import compare_digest

def hash_str(password: str) -> tuple[bytes, bytes]:
   salt = os.urandom(16)
   hash_password = pbkdf2_hmac("sha256", password.encode(), salt, 100000)
   return salt, hash_password

def cmp_str(salt: bytes, hashed: bytes, password: str) -> bool:
   hash_password = pbkdf2_hmac("sha256", password.encode(), salt, 100000)
   return compare_digest(hashed, hash_password)