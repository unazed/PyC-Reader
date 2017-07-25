from sys import argv
from marshal import loads
from struct import unpack
from time import localtime
from dis import dis


assert len(argv) == 2  # python file.py <path-to-pyc>

with open(argv[1]) as _pyc:
    pyc = _pyc.read()

magic, mod_timestamp, marsh_obj = pyc[0:4], localtime(unpack("<L", pyc[4:8])[0]), pyc[8:]
mod_timestamp = "%d:%d" % (mod_timestamp.tm_hour, mod_timestamp.tm_min)
code_obj = loads(marsh_obj)

print("".join(["%s: %s\n" % (attr, repr(getattr(code_obj, attr))) for attr in dir(code_obj) if not attr.startswith('_')]))
print("Time modified: " + mod_timestamp)
