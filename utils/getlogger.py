from logging.handlers import  RotatingFileHandler
import  logging
import time
import os
import sys


def getlogger(mod_name:str,filepath='',level=logging.INFO,propagate=False,maxBytes=10*1,backcount=5):#backcount=5
    logger =logging.getLogger(mod_name)
    logger.setLevel(level)
    logger.propagate = propagate #阻止传递到父logger



    PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(PROJECT_PATH)
    if filepath == '':
        filepath = os.path.join(PROJECT_PATH, "logs", "{}.log".format(os.path.basename(__file__).split('.')[0]))
    else:
        filepath = "d:/test.log"

    handler=logging.handlers.RotatingFileHandler(filename=filepath,maxBytes=10*1024*1024,encoding='utf-8',backupCount=5)#
    handler.setLevel(level)
    formatter =logging.Formatter(fmt='%(asctime)s [%(levelname)s %(funcName)s] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger









