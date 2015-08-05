# On start, environment should be clean, no vars/imports
# from runinpkg.py should leak into script being run.
#print(fname)
#print(sys)

# Arguments should be as expected with direct script invocation.
import sys
print(sys.argv)

# And of course, relative imports should work!
from . import mod1

