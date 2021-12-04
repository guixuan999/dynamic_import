
import sys

# pay attention to the following import clause!!!
from dbg.log import LOG

try:
    l = 1/0
except Exception:
    LOG.warning(' %s: %s'%(sys.exc_info()[0].__name__, str(sys.exc_info()[1])))
