#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

import logging

# log level grater than INFO will be logged to file
logging.basicConfig(filename='logging.log', level=logging.INFO, format='%(asctime)s %(message)s',
                    datefmt='%Y/%m/%d %I:%M:%S %p')

logging.debug('test debug log')
logging.info('test info log')
logging.warning('test warning log')
