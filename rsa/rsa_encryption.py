import random

# Fungsi Euclidean untuk GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Fungsi untuk mencari kunci publik dan privat
def generate_keys():
    p = 61  # bilangan prima
    q = 53  # bilangan prima
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 17  # exponent umum
    d = pow(e, -1, phi)

    return ((e, n), (d, n))

# Enkripsi
def encrypt(msg, public_key):
    e, n = public_key
    return [(ord(char) ** e) % n for char in msg]

# Dekripsi
def decrypt(cipher, private_key):
    d, n = private_key
    return ''.join([chr((char ** d) % n) for char in cipher])

# Testing
public, private = generate_keys()
message = "hello"
cipher = encrypt(message, public)
print("Encrypted:", cipher)

decrypted = decrypt(cipher, private)
print("Decrypted:", decrypted)
