"""
    Brandwatch api module exceptions
"""


class BrandwatchApiException(Exception):
    def __init__(self, msg, response_status_code, code_number=None, code=None):
        """
        Generic exception for Brandwatch API response errors.

        Args:
            msg: `str` error message
            response_status_code: `int` response status code
            code_number: `int` error code number
            code: `str` error code
        """
        self.msg = msg
        self.code_number = code_number
        self.code = code
        self.response_status_code = response_status_code

    def __str__(self):
        return u'{} - {}'.format(self.response_status_code, self.msg)


class BrandwatchApiProjectNotFoundException(BrandwatchApiException):
    """
    Exception for when project related to an API call is not found.
    """
    pass
