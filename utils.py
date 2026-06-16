from passlib.context import CryptContext

# Set up the cryptography context to use bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    """Hashes a plain text password using bcrypt."""
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str):
    """Verifies a plain text password against a hashed password."""
    return pwd_context.verify(password, hashed)