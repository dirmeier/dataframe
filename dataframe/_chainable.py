# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'
#
# Code has been adopted by Massimiliano Tomassoli, 2012.
# Class that allows currying for functions

class Chainable:
    """

    """
    def __init__(self, func, args=(), kwargs=None, unique = True, minargs = None):
        self.__func = func
        self.__args = args
        self.__kwargs = kwargs
        self.__unique = unique
        self.__minargs = minargs

    def __call__(self, *args, **kwargs):
        if args or kwargs:
            new_args = self.__args + args
            new_kwargs = dict.copy(self.__kwargs)
            # If unique is True, we don't want repeated keyword arguments.
            if self.__unique and not kwargs.keys().isdisjoint(new_kwargs):
                raise ValueError("Repeated kw arg while unique = True")
            new_kwargs.update(kwargs)
            # Evaluate function
            if self.__minargs is not None and self.__minargs <= len(new_args) + len(new_kwargs):
                return self.__func(*new_args, **new_kwargs)
            # create new chainable
            else:
                return Chainable(self.__func, new_args, new_kwargs, self.__unique, self.__minargs)
        # do call
        else:
            return self.__func(*self.__args, **self.__kwargs)

    def __ror__(self, arg):
        return self.__func(*(self.__args + (arg,)), **self.__kwargs)

def cur(f, min_args=None):
    return Chainable(f, (), {}, True, min_args)

def curr(f, min_args=None):
    return Chainable(f, (), {}, False, min_args)
