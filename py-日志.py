import logging
from logging.handlers import TimedRotatingFileHandler
log = logging.getLogger()
file_name = "./test.log"
logformatter = logging.Formatter('%(asctime)s [%(levelname)s]|%(message)s')
loghandle = TimedRotatingFileHandler(file_name, 'midnight', 1, 2)
loghandle.setFormatter(logformatter)
loghandle.suffix = '%Y%m%d'
log.addHandler(loghandle)
log.setLevel(logging.DEBUG)

log.debug("init successful")
