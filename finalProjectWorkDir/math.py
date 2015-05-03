from scipy.optimize import fsolve
import math

"""def equations(p,*args):
    x, y = p

    return (x+y**2-4, math.exp(x) + x*y - 3)

slope = 7
dist = 3
x, y =  fsolve(equations,(1,1),args = (slope,dist))

print equations((x,y))"""

import warnings
warnings.filterwarnings('ignore', 'The iteration is not making good progress')

def find_coordinates(p1,x1,y1,axis_x1,axis_y1,axis_x2,axis_y2,theta):
	if (axis_x2>axis_x1) and (axis_y2-axis_y1==0):
		if math.degrees(theta) <= 90:
			x,y = p1[0],axis_y2+math.fabs(p1[1]-y1)
		else:
			x,y = p1[0],axis_y2-math.fabs(p1[1]-y1)
	elif (axis_x2<axis_x1) and (axis_y2-axis_y1==0):
		if math.degrees(theta) <= 90:
			x,y = p1[0],axis_y2-math.fabs(p1[1]-y1)
		else:
			x,y = p1[0],axis_y2+math.fabs(p1[1]-y1)
	elif (axis_y2>axis_y1) and (axis_x2-axis_x1==0):
		if math.degrees(theta) <= 90:
			x,y = axis_x2-math.fabs(p1[0]-x1),p1[1]
		else:
			x,y = axis_x2+math.fabs(p1[0]-x1),p1[1]
	elif (axis_y2<axis_y1) and (axis_x2-axis_x1==0):
		if math.degrees(theta) <= 90:
			x,y = axis_x2+math.fabs(p1[0]-x1),p1[1]
		else:
			x,y = axis_x2-math.fabs(p1[0]-x1),p1[1]
	else:
		#slope of actual folding line
		axis_slope = (axis_y2-axis_y1)/(axis_x2-axis_x1)
		print 'axis',axis_slope
		#slope of final coordinate
		point_slope = -1/axis_slope
		print 'point',point_slope
		#intersection point of not-translated coordinate, base folding line
		int_x,int_y = p1[0],0
		#distance between intersection point and right axis coordinate (not-translated)
		axis_dist = x1-int_x
		point_dist = p1[1]-y1
		print axis_dist,point_dist
		#calculating intersection point on actual folding line
		intersect_x = axis_x2 - (axis_dist*(1/math.sqrt(1+(point_slope**2))))
		intersect_y = axis_y2 - (axis_dist*(point_slope/math.sqrt(1+(point_slope**2))))
		print intersect_x,intersect_y
		#find final translated x,y coordinates
		if math.degrees(theta) <= 90:
			x = axis_x2 - (point_dist*(1/math.sqrt(1+(point_slope**2))))
			y = axis_y2 - (point_dist*(point_slope/math.sqrt(1+(point_slope**2))))
		else:
			x = axis_x2 + (point_dist*(1/math.sqrt(1+(point_slope**2))))
			y = axis_y2 + (point_dist*(point_slope/math.sqrt(1+(point_slope**2))))
	return x,y

print find_coordinates((4.0,3.0),5.0,0.0,3.0,0.0,6.0,4.0,1.57)