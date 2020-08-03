class DatabaseException(BaseException):
    """
    Basic DB exception
    """

    pass


class FieldAlreadyExists(BaseException):
    """
    DB Column already exists
    """

    pass


class ValidationException(BaseException):
    """
    Validation issue in data provided
    """

    pass
