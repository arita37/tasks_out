"""
python tasks/task_test/main.py


"""

import os, sys
from time import sleep

from aapackage import util_log

#LOG_FILE = "zlog/" + util_log.create_logfilename(__file__)
#APP_ID = util_log.create_appid(__file__)

logger = util_log.logger_setup(__name__,
                               log_file = "zlog/task_test_" + str(os.getpid()) + ".log",
                               formatter= util_log.FORMATTER_5)

def log(*argv):
    logger.info( ",".join( [  str(x) for x in argv  ]  ))



log("")
log("Ok, test_log")




log"start job")


import numpy as np 


a = np.random.rand(100, 5000)


for i in range(0, 30) :
     a = np.random.rand(100, 5000)
     sleep(2)
     # print( str(i))
     log(i, len(a))
 
log("finish")


    

