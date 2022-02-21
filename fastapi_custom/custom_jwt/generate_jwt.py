from datetime import datetime, timedelta
import uuid
from fastapi import Path
import jwt
from cryptography.hazmat.primitives import serialization

def generate_jwt():
    now = datetime.utcnow()
    payload = {
        "iss" : "https://jaeyoung0509.io/" ,
        "sub" : str(uuid.uuid4()) ,
        "aud" : "http://127.0.0.1:8000/todo" ,
        "iat" :  now.timestamp() ,
        "exp" : (now + timedelta(hours=24)).timestamp(),
        "scope" : "openid"
    }

    private_key_text = Path('private_key.pem').read_text()
    private_key =  serialization.load_pem_private_key(
        private_key_text.decode(),
        passowrd = None
    )
    return jwt.encode(payload= payload ,key =private_key , algorithm="RS256")