"""Code to take coordinates of each side and fold line and determine the 
plane of the fold line perpendicular to the base. Each side's coordinates are 
transformed onto this plane, and then the program checks for intersecting sides 
to determine whether or not to fold/unfold the sides."""

import numpy as np
import math
import collections

def move_to_actual_coord(old_side,xy_coordinates):
	move_side = list()
	for i in old_side:
		#old_side[old_side.index(i)][0]
		print xy_coordinates

def transform_side(side,theta):
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

	return new_side
	#moved_side = move_to_actual_coord(new_side,actual_coordinates)
	#return moved_side

"""def check_sides(sides,theta):
	Check if sides intersect, and output whether the angles of the side planes need to be changed or not
		Input: all side coordinates, plane equation 
		Output: side coordinates if proper, or neg/pos (for more or less angle) and side coordinates
	
	sides_dict = {}
	rev_sides_dict = {}
	count = 0
	#make list of vectors in each side
	for i in sides:
		key = sides.index(i)
		for j in range(1,len(i)):
			new_vector = (i[j][0]-i[j-1][0],i[j][1]-i[j-1][1],i[j][2]-i[j-1][2])
			#add to dictionary with side as key and vectors as values
			if key in sides_dict:
				sides_dict[key].append(new_vector)
			else:
				sides_dict[key] = [new_vector]

	#create dictionary with vectors as the keys
	for key, values in sides_dict.items():
		for value in values:
			if value in rev_sides_dict:
				rev_sides_dict[value].append(key)
			else:
				rev_sides_dict[value] = [key]

	#while sides_dict:
	for key,value in rev_sides_dict.items():
		if len(value) > 1:
			for i in value:
				if i in sides_dict:
					del sides_dict[i]
		else:
			for i in value:
				if i in sides_dict:
					theta-=1
					sides_dict[i] = transform_side(sides_dict[i],theta)
					print theta
					print sides_dict[i]
	return sides_dict"""

def check_sides(sides,side_dictionary,theta):
	rev_sides_dict = {}
	for key, values in side_dictionary.items():
		for value in values[0]:
			if value in rev_sides_dict:
				rev_sides_dict[value].append(key)
			else:
				rev_sides_dict[value] = [key]
	print rev_sides_dict

def make_dictionaries(sides,xy_coord):
	sides_old_coordinates = {}
	for i in range(0,len(sides)):
		val = sides[i]
		sides_old_coordinates[i] = [val]
		sides_old_coordinates[i].append(xy_coord[i])
	run_fxn = main(sides_old_coordinates)
	check_sides(run_fxn,sides_old_coordinates,90)
	#return run_fxn

def main(sides):
	"""call things"""
	theta = 90
	folded_sides = list()
	length = len(sides)
	for i in sides:
		side = sides[i][0]
		folded_sides.append(transform_side(side,theta))
	return folded_sides
	#sides = make_dictionaries
	#return folded_sides
	#return check_sides(folded_sides,theta)

side_coordinates = (([0,0],[0,6],[6,6],[6,0]),([0,0],[0,6],[6,6],[6,0]),([0,0],[0,6],[6,6],[6,0]),([0,0],[0,6],[6,6],[6,0]))
actual_coordinates = (([6,6],[6,0],[0,0],[0,6]),([0,6],[-6,6],[-6,12],[0,12]),([0,12],[0,18],[6,18],[6,12]),([6,12],[12,12],[12,6],[6,6]))
actual_fold_lines = ([0,12],[0,18],[0,18],[6,18],[6,18],[6,12],[6,12],[6,6],[0,6])

print make_dictionaries(side_coordinates,actual_coordinates)
#print main(side_coordinates,actual_coordinates)