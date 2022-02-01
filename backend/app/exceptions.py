"""app.exceptions
Module that contains the exceptions of our app.
"""

class InternalErrorException(Exception):
    """Exception raised when an internal error occurred"""


class ConnectionAPIError(Exception):
    """Exception raised when couldn't connect to an API."""


class NotFound(Exception):
    """Exception raised when an information is not found in either API."""


class AlreadyExists(Exception):
    """Exception raised when an information already exists in either API."""
