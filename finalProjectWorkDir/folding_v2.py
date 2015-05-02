"""Shivali Chandra
Restructured code that takes coordinates of sides and axes of rotation, and rotates the sides 
until they meet, forming a closed 3D shape.
"""

import numpy as np
import math
import collections
from scipy.optimize import fsolve

def find_intersection_distances(p1,y1,x1,y2,x2):
	if y2-y1 == 0:
		dist = math.fabs(p1[1]-y1)
	elif x2-x1 == 0:
		dist = math.fabs(p1[0]-x1)
	else:
		axis_line_slope = (y2-y1)/(x2-x1)
		perp_slope = -1/(axis_line_slope)
		c1 = axis_line_slope * x1 - y1
		c2 = perp_slope * p1[0] - p1[1]
		x_intersect = (c2 - c1)/(perp_slope - axis_line_slope)
		y_intersect = perp_slope * x_intersect + c2
		eq1_slope = ((p1)) 
		dist = math.sqrt((x_intersect-p1[0])**2+(y_intersect-p1[1])**2)

	return dist

def equations(p):
    x,y,x2,y2,slope,dist = p
    return ((y2-y)/(x2-x)-slope, math.sqrt((y2-x)**2+(x2-y)**2)-dist)

x,y =  fsolve(equations,(1,1,1,1,1,1))

def find_coordinates(p1,x1,y1,axis_x1,axis_y1,axis_x2,axis_y2,theta):
	if (axis_x2>axis_x1) and (axis_y2-axis_y1==0):
		if math.degrees(theta) <= 90:
			trans_x,trans_y = p1[0],axis_y2+math.fabs(p1[1]-y1)
		else:
			trans_x,trans_y = p1[0],axis_y2-math.fabs(p1[1]-y1)
	elif (axis_x2<axis_x1) and (axis_y2-axis_y1==0):
		if math.degrees(theta) <= 90:
			trans_x,trans_y = p1[0],axis_y2-math.fabs(p1[1]-y1)
		else:
			trans_x,trans_y = p1[0],axis_y2+math.fabs(p1[1]-y1)
	elif (axis_y2>axis_y1) and (axis_x2-axis_x1==0):
		if math.degrees(theta) <= 90:
			trans_x,trans_y = axis_x2-math.fabs(p1[0]-x1),p1[1]
		else:
			trans_x,trans_y = axis_x2+math.fabs(p1[0]-x1),p1[1]
	elif (axis_y2<axis_y1) and (axis_x2-axis_x1==0):
		if math.degrees(theta) <= 90:
			trans_x,trans_y = axis_x2+math.fabs(p1[0]-x1),p1[1]
		else:
			trans_x,trans_y = axis_x2-math.fabs(p1[0]-x1),p1[1]
	else:
		axis_slope = (axis_y2-axis_y1)/(axis_x2-axis_x1)
		point_slope = (y1-p1[1])/(x1-p1[0])
		dist = math.sqrt((y1-p1[1])**2+(x1-p1[0])**2)
	print equations((x,y,axis_x2,axis_y2,point_slope,dist))

print find_coordinates((3,4),5,5,5,6,4,0,3)

def move_to_actual_coord(old_side,side_dict,side_num,theta):
	"""Change the xy coordinates of the sides to the correct values from the original image
		Input: side coordinates, sides dictionary
		Output: new side coordinates in the sides dictionary	
	"""
	final_side = list()
	y1 = old_side[0][1]
	x1 = old_side[0][0]
	y2 = old_side[len(old_side)-1][1]
	x2 = old_side[len(old_side)-1][0]
	new_xaxis = side_dict[side_num][1][len(old_side)-1][0]
	new_xaxis1 = side_dict[side_num][1][0][0]
	new_yaxis = side_dict[side_num][1][len(old_side)-1][1]
	new_yaxis1 = side_dict[side_num][1][0][1]

	for i,j in enumerate(old_side):
		x = side_dict[side_num][1][i][0]
		y = side_dict[side_num][1][i][1]
		dist = find_intersection_distances((j[0],j[1]),y1,x1,y2,x2)
		coordinates = {1:(x,(dist+new_yaxis)),2:(x,(new_yaxis-dist)),3:((new_xaxis-dist),y),4:((new_xaxis+dist),y)}
		if (new_xaxis>new_xaxis1) and (new_yaxis-new_yaxis1==0):
			if math.degrees(theta) <= 90:
				[fin_x,fin_y] = coordinates[1]
			else:
				[fin_x,fin_y] = coordinates[2]
		elif (new_xaxis<new_xaxis1) and (new_yaxis-new_yaxis1==0):
			if math.degrees(theta) <= 90: 
				[fin_x,fin_y] = coordinates[2]
			else:
				[fin_x,fin_y] = coordinates[1]
		elif (new_yaxis>new_yaxis1) and (new_xaxis-new_xaxis1==0):
			if math.degrees(theta) <= 90:
				[fin_x,fin_y] = coordinates[3]
			else:
				[fin_x,fin_y] = coordinates[4]
		else:
			if math.degrees(theta) <=90:
				[fin_x,fin_y] = coordinates[4]
			else:
				[fin_x,fin_y] = coordinates[3]

		
		z = j[2]

		final_coord = fin_x/1.0,fin_y/1.0,z
		final_coord = list(final_coord)
		final_side.append(final_coord)
	side_dict[side_num] = list(side_dict[side_num])
	side_dict[side_num].append(final_side)
	return side_dict

