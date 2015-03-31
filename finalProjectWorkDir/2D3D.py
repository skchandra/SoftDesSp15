"""Shivali Chandra
Function that takes in lists of tuples that represent 2D-coordinates and convert them into 3D-coordinates"""

import plotly.plotly as py
from plotly.graph_objs import *

def two_D_three_D(front,left_side,back,right_side,top,bottom):
	front_3D = [(front[0][0],front[0][1],0),(front[1][0],front[1][1],0),(front[2][0],front[2][1],0),(front[3][0],front[3][1],0)]
	start_x_bottom = front_3D[0][0]
	start_x_top = front_3D[3][0]
	left_side_3D = [(start_x_bottom,left_side[0][1],left_side[1][0]),(start_x_bottom,left_side[1][1],left_side[0][0]),(start_x_top,left_side[2][1],left_side[3][0]),(start_x_top,left_side[3][1],left_side[2][0])]
	width_bottom = left_side_3D[0][2]-left_side_3D[1][2]
	width_top = left_side_3D[3][2]-left_side_3D[2][2]
	#Need to flip back!!!!!!!!!
	back_3D = [(back[0][0],back[0][1],width_bottom),(back[1][0],back[1][1],width_bottom),(back[2][0],back[2][1],width_top),(back[3][0],back[3][1],width_top)]
	length = front_3D[1][0]-front_3D[0][0]
	right_side_3D = [(length,right_side[0][1],right_side[0][0]),(length,right_side[1][1],right_side[1][0]),(length,right_side[2][1],right_side[2][0]),(length,right_side[3][1],right_side[3][0])]
	height = front_3D[2][1]-front_3D[1][1]
	top_3D = [(top[0][0],height,top[0][1]),(top[1][0],height,top[1][1]),(top[2][0],height,top[2][1]),(top[3][0],height,top[3][1])]
	start_y = front_3D[0][1]
	bottom_3D = [(bottom[0][0],start_y,bottom[0][1]),(bottom[1][0],start_y,bottom[1][1]),(bottom[2][0],start_y,bottom[2][1]),(bottom[3][0],start_y,bottom[3][1])]
	

	"""x, y, z = zip(*front_3D)
	z = map(float, z)
	grid_x, grid_y = np.mgrid[0:5:100j,0:5:100j]
	grid_z = griddata((x, y),z,(grid_x, grid_y), method='cubic')

	fig = plt.figure()
	ax = fig.gca(projection='3d')
	ax.plot_surface(grid_x, grid_y, grid_z, cmap=plt.cm.Spectral)
	#plt.show()"""

	b = [int(i[0]) for i in front_3D]
	c = [int(i[1]) for i in front_3D]
	d = [int(i[2]) for i in front_3D]
	b1 = [int(i[0]) for i in left_side_3D]
	c1 = [int(i[1]) for i in left_side_3D]
	d1 = [int(i[2]) for i in left_side_3D]
	b2 = [int(i[0]) for i in back_3D]
	c2 = [int(i[1]) for i in back_3D]
	d2 = [int(i[2]) for i in back_3D]
	b3 = [int(i[0]) for i in right_side_3D]
	c3 = [int(i[1]) for i in right_side_3D]
	d3 = [int(i[2]) for i in right_side_3D]
	b4 = [int(i[0]) for i in top_3D]
	c4 = [int(i[1]) for i in top_3D]
	d4 = [int(i[2]) for i in top_3D]
	b5 = [int(i[0]) for i in bottom_3D]
	c5 = [int(i[1]) for i in bottom_3D]
	d5 = [int(i[2]) for i in bottom_3D]
	trace1 = Scatter3d(
	    x=b,
	    y=c,
	    z=d,
	    mode='markers',
	)
	trace2 = Scatter3d(
	    x=b1,
	    y=c1,
	    z=d1,
	    mode='markers',
	)
	trace3 = Scatter3d(
	    x=b2,
	    y=c2,
	    z=d2,
	    mode='markers',
	)
	trace4 = Scatter3d(
	    x=b3,
	    y=c3,
	    z=d3,
	    mode='markers',
	)
	trace5 = Scatter3d(
	    x=b4,
	    y=c4,
	    z=d4,
	    mode='markers',
	)
	trace6 = Scatter3d(
	    x=b5,
	    y=c5,
	    z=d5,
	    mode='markers',
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
	#plot_url = py.plot(fig, filename='simple-3d-scatter')

	return "front:",front_3D,"left:",left_side_3D,"back:",back_3D,"right:",right_side_3D,"top:",top_3D,"bottom:",bottom_3D

front_2D = [(0,0),(5,0),(5,5),(0,5)]
left_side_2D = [(0,0),(5,0),(5,5),(0,5)]
back_2D = [(0,0),(5,0),(5,5),(0,5)]
right_side_2D = [(0,0),(5,0),(5,5),(0,5)]
top_2D = [(0,0),(5,0),(5,5),(0,5)]
bottom_2D = [(0,0),(5,0),(5,5),(0,5)]
print two_D_three_D(front_2D,left_side_2D,back_2D,right_side_2D,top_2D,bottom_2D)