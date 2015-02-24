""" SHIVALI CHANDRA
	FEBRUARY 22, 2015
	This is a program that opens a novel as a text file and can analyze it in multiple ways, including sentiment analysis and word frequency.
"""

import plotly.plotly as py
from plotly.graph_objs import *
from pattern.en import *
import re

def top_words(v,k,num):
	nd = {}
	for i in range(0,num):
		key = k[v.index(max(v))]
		val = max(v)
		nd[key] = val
		k.remove(key)
		v.remove(val)
	return nd

def word_frequency(dictionary,name):
	v=list(dictionary.values())
	k=list(dictionary.keys())
	kv = top_words(v,k,30)
	x = kv.keys()
	y = kv.values()
	data = Data([
	    Bar(
	        x=x,
	        y=y
	    )
	])
	plot_url = py.plot(data, filename=name)

def line_sentiment(alllines,chapters,filename):
	very_happy = []
	happy = []
	neutral = []
	neg = []
	very_neg = []
	vh_pg = []
	h_pg = []
	n_pg = []
	neg_pg = []
	vn_pg = []
	for i in range(0,len(chapters)-1):
		page_ranges = ''.join(alllines[chapters[i]:chapters[i+1]])
		sent = sentiment(page_ranges)[0]
		if sent >= .5:
			very_happy.append(sent)
			vh_pg.append(i)
		elif (sent > 0) and (sent < .5):
			happy.append(sent)
			h_pg.append(i)
		elif sent == 0:
			neutral.append(sent)
			n_pg.append(i)
		elif (sent < 0) and (sent >= -0.5):
			neg.append(sent)
			neg_pg.append(i)
		else:
			very_neg.append(sent)
			vn_pg.append(i)

	trace1 = Bar(
	    x=vh_pg,
	    y=very_happy,
	    name='Very Positive',
	    marker=Marker(
	        color='rgb(255,1,1)' 
	        )
	    )
	trace2 = Bar(
	    x=h_pg,
	    y=happy,
	    name='Positive',
	    marker=Marker(
	        color='rgb(255,146,1)'
	    )
	)
	trace3 = Bar(
	    x=n_pg,
	    y=neutral,
	    name='Neutral',
	    marker=Marker(
	        color='rgb(255,235,1)'
	    )
	)
	trace4 = Bar(
	    x=neg_pg,
	    y=neg,
	    name='Negative',
	    marker=Marker(
	        color='rgb(1,226,34)'
	    )
	)
	trace5 = Bar(
	    x=vn_pg,
	    y=very_neg,
	    name='Very Negative',
	    marker=Marker(
	        color='rgb(1,255,255)'
	    )
	)
	data = Data([trace1,trace2,trace3,trace4,trace5])
	layout = Layout(
	    title='Sentiment Analysis of A Game Of Thrones',
	    xaxis=XAxis(
	        title='Chapter',
	        titlefont=Font(
	            size=16,
	            color='rgb(107, 107, 107)'
	        ),
	        tickfont=Font(
	            size=14,
	            color='rgb(107, 107, 107)'
	        )
	    ),
	    yaxis=YAxis(
	        title='Value of Sentiment',
	        titlefont=Font(
	            size=16,
	            color='rgb(107, 107, 107)'
	        ),
	        tickfont=Font(
	            size=14,
	            color='rgb(107, 107, 107)'
	        )
	    ),
	    barmode='stack',
	    bargap=0.15,
	    bargroupgap=0.1
	)
	fig = Figure(data=data, layout=layout)
	plot_url = py.plot(fig, filename=filename)

def book_analysis(filename):
	lines = open(filename).readlines() 
	d = dict()
	count = 0
	chapters = []
  	for line in range(0,len(lines)):
  		if (lines[line] in ['\n','\r\n']):
  			count+=1
  			if count > 4: 
  				chapters.append(line)
  		else:
  			count = 0
  		words = lines[line].split()
  		for word in words:
  			punctuation = re.compile(r'[.?!,":;]') 
  			word = punctuation.sub('', word)
  			word = word.lower()
			d[word] = d.get(word,0)+1
	#word_frequency(d,filename)
	line_sentiment(lines,chapters,filename)
	
print book_analysis('AGameOfThrones1.txt')