def transform_side(side_num,side_dict,theta):
	"""Transform the coordinates of the side onto the perpendicular plane using Euler-Rodrigues formula
		Input: side coordinates, plane
		Output: new coordinates
	"""
	side = side_dict[side_num][0]
	new_side = list()
	#calculating axis of rotation
	axis = side[len(side)-1][0]-side[0][0],0.0,0.0
	#converting theta to radians
	rad = math.radians(theta)
	for i in side: 
		#calculating vector for each point in side
		side_vector = i[0],i[1],0.0
		#Euler-Rodrigues formula to rotate vectors
		axis = np.asarray(axis)
		theta = np.asarray(rad)
		axis = axis/math.sqrt(np.dot(axis, axis))
		a = math.cos(theta/2.0)
		b, c, d = -axis*math.sin(theta/2.0)
		aa, bb, cc, dd = a*a, b*b, c*c, d*d
		bc, ad, ac, ab, bd, cd = b*c, a*d, a*c, a*b, b*d, c*d
		multiplier = np.array([[aa+bb-cc-dd, 2.0*(bc+ad), 2.0*(bd-ac)],
					[2.0*(bc-ad), aa+cc-bb-dd, 2.0*(cd+ab)],
					[2.0*(bd+ac), 2.0*(cd-ab), aa+dd-bb-cc]])
		transform_vector = (np.dot(multiplier, side_vector))
		#round points to nearest whole number, add to list of transformed side coordinates
		folded_vector = round(transform_vector[0]),round(transform_vector[1]),round(transform_vector[2])
		new_side.append(folded_vector)

	moved_side = move_to_actual_coord(new_side,side_dict,side_num,theta)
	return moved_side

def output(theta,final_list):
	x = list()
	y = list()
	z = list()
	final_coordinates = []
	for i in final_list:
		final_coordinates.append(final_list[i][2]) 
	for i in final_coordinates:
		for j in i: 
			x.append(j[0])
			y.append(j[1])
			z.append(j[2])
	return x,y,z

def check_sides(run,temp,theta,fin):
	vector_sides = temp
	data = []
	redo_sides = {}
	new_run = {}
	for i in run: 
		position = run[i][2]
		for j in range(1,len(position)):
			if ((position[j][0]==position[j-1][0]) or (position[j][1]==position[j-1][1])) and (position[j][2]>position[j-1][2]):
				key = str(position[j])+str(position[j-1])
			elif ((position[j][0]>position[j-1][0]) or (position[j][1]>position[j-1][1])):
				key = str(position[j])+str(position[j-1])
			else:
				key = str(position[j-1])+str(position[j])
			if key in vector_sides:
				vector_sides[key].append(i)
			else: 
				vector_sides[key] = [i]
	for k in vector_sides:
		if len(vector_sides[k])>1:
			data.append(vector_sides[k][0])
			data.append(vector_sides[k][1])
	new_side_list = list(set(run.keys())-set(data))
	if not new_side_list:
		return theta,run
	else:
		new_t = theta+1
		for i in run.keys():
			if i in new_side_list:
				redo_sides[i] = [run[i][0]]
				redo_sides[i].append(run[i][1])
			else:
				new_run[i] = run[i]
			redone = transform_side(i,redo_sides,new_t)
		final = redone.copy()
		final.update(new_run)
		return check_sides(redone,new_run,new_t,final)

def make_sides(sides,theta):
	"""call things"""
	length = len(sides)
	for i in sides:
		side = sides[i][0]
		transformed_side = transform_side(i,sides,theta)
	return transformed_side

def main(sides,xy_coord):
	#create dictionary of sides as keys, both sets of xy coordinates as values
	theta = 0
	sides_old_coordinates = {}
	for i in range(0,len(sides)):
		val1 = sides[i]
		val2 = xy_coord[i]
		if i not in sides_old_coordinates:
			sides_old_coordinates[i] = val1,val2
	run_fxn = make_sides(sides_old_coordinates,theta)
	final_sides = check_sides(run_fxn,{},theta,{})
	return output(final_sides[0],final_sides[1])
	
if __name__ == "__main__":

	"""CUBE WORKS
	side_coordinates = (([0,0],[0,6],[6,6],[6,0]),([0,0],[0,6],[6,6],[6,0]),([0,0],[0,6],[6,6],[6,0]),([0,0],[0,6],[6,6],[6,0]))
	actual_coordinates = (([6,6],[0,6],[0,12],[6,12]),([6,12],[6,18],[12,18],[12,12]),([12,12],[18,12],[18,6],[12,6]),([12,6],[12,0],[6,0],[6,6]))

	print main(side_coordinates,actual_coordinates)"""

	"""PYRAMID DOESN'T WORK
	side_coordinates = (([0,0],[3,6],[6,0]),([0,0],[3,6],[6,0]),([0,0],[3,6],[6,0]))
	actual_coordinates = (([6,0],[0,0],[3,6]),([3,6],[6,12],[9,6]),([9,6],[12,0],[6,0]))
	print main(side_coordinates,actual_coordinates)"""

	"""SQUARE PYRAMID WORKS
	side_coordinates = (([0,0],[3,6],[6,0]),([0,0],[3,6],[6,0]),([0,0],[3,6],[6,0]),([0,0],[3,6],[6,0]))
	actual_coordinates = (([6,6],[0,9],[6,12]),([6,12],[9,18],[12,12]),([12,12],[18,9],[12,6]),([12,6],[9,0],[6,6]))
	print main(side_coordinates,actual_coordinates)"""

	"""TRIANGULAR PRISM WIP
	side_coordinates = (([0,0],[0,6],[6,6],[6,0]),([0,0],[3,6],[6,0]),([0,0],[0,6],[6,6],[6,0]),([0,0],[3,6],[6,0]))
	actual_coordinates = (([6,6],[0,6],[0,12],[6,12]),([6,12],[9,18],[12,12]),([12,12],[18,12],[18,6],[12,6]),([12,6],[9,0],[6,6]))

	print main(side_coordinates,actual_coordinates)"""

