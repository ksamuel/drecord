

from itertools import islice, takewhile, dropwhile


class r(tuple):

    slots = ()

    def __new__(cls, *args, **kwargs):
        if args:
            raise TypeError('r() takes not positional arguments')
        return tuple.__new__(cls, kwargs.values())

    def __init__(self, **kwargs):
        for i, name in enumerate(kwargs):
            setattr(self, name, self[i])

    def __getitem__(self, item):

        if not isinstance(item, slice):
            try:
                return tuple.__getitem__(self, item)
            except TypeError:
                return getattr(self, item)

        try:

            return r(**dict(tuple(self.__dict__.items())[item]))
        except TypeError:
            iterable = self.__dict__.items()
            start = item.start
            stop = item.stop
            namespace = self.__dict__
            iterable = namespace.items()
            if start is not None:
                if start not in namespace:
                    if isinstance(start, int):
                        raise ValueError(
                            "Cannot mix an index and a key when slicing a record") from None
                    raise KeyError(start) from None
                iterable = dropwhile(lambda pair: pair[0] != start, iterable)
            if stop is not None:
                if stop not in namespace:
                    if isinstance(stop, int):
                        raise ValueError(
                            "Cannot mix an index and a key when slicing a record") from None
                    raise KeyError(stop) from None
                iterable = takewhile(lambda pair: pair[0] != stop, iterable)

            return self.__class__(**dict(islice(iterable, None, None, item.step)))

    def __call__(self, **kwargs):
        return self.__class__(**{**self.__dict__, **kwargs})

    def __repr__(self):
        fields = " ".join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({fields})"

    def __getnewargs__(self):
        'Return self as a plain tuple.  Used by copy and pickle.'
        return tuple(self)

    def __getstate__(self):
        'Exclude the OrderedDict from pickling'
        return None
