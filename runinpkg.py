_org_globals = globals().copy()
import sys

class LocalPkg:
    __path__ = ["."]
    __name__ = "@"

sys.modules[""] = sys.modules["@"] = LocalPkg()

# Note: __init__.py support is experimental
# Form "from .mod import ..." is known to re-import module previously
# import by "from . import mod".
try:
    # Check for file presense, to avoid overriding
    # ImportError handling for __import__
    open("__init__.py")
except OSError:
    pass
else:
    init = __import__("__init__")
    # Seems to work even without below
    init.__path__ = ["."]
    init.__name__ = "@"
    sys.modules[""] = sys.modules["@"] = init

fname = sys.argv[1]
sys.argv = sys.argv[1:]
exec(open(fname).read(), _org_globals)
