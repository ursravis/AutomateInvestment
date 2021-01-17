

import emailhelper
import logging

logging.basicConfig(filename='logs/logfile.log',level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


logging.info('Starting process')
emailhelper.sendmail("login Succeed")
logging.info('Cmpleted process')