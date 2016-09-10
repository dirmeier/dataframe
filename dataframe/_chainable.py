# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'


class Chainable:
    """
    Class that allows chaining of methods.

    """

    def __init__(self, func, args=(), kwargs=None, minargs = None):
        """
        Constructor for chainable.

        :param func: the function to be called
        :param args: tuple of params
        :param kwargs: dictionary of named params
        """
        self.__func = func
        self.__args = args
        self.__kwargs = kwargs
        self.__minargs = minargs

    def __call__(self, *args, **kwargs):
        if args or kwargs:
            new_args = self.__args + args
            new_kwargs = dict.copy(self.__kwargs)
            new_kwargs.update(kwargs)
            # Evaluate function
            if self.__minargs is not None and self.__minargs <= len(new_args) + len(new_kwargs):
                return self.__func(*new_args, **new_kwargs)
            # create new chainable
            else:
                return Chainable(self.__func, new_args, new_kwargs, self.__minargs)
        # do call
        else:
            return self.__func(*self.__args, **self.__kwargs)

    def __ror__(self, arg):
        return self.__func(*(self.__args + (arg,)), **self.__kwargs)

def chain(func, min_args=None):
    """
    Definition for chainable functions.

    :param func: function to be made chainable
    :param min_args: minimal arguments of the function
    :return: returns the function as chainable function
    """
    return Chainable(func, (), {}, min_args)
