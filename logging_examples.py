# video completo https://www.youtube.com/watch?v=p0A4CV4MWd0
# https://realpython.com/python-logging/
'''
logging.DEBUG	10	"DEBUG"
logging.INFO	20	"INFO"
logging.WARNING	30	"WARNING"
logging.ERROR	40	"ERROR"
logging.CRITICAL	50	"CRITICAL"
'''

import logging
def clear_log_cache():
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged.')
#DEBUG:root:This will get logged.

logging.info('This will get logged.')

clear_log_cache() 

logging.basicConfig(format="%(message)s:%(levelname)s:%(name)s")
logging.warning("Hello, Warning! New configurations")

clear_log_cache()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.debug("Hello, New Debug!")

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.critical("Hello, Critical Finish!")    
