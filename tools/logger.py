import sys
import traceback
from datetime import datetime

def log(*args, **kargs):
    print(datetime.now().strftime('[%Y/%m/%d %H:%M:%S]'), *args, **kargs)

def log_err(*args, **kargs):
    log(*args, file=sys.stderr, **kargs)

def exception_dump():
    exc_type, exc_value, exc_traceback = sys.exc_info()
    error_strings = traceback.format_exception(exc_type,
                                               exc_value,
                                               exc_traceback,
                                               limit=100)
    log('\n'.join(error_strings), file=sys.stderr)
