import uuid


def hashing_function(string_to_hash: str) -> str:
    return str(uuid.uuid4())
