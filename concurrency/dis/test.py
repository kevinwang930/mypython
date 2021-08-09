import datetime
import time
import types
@types.coroutine
def sleep(seconds):
    """Pause a coroutine for the specified number of seconds.

    Think of this as being like asyncio.sleep()/curio.sleep().
    """
    
    now = datetime.datetime.now()
    time.sleep(1)
    wait_until = now + datetime.timedelta(seconds=seconds)
    # Make all coroutines on the call stack pause; the need to use `yield`
    # necessitates this be generator-based and not an async-based coroutine.
    actual = yield wait_until
    # Resume the execution stack, sending back how long we actually waited.
    print(actual - now)
    return actual - now


async def test():
    delta = await sleep(3)
    print(f'sleep finished {delta}')

a = test()
t = a.send(None)

now = datetime.datetime.now()
try:
    a.send(now)
except StopIteration as exc:
    pass

