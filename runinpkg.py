_org_globals = globals().copy()
import sys

class LocalPkg:
    __path__ = ["."]
    __name__ = "@"

sys.modules[""] = sys.modules["@"] = LocalPkg()

fname = sys.argv[1]
sys.argv = sys.argv[1:]
exec(open(fname).read(), _org_globals)
