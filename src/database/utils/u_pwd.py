import binascii
import hashlib
import os


def hash_pwd(pwd: str) -> tuple:
    """Generate salt, hash the password, and return both."""
    salt = gen_salt()  # Generate a random salt
    hashed_password = salt_pwd(pwd, salt)  # Hash the password with the generated salt
    return (
        hashed_password,
        binascii.hexlify(salt).decode(),
    )  # Return hashed password and hex-encoded salt


def gen_salt(length=16) -> bytes:
    """Generate a random salt."""
    return os.urandom(length)  # Generate a random byte string of the specified length


def salt_pwd(password: str, salt: bytes) -> str:
    """Hash the password with the provided salt."""
    pwd_salt = password.encode() + salt  # Combine the password and salt
    pwd_hash = hashlib.pbkdf2_hmac(
        "sha256", pwd_salt, salt, 100000
    )  # Hash the combined string using PBKDF2-HMAC-SHA256
    return binascii.hexlify(
        pwd_hash
    ).decode()  # Return the hashed password as a hex-encoded string


def verify_password(
    stored_password: str, stored_salt: str, provided_password: str
) -> bool:
    """Verify that the provided password matches the stored hashed password."""
    # Decode the stored salt from hex to bytes
    salt_bytes = binascii.unhexlify(stored_salt.encode())

    # Hash the provided password using the stored salt
    hashed_password = salt_pwd(provided_password, salt_bytes)

    # Compare the hashed password to the stored password and return the result
    return stored_password == hashed_password
