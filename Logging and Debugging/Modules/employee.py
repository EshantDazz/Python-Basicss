import logging
import saveToFile as STF


logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

f=logging.Formatter('%(levelname)s - %(message)s')

fh = logging.FileHandler('employee.log')
fh.setFormatter(f)

logger.addHandler(fh)


stream_handler = logging.StreamHandler()

logger.addHandler(stream_handler)

stream_handler.setFormatter(f)

#logging.basicConfig(filename='employee.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
logger.debug('Start of employee program')

name = 'imran'
age = 27
email = 'imran@gmail.com'

if STF.namecheck(name) is True:
    STF.saveData(name,age,email)
else:
    logger.critical('Employee check failed')


logger.debug('End of employee program')
logger.debug('######################')
