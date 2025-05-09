# SSH dan RSA Hands-On

Dokumentasi praktik hands-on untuk pemahaman konsep kriptografi dan keamanan jaringan yang mencakup:

- **SSH (Secure Shell)**: Implementasi koneksi jarak jauh yang aman dan manajemen kunci
- **RSA (Rivest-Shamir-Adleman)**: Simulasi algoritma enkripsi dan dekripsi asimetrik dengan Python

## Daftar Isi

- [Overview](#overview)
- [SSH Key Generation & Connection](#ssh-key-generation--connection)
- [RSA Python Implementation](#rsa-python-implementation)
- [Struktur Project](#struktur-project)
- [Instalasi dan Penggunaan](#instalasi-dan-penggunaan)
- [Hasil Pengujian](#hasil-pengujian)

## Overview

Project ini berisi implementasi praktis dari dua materi kelas kriptografi yang fundamental:

1. **SSH Key-Pair Authentication**: Metode otentikasi yang aman tanpa password menggunakan pasangan kunci publik-privat
2. **RSA Encryption/Decryption**: Simulasi sederhana algoritma RSA untuk enkripsi dan dekripsi pesan

## SSH Key Generation & Connection

### Langkah-langkah Implementasi

1. **Generate SSH Key Pair** menggunakan command:
   ```bash
   ssh-keygen -t rsa -b 2048 -C "your_email@example.com"
   ```

2. **Transfer Public Key ke Server** untuk autentikasi:
   ```bash
   ssh-copy-id username@host_ip
   ```

3. **Koneksi Tanpa Password**:
   ```bash
   ssh username@host_ip
   ```

### Informasi Penting

- Pasangan kunci disimpan di direktori `~/.ssh/` (Linux/Mac) atau `C:\Users\<username>\.ssh\` (Windows)
- File kunci privat: `id_rsa` (jangan pernah dibagikan)
- File kunci publik: `id_rsa.pub` (dapat dibagikan ke server)

## RSA Python Implementation

Program Python yang mengimplementasikan algoritma RSA dengan langkah-langkah:

1. **Generating Keys**:
   - Memilih dua bilangan prima (p dan q)
   - Menghitung n = p × q
   - Menghitung fungsi Euler's totient: φ(n) = (p-1) × (q-1)
   - Memilih bilangan e (public exponent)
   - Menghitung d (private exponent) sebagai invers modular dari e mod φ(n)

2. **Enkripsi**:
   - C = M^e mod n (dimana M adalah pesan plain text)

3. **Dekripsi**:
   - M = C^d mod n (dimana C adalah cipher text)

### Sample Code

```python
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
```

## Struktur Project

```
project-root/
├── ssh/
│   └── ssh_practice.md  # Dokumentasi praktik SSH
├── rsa/
│   └── rsa_encryption.py  # Implementasi RSA
└── README.md  # Dokumentasi project
```

## Instalasi dan Penggunaan

### SSH Setup

1. Install OpenSSH jika belum tersedia
2. Jalankan perintah-perintah SSH seperti yang tercantum di bagian SSH Key Generation

### RSA Python

1. Pastikan Python sudah terinstall
2. Jalankan script RSA:
   ```bash
   python rsa_encryption.py
   ```

## Hasil Pengujian

### SSH Key Generation

![SSH Key Generation](./image/Screenshot%202025-05-09%20140435.png)

Berhasil membuat pasangan kunci SSH:
- Private key: `id_rsa` (2KB)
- Public key: `id_rsa.pub` (1KB)

### RSA Encryption/Decryption

Contoh output dari program RSA:
```
Encrypted: [2170, 1313, 745, 745, 2185]
Decrypted: hello
```

---

Dibuat oleh: Subkhan Masudi (5027221044)
