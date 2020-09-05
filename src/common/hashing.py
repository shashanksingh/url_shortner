import uuid
import hashlib


def generate_short_url() -> str:
    """
    UUID is used for generating short url's
    :return: UUID example 721be567-07bd-4cfd-a340-38a8fe0a9356
    """
    return str(uuid.uuid4())


def generate_unique_hash(string_to_hash: str) -> str:
    """
    used for forcing one long url to one short url constraint
    :param string_to_hash: sstring to be hashed , right now only long_url is pass
    :return: sha 2 hash
    """
    return hashlib.sha224(string_to_hash.encode("utf-8")).hexdigest()
    