from contextlib import contextmanager
#import numpy as np
#import tensorflow as tf

'''
@contextmanager
def checkcontext(**args):
    print("before context")
    yield args.items()
    print("Outside of context")

kargs={'name': 'tensor', 'stack': 'lamp'}
with checkcontext(**kargs) as c:
    print(c)
    #x=lambda values: [(value, key) for key, value in values if value is not None]
    #print(x(c))


def tee(name, stack, /):
    print(name, stack)

data=['ddd','qqqq']
'''

class A(object):
     def __init__(self,**args):
         self.args = args

     def __enter__(self):
         yield self.args.items()
     def __exit__(self, exc_type, exc_value, traceback):
         print(traceback)

kargs={'name': 'tensor', 'stack': 'lamp'}
with A(**kargs) as a:
   print([(key,value) for key,value in a])
