from Crypto.PublicKey import DSA
from Crypto.Hash import SHA256
from Crypto.Signature import DSS

def string_to_bytes(str: str):
    """Converts string to bytes."""
    return bytes(str, 'utf-8')

def bytes_to_string(b):
    return b.decode("utf-8")

def int_to_bytes(n):
    """Converts int to bytes."""
    return n.to_bytes((n.bit_length() + 7) // 8, 'big')


def bytes_to_int(nb):
    """Converts bytes to int."""
    return int.from_bytes(nb, 'big')


def string_to_int(str: str):
    """Converts string to int."""
    return bytes_to_int(string_to_bytes(str))

def int_to_string(n):
    """Converts int to string."""
    return bytes_to_string(int_to_bytes(n))

def sign_message(key, bytes_message):
    hash_obj = SHA256.new(bytes_message)
    signer = DSS.new(key, 'fips-186-3')
    return signer.sign(hash_obj)

def verify_signature(public_key_filename, bytes_message, signature):
    f = open(public_key_filename, "r")
    public_key = DSA.importKey(f.read())
    f.close()

    hash_obj = SHA256.new(bytes_message)
    verifier = DSS.new(public_key, 'fips-186-3')
    verifier.verify(hash_obj, signature)
