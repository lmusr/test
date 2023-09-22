from math import *

def task():
    """some function"""
    #input
    try:
        a = float(input( "a = "))
    except:
        print("Invalid integer!")
    else:
        #calculations
        num = sin(pi * radians(a))
        denom = pow(abs(a), 1/3) + sqrt(abs(a))
        b = ( num / denom)
        #output
        print("b = ", b)
        
def task1():
    pass

def task2():
    pass
