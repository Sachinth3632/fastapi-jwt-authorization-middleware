from passlib.context import CryptContext

bcrypt_object = CryptContext(schemes=["bcrypt"])

def hash_password(password):
    return bcrypt_object.hash(password)

def verify_password(entered_password, hashed_password):
    return bcrypt_object.verify(entered_password, hashed_password)

if __name__ == "__main__":
    password = input("Enter Password: ")
    print(hash_password(password))