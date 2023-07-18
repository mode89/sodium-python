from contextlib import contextmanager
from threading import Lock
from typing import Callable, Generic, Iterator, List, TypeVar

A = TypeVar("A")
Listener = Callable[[A], None]
Unlisten = Callable[[], None]
GraphNodeAction = Callable[[A], None]

class Transaction:

    _lock = Lock()


@contextmanager
def transaction() -> Iterator[Transaction]:
    with Transaction._lock:
        yield Transaction()


class GraphNode:

    def __init__(self, rank: int, action: GraphNodeAction) -> None:
        self._rank = rank
        self._action = action
        self._downstream: List[GraphNode] = []


class Stream(Generic[A], GraphNode):

    def __init__(self, rank: int, action: GraphNodeAction) -> None:
        GraphNode.__init__(self, rank, action)

    def listen(self, f: Listener) -> Unlisten:
        with transaction():
            listener_node = GraphNode(self._rank + 1, f)
            self._downstream.append(listener_node)
            def unlisten() -> None:
                self._downstream.remove(listener_node)
            return unlisten


class StreamSink(Stream[A]):

    def __init__(self) -> None:
        Stream.__init__(self, 0, lambda _: None)

    def send(self, a: A) -> None:
        with transaction():
            pass
