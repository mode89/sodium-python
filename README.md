# Sodium

Port of [Sodium](https://github.com/SodiumFRP/sodium) - Functional Reactive Programming (FRP) library - to Python.


## Installation

Just `pip install sodiumfrp`.


## Main Concepts

### Streams and Cells

This library is based on two types:
[`Stream`](https://sodium-python.readthedocs.io/en/latest/sodiumfrp.html#sodiumfrp.primitives.Stream)
and [`Cell`](https://sodium-python.readthedocs.io/en/latest/sodiumfrp.html#sodiumfrp.primitives.Cell).
`Stream` represents a *stream of events*, while `Cell` represents a *value that changes over time*.

### Operators

There is also a bunch of primitives that you can use to build streams/cells and to compose them together.
They provide means for doing common operations like mapping, filtering, reduction, flat-mapping and more.
All of them are implemented as members of
[`Stream`](https://sodium-python.readthedocs.io/en/latest/sodiumfrp.html#sodiumfrp.primitives.Stream)
and [`Cell`](https://sodium-python.readthedocs.io/en/latest/sodiumfrp.html#sodiumfrp.primitives.Cell) classes.

### Forward references

In situations, where a stream or cell needs to be referenced *before* it is assigned, use
[`StreamLoop`](https://sodium-python.readthedocs.io/en/latest/sodiumfrp.html#sodiumfrp.primitives.StreamLoop) or
[`CellLoop`](https://sodium-python.readthedocs.io/en/latest/sodiumfrp.html#sodiumfrp.primitives.CellLoop).

### Interfacing with imperative world

`Stream` and `Cell` lets you model your business logic in a *purely functional* way.
In order to provide your model with input data, use
[`StreamSink`](https://sodium-python.readthedocs.io/en/latest/sodiumfrp.html#sodiumfrp.primitives.StreamSink) and
[`CellSink`](https://sodium-python.readthedocs.io/en/latest/sodiumfrp.html#sodiumfrp.primitives.CellSink).
And, whenever you need to get data out of the model, use
[`Stream.listen()`](https://sodium-python.readthedocs.io/en/latest/sodiumfrp.html#sodiumfrp.primitives.Stream.listen)
and [`Cell.listen()`](https://sodium-python.readthedocs.io/en/latest/sodiumfrp.html#sodiumfrp.primitives.Cell.listen).

When an input value is pushed into a stream or cell, Sodium automatically starts a *transaction*.
Any state changes, that occur as a result of that input, are performed within the same *transaction*.
Most of the time you don't need to do anything, but it is possible to start a transaction explicitly via
[`Transaction.run()`](https://sodium-python.readthedocs.io/en/latest/sodiumfrp.html#sodiumfrp.transaction.Transaction.run).
For example:
* It often makes sense for all the program initialization to be wrapped in a single, big transaction.
* `StreamLoop` and `CellLoop` require an explicit transaction.

### The Book

The most comprehensive guide on FRP and this library would be the book
[Functional Reactive Programming by Stephen Blackheath](https://www.manning.com/books/functional-reactive-programming).
Even though, the book aims Java, it is pretty straightforward to map it into Python.


## Examples

See [examples](examples) directory.


## Development

To run the tests, execute `pytest` from the package directory.

To build [API reference](https://sodium-python.readthedocs.io), go to `docs` directory and run `make html`.
It requires `sphinx` and `sphinx-rtd-theme` packages to be installed.


## License

Distributed under [BSD 3-Clause](https://github.com/SodiumFRP/sodium/blob/master/COPYING).
