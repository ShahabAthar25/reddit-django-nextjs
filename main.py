def generate_secret_key():
    import base64
    import os

    # Generate a random 32-byte key
    key = os.urandom(32)

    # Encode the key in base64 to make it URL-safe
    secret_key = base64.urlsafe_b64encode(key).decode("utf-8")

    return secret_key


if __name__ == "__main__":
    secret_key = generate_secret_key()
    print(f"Generated SECRET_KEY: {secret_key}")
