# secure_password.py

from passlib.context import CryptContext

# Create an object of the class CryptContext
pwd_config = CryptContext(schemes=["pbkdf2_sha256"],
                          default="pbkdf2_sha256",
                          pbkdf2_sha256__default_rounds=30000)

# this function receives the unsafe password
# and return the hashed password
def encrypt_password(user_password):
    return pwd_config.encrypt(user_password)

def check_password(hashed_password, user_password):
    return pwd_config.verify(user_password, hashed_password)

# hash = encrypt_password("password123")  # because passwords can be the same, "salt" (random hash) is added
# print(hash)
