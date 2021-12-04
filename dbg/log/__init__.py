import sys

#print(0, ".".join((__name__, "dbglog")))

# dynamic importing here!!! 
DEBUG = __import__(".".join((__name__, "dbglog")), None, None, "dbglog")

#print(1, DEBUG)
DEBUG.Base = sys.modules[__name__]           # actually i don't know what's this and the last line for 

sys.modules[__name__] = DEBUG
#print(2, sys.modules[__name__])
sys.modules[__name__+".Base"] = DEBUG.Base   # actually i don't know what's this for
