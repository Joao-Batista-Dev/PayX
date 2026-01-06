from passlib.context import CryptContext


CRYPT = CryptContext(schemes=['bcrypt'], deprecated='auto')

# verify if the password matches the hash stored in the database
def check_password(password: str, hash_password: str) -> bool:
    return CRYPT.verify(password, hash_password)

# Generate a secure hash for the password.
def generate_password_hash(password: str) -> str:
    return CRYPT.hash(password)
