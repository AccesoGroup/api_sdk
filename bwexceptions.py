"""
    Brandwatch api module exceptions
"""


class BrandwatchApiException(Exception):
    pass


class BrandwatchApiProjectNotFoundException(BrandwatchApiException):
    pass
