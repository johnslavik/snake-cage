from asyncio.events import _Local
from traceback import print_tb
from warnings import warn

def _Local__del__(self, _warn=warn, _ptb=print_tb):
    loop = self._loop
    if loop and not loop.is_closed():
        _warn(f"unclosed event loop {loop!r}", ResourceWarning, source=loop)
        if not self.is_running():
            try:
                self.close()
            except Exception as e:
                _ptb(exc.__traceback__)

_Local.__del__ = _Local__del__

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(asyncio.sleep(1))
