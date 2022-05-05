import sys


class _constant:
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise Exception("Don't allocate value on Constant")
        self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__dict__:
            raise Exception("Don't Delete Value")


sys.modules[__name__] = _constant()
