import logging

logging.basicConfig(level=logging.DEBUG) #if we remive this we won't be getting any output

def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x//y


n1=10
n2=20

sum=add(n1,n2)
logging.debug(sum)
diff=substract(n1,n2)
logging.debug(diff)
mul=multiply(n1,n2)
logging.debug(mul)
div=divide(n2,n1)
logging.debug(div)