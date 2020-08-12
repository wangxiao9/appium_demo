__author__ = 'wangxiao'

import logging

formatters = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
datefmt = '%a, %d %b %Y %H:%M:%S'
filename = '../log/test.log'
logging.basicConfig(level=logging.DEBUG,
                    format=formatters,
                    datefmt=datefmt,
                    filename=filename,
                    filemode='w')


def debug(message):
    logging.debug(message)


def info(message):
    logging.info(message)


def warning(message):
    logging.warning(message)


def error(message):
    logging.error(message)


if __name__ == '__main__':
    error('cesss')
