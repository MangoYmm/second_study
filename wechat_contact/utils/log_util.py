import logging
import os
import time

# create logger
logger = logging.getLogger('logger_utils')
# logger1 = logging.getLogger('simple_example1')
# self.logger.isEnabledFor(logging.ERROR)
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

curdate = time.strftime('%Y%m%d', time.localtime())
log_file_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs')
if not os.path.exists(log_file_dir):
    os.mkdir(log_file_dir)
log_file_path = os.path.join(log_file_dir, f'log_{curdate}.log')

# create file handler and set level to debug
fh = logging.FileHandler(log_file_path, encoding='utf-8')
fh.setLevel(logging.DEBUG)

# create formatter  - %(module)s - %(pathname)s
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(filename)s  - %(funcName)s - %(lineno)d - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)
logger.addHandler(fh)