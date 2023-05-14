import logging

#type python logging library in google
logging.basicConfig(filename='test2.log',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

def namecheck(name):
    if len(name)<2:
        logging.debug('checking for name length')
        return 'Invalid name'
    elif name.isspace():
        logging.debug('checking for name has space')
        return 'Invalid name'
    elif name.isalpha():
        logging.debug('checking for name is alphabet')
        return 'valid name'
    elif name.replace(' ','').isalpha():
        logging.debug('checking for full name')
        return 'name is valid'
    else:
        logging.error('failed all checks')
        return 'invalid name'


print(namecheck('Eshant'))
print(namecheck('popat lal'))
print(namecheck('dev stupid 234'))
