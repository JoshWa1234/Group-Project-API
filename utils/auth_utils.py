import uuid
import bcrypt
import secrets
import re

def hashPassword(password: str) -> str:
    pw_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pw_bytes, salt)
    return hashed.decode("utf-8")

def verifyPassword(password: str, stored_hash: str) -> bool:
    success = bcrypt.checkpw(password.encode("utf-8"), stored_hash.encode("utf-8"))
    return success

def validate_password(password: str) -> bool:
    pattern = r'^(?=.*[A-Z])(?=(?:.*[a-z]){6,})(?=.*[!@#$%^&*(),.?":{}|<>])(?=.*\d).{1,32}$'
    return bool(re.match(pattern, password))

def gerateNewID():
    return str(uuid.uuid4())
    
def generateAuthToken():
    return secrets.token_hex(16)

def verifyInteger(value:str | int ) -> bool:
    
    isInteger = False
    if type(value) == int:
        isInteger = True
    else:
        try:
            value = int(value)
            if type(value) == int:
                isInteger = True
        except:
            isInteger = False

    return isInteger


def verifyFloat(value:str | int | float ) -> bool:
    
    isFloat = False
    if type(value) == float:
        isFloat = True
    else:
        try:
            value = float(value)
            if type(value) == float:
                isFloat = True
        except:
            isFloat = False

    return isFloat
