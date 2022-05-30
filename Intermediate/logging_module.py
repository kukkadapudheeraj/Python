# from distutils.debug import DEBUG
import logging

'''
five levels of logging

logging.debug('this is a debug message')
logging.info('this is a info message')
logging.warning('this is a warning message')
logging.error('this is a error message')
logging.critical('this is a critical message')
'''

logging.basicConfig(level=logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%y %H:%M:%S')
logging.debug('this is a debug message')
logging.info('this is a info message')
logging.warning('this is a warning message')
logging.error('this is a error message')
logging.critical('this is a critical message')

# creating your own logger

logger = logging.getLogger(__name__)

logger.info("This is info")

#create logging stream handler

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')

# level and format setting

stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)


stream_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(stream_formatter)
file_handler.setFormatter(stream_formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning("this is a warning")
logger.error('This is a error')

