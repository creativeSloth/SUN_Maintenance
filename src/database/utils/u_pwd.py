import binascii
import hashlib
import os


def hash_pwd(pwd: str) -> tuple:
    r"""Generate salt, hash the password, and return both."""
    salt = gen_salt()  # Generate a random salt
    hashed_password = salt_pwd(pwd, salt)  # Hash the password with the generated salt
    return (
        hashed_password,
        binascii.hexlify(salt).decode(),
    )  # Return hashed password and hex-encoded salt


def gen_salt(length=16) -> bytes:
    r"""Generate a random salt."""
    return os.urandom(length)  # Generate a random byte string of the specified length


def salt_pwd(pwd: str, salt: bytes) -> str:
    r"""
    Hash the password with the provided salt.
    :param pwd: The password to hash with the provided salt
    :type pwd: str
    :param salt: The salt to use for hashing
    """
    pwd_salt = pwd.encode() + salt  # Combine the password and salt
    pwd_hash = hashlib.pbkdf2_hmac(
        "sha256", pwd_salt, salt, 100000
    )  # Hash the combined string using PBKDF2-HMAC-SHA256
    return binascii.hexlify(
        pwd_hash
    ).decode()  # Return the hashed password as a hex-encoded string


def verify_password(stored_pwd: str, stored_salt: str, provided_pwd: str) -> bool:
    r"""
    Verify that the provided password matches the stored hashed password.
    :param stored_pwd: The password to verify
    :type stored_pwd: str
    :param stored_salt: The salt associated with the stored password
    :type stored_salt: str
    :param provided_pwd: The password to be verified
    :type provided_pwd: str
    :return: A boolean value indicating whether the verification was successful

    """
    try:
        # Decode the stored salt from hex to bytes
        salt_bytes = binascii.unhexlify(stored_salt.encode())

        # Hash the provided password using the stored salt
        hashed_password = salt_pwd(provided_pwd, salt_bytes)

        # Compare the hashed password to the stored password and return the result
        return stored_pwd == hashed_password

    except (binascii.Error, ValueError) as e:
        # Handle any errors during the decoding or hashing process
        print(f"Error verifying password: {e}")
        return False
