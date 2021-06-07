""" Add Function """
def add(x,y):
    return x+y
""" Subtract Function """
def sub(x,y):
    return x-y
""" Multiplication Function """
def mul(x,y):
    return x*y
""" Division Function """
def div(x,y):
    if y==0:
        raise ValueError('Division by zero not allowed.')
    return x/y

## Check function is working
#print(add(5,3))