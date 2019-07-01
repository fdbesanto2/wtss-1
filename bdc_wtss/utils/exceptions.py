class APIError(Exception):
    """"
    Base class for API exception handling
    """

    code = None
    message = None

    def __init__(self, message):
        super(Exception, self).__init__(message)
        self.message = message


class BadRequestError(APIError):
    code = 400


class NotFoundError(APIError):
    code = 404