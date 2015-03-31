"""Shivali Chandra
Function that takes in lists of tuples that represent 2D-coordinates and convert them into 3D-coordinates.
Currently works for rectangles and squares, working to modify to add more functionality."""

import plotly.plotly as py
from plotly.graph_objs import *

def front_plane(front):
	new_front = [None]*len(front)
	#iterate through list of tuples, add z-dimension
	for i,(x,y) in enumerate(front):
		new_front[i] = (x,y,0)
	return new_front

def left_plane(left_side,start_x):
	left = [None]*len(left_side)
	#iterate through list of tuples, add z-dimension and change x-coordinates
	for i,(x,y) in enumerate(left_side):
		left[i] = (start_x,y,x)
	left_list = [list(k) for k in left]		#list of tuples to list of lists
	#switch coordinates to flip the face
	left_list[0][2],left_list[1][2],left_list[2][2],left_list[3][2] = left_list[1][2],left_list[0][2],left_list[3][2],left_list[2][2]
	new_left = [tuple(j) for j in left_list]	#list of lists to list of tuples
	return new_left

def right_plane(right_side,width):
	new_right = [None]*len(right_side)
	#iterate through list of tuples, add z-dimension and change x-coordinates
	for i,(x,y) in enumerate(right_side):
		new_right[i] = (width,y,x)
	return new_right

def back_plane(back,length):
	back_side = [None]*len(back)
	#iterate through list of tuples, add z-dimension
	for i,(x,y) in enumerate(back):
		back_side[i] = (x,y,length)
	back_list = [list(k) for k in back_side]	#list of tuples to list of lists
	#switch coordinates to flip the face
	back_list[0][0],back_list[1][0],back_list[2][0],back_list[3][0] = back_list[1][0],back_list[0][0],back_list[3][0],back_list[2][0]
	new_back = [tuple(j) for j in back_list]	#list of lists to list of tuples
	return new_back

def top_plane(top,height):
	new_top = [None]*len(top)
	#iterate through list of tuples, add z-dimension and change y-coordinates
	for i,(x,y) in enumerate(top):
		new_top[i] = (x,height,y)
	return new_top

def bottom_plane(bottom,start_y):
	bottom_side = [None]*len(bottom)
	#iterate through list of tuples, add z-dimension and change y-coordinates
	for i,(x,y) in enumerate(bottom):
		bottom_side[i] = (x,start_y,y)
	bottom_list = [list(k) for k in bottom_side]	#list of tuples to list of lists
	#switch coordinates to flip the face
	bottom_list[0][2],bottom_list[2][2],bottom_list[1][2],bottom_list[3][2] = bottom_list[2][2],bottom_list[0][2],bottom_list[3][2],bottom_list[1][2]
	new_bottom = [tuple(j) for j in bottom_list]	#list of lists to list of tuples
	return new_bottom

def make_shape(front,left_side,back,right_side,top,bottom):
	"""This function takes the 2D-coordinates as inputs, 
	calls each respective face function to get the 3D-coordinates, 
	and plots them to ensure that they are correct"""

	front_3D = front_plane(front)
	left_side_3D = left_plane(left_side,front_3D[0][0])
	right_side_3D = right_plane(right_side,front_3D[1][0])
	back_3D = back_plane(back,left_side_3D[0][2])
	top_3D = top_plane(top,front_3D[2][1])
	bottom_3D = bottom_plane(bottom,front_3D[0][1])

	trace1 = Scatter3d(
	    x=[int(i[0]) for i in front_3D],
	    y=[int(j[1]) for j in front_3D],
	    z=[int(k[2]) for k in front_3D],
	    mode='lines+markers',
	)
	trace2 = Scatter3d(
	    x=[int(i[0]) for i in left_side_3D],
	    y=[int(j[1]) for j in left_side_3D],
	    z=[int(k[2]) for k in left_side_3D],
	    mode='lines+markers',
	)
	trace3 = Scatter3d(
	    x=[int(i[0]) for i in right_side_3D],
	    y=[int(j[1]) for j in right_side_3D],
	    z=[int(k[2]) for k in right_side_3D],
	    mode='lines+markers',
	)
	trace4 = Scatter3d(
	    x=[int(i[0]) for i in back_3D],
	    y=[int(j[1]) for j in back_3D],
	    z=[int(k[2]) for k in back_3D],
	    mode='lines+markers',
	)
	trace5 = Scatter3d(
	    x=[int(i[0]) for i in top_3D],
	    y=[int(j[1]) for j in top_3D],
	    z=[int(k[2]) for k in top_3D],
	    mode='lines+markers',
	)
	trace6 = Scatter3d(
	    x=[int(i[0]) for i in bottom_3D],
	    y=[int(j[1]) for j in bottom_3D],
	    z=[int(k[2]) for k in bottom_3D],
	    mode='lines+markers',
	)
	data = Data([trace1,trace2,trace3,trace4,trace5,trace6])
	layout = Layout(
	    margin=Margin(
	        l=0,
	        r=0,
	        b=0,
	        t=0
	    )
	)
	fig = Figure(data=data, layout=layout)
	plot_url = py.plot(fig, filename='simple-3d-scatter')

	return "front:",front_3D,"left:",left_side_3D,"back:",back_3D,"right:",right_side_3D,"top:",top_3D,"bottom:",bottom_3D

#define each face for testing purposes
front_2D = [(0,0),(10,0),(10,5),(0,5)]
left_side_2D = [(0,0),(5,0),(5,5),(0,5)]
back_2D = [(0,0),(10,0),(10,5),(0,5)]
right_side_2D = [(0,0),(5,0),(5,5),(0,5)]
top_2D = [(0,0),(10,0),(10,5),(0,5)]
bottom_2D = [(0,0),(10,0),(10,5),(0,5)]
#convert coordinates
print make_shape(front_2D,left_side_2D,back_2D,right_side_2D,top_2D,bottom_2D)
