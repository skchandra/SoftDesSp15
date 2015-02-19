from swampy.TurtleWorld import *

world = TurtleWorld()
beth = Turtle()

def draw_line(turtle,angle,start_x,start_y,line_length):
	"""Draws a line with the specified turtle.
	turtle: this is the turtle that will do the drawing
	angle: the angle in degress where 0 degrees is East
	start_x: starting x-coordinate for the line
	start_y: starting y-coordinate for the line
	line_length: the length of the line that should be drawn"""

	#first move to the appropriate starting location
	turtle.x = start_x
	turtle.y = start_y
	#turn the turtle to the appropriate angle
	turtle.lt(angle)
	#put the pen down, walk forward appropriate number of steps
	turtle.fd(line_length)


#draw_line(beth,45,0,0,200)

def my_square(turtle,start_x,start_y,side_length):
	my_regular_polygon(beth,start_x,start_y,4,side_length)

def my_regular_polygon(turtle,start_x,start_y,num_sides,side_length):
	turtle.x = start_x
	turtle.y = start_y
	angle = 180-((num_sides-2)*180)/num_sides
	for n in range(0,num_sides):
		turtle.fd(side_length)
		turtle.lt(angle)

import math
def my_circle(turtle,start_x,start_y,radius):
	x = start_x 
	y = start_y - radius
	circ = 2 * math.pi * radius
	m = math.sqrt(radius)
	n = int(circ / m)
	my_regular_polygon(turtle,x,y,n,m)

def snowflake_side(turtle,length,level):
	turtle.delay = 0.01
	if level > 0:
		turtle.x = level*level
		turtle.y = level*level
		turtle.fd(length)
		turtle.rt(60)
		turtle.fd(length)
		turtle.lt(120)
		turtle.fd(length)
		turtle.rt(60)
		turtle.fd(length)
		snowflake_side(turtle,float(length)/2.0,level-1)

def neg_snowflake_side(turtle,length,level):
	turtle.delay = 0.001
	if level > 0:
		turtle.x = level*level
		turtle.y = level*level
		turtle.fd(length)
		turtle.lt(60)
		turtle.fd(length)
		turtle.rt(120)
		turtle.fd(length)
		turtle.lt(60)
		turtle.fd(length)
		snowflake_side(turtle,float(length)/3.0,level-1)

def snowflake(turtle,length,level):
	for i in range(0,length*15):
		"""turtle.x = 0
		turtle.y = 0"""
		if i%2 != 0:
			snowflake_side(turtle,length,level)
			turtle.lt(360.0/(length*15))
		else:
			neg_snowflake_side(turtle,length,level)
			turtle.lt(360.0/(length*15))


snowflake(beth,20,6)
die(beth)

#my_circle(beth,0,0,100)
#my_regular_polygon(beth,0,0,7,20)
#my_square(beth,0,0,20)
wait_for_user()