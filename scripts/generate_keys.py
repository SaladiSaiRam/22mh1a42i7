# scripts/generate_keys.py
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

priv = rsa.generate_private_key(public_exponent=65537, key_size=4096)
priv_pem = priv.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption(),
)
pub_pem = priv.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)
open("student_private.pem","wb").write(priv_pem)
open("student_public.pem","wb").write(pub_pem)
print("WROTE student_private.pem and student_public.pem (4096-bit)")