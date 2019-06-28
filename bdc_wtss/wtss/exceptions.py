from bdc_wtss.utils.exceptions import NotFoundError


class CoverageNotFoundError(NotFoundError):
    """
    Utility Exception when coverage is not found on the server
    """
    def __init__(self, coverage):
        super(NotFoundError, self).__init__('Coverage "{}" not found'.format(coverage))


