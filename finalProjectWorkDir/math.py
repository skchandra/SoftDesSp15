from scipy.optimize import fsolve
import math

def equations(p):
    x, y,g,d= (i for i in p)
    return (x+y**2-4, math.exp(x) + x*y - 3)

x, y =  fsolve(equations,(1,1,3,3))

print equations((x,y,3,3))
