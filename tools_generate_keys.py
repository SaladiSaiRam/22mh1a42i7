#!/usr/bin/env python3
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
# Generate RSA 4096-bit key
priv = rsa.generate_private_key(public_exponent=65537, key_size=4096)
pub = priv.public_key()
# Write private key (PEM, no passphrase)
with open("student_private.pem", "wb") as f:
    f.write(priv.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ))
# Write public key (PEM)
with open("student_public.pem", "wb") as f:
    f.write(pub.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))
print("WROTE student_private.pem and student_public.pem")
