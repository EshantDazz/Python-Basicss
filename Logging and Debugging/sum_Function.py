import logging as lg

lg.basicConfig(level=lg.INFO,filename='sumLog.log')

def addition(*args):
    lg.info("This is my addition function")
    sum=0
    for i in args:
        lg.info(str(i))
        sum+=i
    return sum

f=open('sumLog.log','r')
print(f.read())

print(addition(34,56,1))
