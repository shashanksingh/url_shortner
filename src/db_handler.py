from typing import List



class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class PersistentDictSingleton(metaclass=SingletonMeta):
    def __init__(self):
        pass

    def save_into_storage(
        self, database_name: str, table_name: str, object_to_be_stored: object
    ) -> bool:
        pass

    def load_from_storage(self, database_name: str, table_name: str) -> object:
        pass

    # https://stackoverflow.com/a/54667683
    def list_all(self) -> List[object]:
        pass

    def close(self):
        self.shelve.close()
