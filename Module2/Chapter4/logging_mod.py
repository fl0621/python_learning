#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

import logging


# log level greater than or equal to INFO will be logged.
# logging.basicConfig(filename='logging.log', level=logging.INFO, format='%(asctime)s %(message)s',
#                     datefmt='%Y/%m/%d %I:%M:%S %p')
#
# logging.debug('test debug log')
# logging.info('test info log')
# logging.warning('test warning log')


# logging filter
class IgnoreBackupLogFilter(logging.Filter):
    def filter(self, record):
        return "db backup" not in record.getMessage()


# 1.create logger object
logger01 = logging.getLogger("database")
logger01.setLevel(logging.DEBUG)

# 1.1 add filter object to logger
logger01.addFilter(IgnoreBackupLogFilter())

# 2.create handler object
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
fh = logging.FileHandler("log_adv.log")
fh.setLevel(logging.WARNING)
from logging import handlers

# Size rotating file handler.
srth = handlers.RotatingFileHandler("srt.log", maxBytes=10, backupCount=3)
# Time rotating file handler, log to new file every 5 seconds and keep max 3 files.
trth = handlers.TimedRotatingFileHandler("trt.log", when="S", interval=5, backupCount=3)

# 2.1 bind handler object to logger
logger01.addHandler(ch)
logger01.addHandler(fh)

# 3create formatter object
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(message)s')
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)d -%(message)s')

# 3.1 bind formatter object to handler
ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)

# logger01.debug("test debug")
# logger01.info("test info")
logger01.warning("test db backup warning")


