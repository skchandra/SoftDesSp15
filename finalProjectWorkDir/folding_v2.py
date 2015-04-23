"""Shivali Chandra
Restructured code that takes coordinates of sides and axes of rotation, and rotates the sides 
until they meet, forming a closed 3D shape.
"""

import numpy as np
import math

def move_to_actual_coord(old_side,side_dict,side_num,theta):
	"""Change the xy coordinates of the sides to the correct values from the original image
		Input: side coordinates, sides dictionary
		Output: new side coordinates in the sides dictionary	
	"""
	final_side = list()
	move_side = list()
	rotate = 0
	yes = False
	no = False
	if side_dict[side_num][1][0][1]<side_dict[side_num][1][len(old_side)-1][1]:
		rotate = 6
	for j,i in enumerate(old_side):
		new_x = side_dict[side_num][1][j][0]
		#rotate side coordinates if needed
		if rotate > 0:
			print side_dict[side_num][1],
			yes = True
		while rotate > 0:
			side_dict[side_num][1] = np.roll(side_dict[side_num][1],1)
			rotate-=1
		if yes:
			print side_dict[side_num][1]
			no = True
		x_diff = side_dict[side_num][0][j][0] - i[0]
		x_diff = 0
		new_y = side_dict[side_num][1][j][1]
		y_diff = side_dict[side_num][0][j][1] - i[1]
		y_diff = 0
		z = i[2]
		final_coord = new_x-x_diff,new_y-y_diff,z
		final_side.append(final_coord)
	side_dict[side_num].append(final_side)
	if no:
		print side_dict[side_num][2]
		no = False
		yes = False

def transform_side(side,theta,xy_coord,side_num):
	"""Transform the coordinates of the side onto the perpendicular plane using Euler-Rodrigues formula
		Input: side coordinates, plane
		Output: new coordinates
	"""
	new_side = list()
	#calculating axis of rotation
	axis = side[len(side)-1][0]-side[0][0],0,0
	#converting theta to radians
	rad = math.radians(theta)
	for i in side: 
		#calculating vector for each point in side
		side_vector = i[0],i[1],0
		#Euler-Rodrigues formula to rotate vectors
		axis = np.asarray(axis)
		theta = np.asarray(rad)
		axis = axis/math.sqrt(np.dot(axis, axis))
		a = math.cos(theta/2)
		b, c, d = -axis*math.sin(theta/2)
		aa, bb, cc, dd = a*a, b*b, c*c, d*d
		bc, ad, ac, ab, bd, cd = b*c, a*d, a*c, a*b, b*d, c*d
		multiplier = np.array([[aa+bb-cc-dd, 2*(bc+ad), 2*(bd-ac)],
					[2*(bc-ad), aa+cc-bb-dd, 2*(cd+ab)],
					[2*(bd+ac), 2*(cd-ab), aa+dd-bb-cc]])
		transform_vector = (np.dot(multiplier, side_vector))
		#round points to nearest whole number, add to list of transformed side coordinates
		folded_vector = round(transform_vector[0]),round(transform_vector[1]),round(transform_vector[2])
		new_side.append(folded_vector)

	moved_side = move_to_actual_coord(new_side,xy_coord,side_num,theta)
	return moved_side

def make_dictionaries(sides,xy_coord):
	#create dictionary of sides as keys, both sets of xy coordinates as values
	sides_old_coordinates = {}
	for i in range(0,len(sides)):
		val = sides[i]
		sides_old_coordinates[i] = [val]
		sides_old_coordinates[i].append(xy_coord[i])
	run_fxn = main(sides_old_coordinates,sides_old_coordinates)
	#check_sides(run_fxn,sides_old_coordinates,90)
	#return run_fxn

def main(sides,xy_coordinates):
	"""call things"""
	theta = 0
	folded_sides = list()
	length = len(sides)
	for i in sides:
		side = sides[i][0]
		folded_sides.append(transform_side(side,theta,xy_coordinates,i))
	return folded_sides

side_coordinates = (((0,0),(0,6),(6,6),(6,0)),((0,0),(0,6),(6,6),(6,0)),((0,0),(0,6),(6,6),(6,0)),((0,0),(0,6),(6,6),(6,0)))
actual_coordinates = (((6,6),(0,6),(0,12),(6,12)),((6,12),(6,18),(12,18),(12,12)),((12,12),(18,12),(18,6),(12,6)),((12,6),(12,0),(6,0),(6,6)))

print make_dictionaries(side_coordinates,actual_coordinates)