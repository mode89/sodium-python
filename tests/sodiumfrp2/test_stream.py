from sodiumfrp2 import StreamSink

def test_send_stream() -> None:
    e: StreamSink[int] = StreamSink()
    out: List[int] = []
    unlisten = e.listen(out.append)
    e.send(5)
    unlisten()
    assert [5] == out
    e.send(6)
    assert [5] == out
