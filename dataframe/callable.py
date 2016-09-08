# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

class Callable:
    """
    Super-class for all classes that should be callable. E.g.: whenever you want to use ``modify`` or ``aggregate``
    you need to write a class that extends ``Callable`` and overwrite ``__call__``.
    ``__call__`` has to return a scalar or list,
    depending if you want to aggregate columns or modify. So a class that modifies a column returns a list,
    while a class that aggregates returns a scalar.
    """

    def __call__(self, *args):
        """
        Call method. Is used when object is called like this: object()

        :param args: tuple of columns
        :type args: tuple
        :return: returns a list/scalar
        :rtype: list(any)/scalar
        """
        pass
