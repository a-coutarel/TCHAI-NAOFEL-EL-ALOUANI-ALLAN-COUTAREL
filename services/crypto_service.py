import base64
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512
from Crypto import Random

class CryptoService:
    @staticmethod
    def generate_keys() -> (str, str):
        random_generator = Random.new().read
        key_size = 2048
        key: RSA.RsaKey = RSA.generate(key_size, random_generator)
        private, public = key, key.publickey()
        return private.export_key().decode(), str(public.export_key().decode())

    @staticmethod
    def sign_transaction(private_key: str, transaction_data: str) -> str:
        try:
            private_key: RSA.RsaKey = RSA.import_key(private_key)
        except ValueError:
            print("Invalid private key:", private_key)
            return None
        
        signer = PKCS1_v1_5.new(private_key)
        digest = SHA512.new()
        digest.update(transaction_data.encode())
        signature = signer.sign(digest)
        #return base64.b64encode(signature).decode()
        return signature

    def verify_signature(public_key: str, transaction_data: str, signature: str) -> bool:
        try:
            public_key = RSA.import_key(public_key)
        except ValueError:
            print("Error", ValueError,"Invalid public key:", public_key)
            return False
        
        try:
            signature = base64.b64decode(signature)
        except Exception:
            print("Error", Exception,"Invalid signature:", signature)
            return False

        signer = PKCS1_v1_5.new(public_key)
        digest = SHA512.new()
        digest.update(transaction_data.encode())
        return signer.verify(digest, signature)