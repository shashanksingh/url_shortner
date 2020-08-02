class DatabaseException(BaseException):
    pass


class FieldAlreadyExists(DatabaseException):
    pass


class ValidationException(BaseException):
    pass
