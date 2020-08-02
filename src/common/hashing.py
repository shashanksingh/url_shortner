import uuid


def hashing_function(string_to_hash: str) -> str:
    return uuid.uuid4(string_to_hash)
