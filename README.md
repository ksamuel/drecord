# drecord: Dynamic record type for python

I often wish Python had a literal syntax for a record type that you can dynamically create on the fly.

NamedTuple is nice, but must be defined before hand. SimpleNamespace is also interesting, but is not iterable, nor sliceable.

This repo is a PoC of what such a dynamic record type could be:

```python
>>> from drecord import r
>>> record = r(a=0, b=1, c=2, d=3, e=4, f=5, g=5)
>>> record[0]
0
>>> record.a
0
>>> list(record)
[0, 1, 2, 3, 4, 5, 5]
>>> record == (0, 1, 2, 3, 4, 5, 5)
True
>>> record[1:4]
r(b=1 c=2 d=3)
>>> record["b":"e"]
r(b=1 c=2 d=3)
>>> record(a="foo", b="bar")
r(a=foo b=bar c=2 d=3 e=4 f=5 g=5)
>>> record.__dict__
{'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 5}
```


It's not a on pypi but it's a single standalone file.