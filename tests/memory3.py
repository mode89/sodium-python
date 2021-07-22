from pathlib import Path
import sys
from threading import Thread
from time import sleep
import tracemalloc as tm

sys.path.append(str(Path(__file__).parent.parent))
from sodiumfrp.core import Cell, StreamSink

def main() -> None:

    def thread() -> None:
        tm.start()
        while True:
            current, peak = tm.get_traced_memory()
            print(f"memory current: {current}, peak: {peak}")
            sleep(5)
    Thread(target=thread).start()

    et: StreamSink[int] = StreamSink()
    t: Cell[int] = et.hold(0)
    eChange: StreamSink[int] = StreamSink()
    oout = eChange.map(lambda x: t).hold(t)
    out = Cell.switch_cell(oout)
    l = out.listen(lambda tt: None)
    for i in range(1000000000):
        eChange.send(i)
    l.unlisten()

if __name__ == "__main__":
    main()
