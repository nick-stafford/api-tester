# oauth helper - work in progress

import base64
import hashlib
import secrets

def generate_pkce():
    """Generate PKCE code verifier and challenge"""
    verifier = secrets.token_urlsafe(32)
    challenge = base64.urlsafe_b64encode(
        hashlib.sha256(verifier.encode()).digest()
    ).rstrip(b'=').decode()
    return verifier, challenge

def basic_auth_header(username, password):
    credentials = f"{username}:{password}"
    encoded = base64.b64encode(credentials.encode()).decode()
    return f"Basic {encoded}"

# TODO: add oauth2 flow
# TODO: add jwt helper
