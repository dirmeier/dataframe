# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'


class Function:
    def __init__(self, func, args=(), kwargs=None, unique=True, min_arg=None):
        self.__func = func
        self.__args = args
        self.__kwargs = kwargs
        self.__unique = unique
        self.__min_arg = min_arg

    def __call__(self, *args, **kwargs):
        if args or kwargs:
            _args = self.__aArgs + args
            _kwargs = dict.copy(self.__kwargs)
            if self.__unique and not kwargs.keys().isdisjoint(kwargs):
                raise ValueError("Muliple keys!")
            _kwargs.update(kwargs)
            if self.__min_arg is not None and self.__min_arg <= len(_args) + len(_kwargs):
                return self.__func(*_args, **_kwargs)
            else:
                return Function(self.__func, _args, _kwargs, self.__unique, self.__min_arg)
        else:
            return self.__func(*self.__args, **self.__kwargs)

    def __ror__(self, arg):
        return self.__func(*(self.__args + (arg,)),
                           **self.__kwargs)

    def __add__(self, other):
        if not isinstance(other, Function):
            raise TypeError("Needs to be a Function instance")
        def compute(*args, **kwargs):
            return other.__func(*(other.__args + (self.__func(*args, **kwargs),)),
                                **other.__kwargs)
        return Function(compute, self.__args, self.__kwargs, self.__unique, self.__min_arg)


def cur(f, min_args=None):
    return Function(f, (), {}, True, min_args)


def curr(f, min_args=None):
    return Function(f, (), {}, False, min_args)
