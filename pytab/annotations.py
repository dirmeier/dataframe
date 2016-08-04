# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

def override(interface):
    def override(method):
        assert(method.__name__ in dir(interface))
        return method
    return override
