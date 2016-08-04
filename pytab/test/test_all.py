# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

import functools

def func(a, b, c, d, e, f, g = 100):
    print(a, b, c, d, e, f, g)

f = functools.cur(func)

c1 = f(1)
c2 = c1(2, d = 4)               # Note that c is still unbound
c3 = c2(3)(f = 6)(e = 5)        # now c = 3
c3()                            # () forces the evaluation              <====
                                #   it prints "1 2 3 4 5 6 100"
c4 = c2(30)(f = 60)(e = 50)     # now c = 30
c4()