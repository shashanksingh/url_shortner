import uuid
import hashlib


def generate_short_url(string_to_hash: str) -> str:
    return str(uuid.uuid4())


def generate_unique_hash(string_to_hash: str) -> str:
    return hashlib.sha224(string_to_hash).hexdigest()
