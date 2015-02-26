""" SHIVALI CHANDRA
	FEBRUARY 22, 2015
	This is a program that opens a novel as a text file and can analyze it in multiple ways, including sentiment analysis 
	and word frequency. I got the basic framework for graphing my results from plot.ly, but the code written is my own work. 
"""

import plotly.plotly as py
from plotly.graph_objs import *
from pattern.en import *
import re

def top_words(dictionary,num):
	"""This function takes a dictionary and a number, and locates the most frequency words, 
	the amount of which is specified through the inputted number"""
	#breaks dictionary into lists of values and keys
	v=list(dictionary.values())
	k=list(dictionary.keys())
	new_dict = {}
	#loops through to find inputted number of frequent words
	if len(dictionary) < num:
		num = len(dictionary)
	for i in range(0,num):
		key = k[v.index(max(v))]
		val = max(v)
		new_dict[key] = val
		#removes the word from dictionary to find next highest word count
		k.remove(key)
		v.remove(val)
	return new_dict
import csv

def plot_frequency(dictionary,name):
	"""This function uses top_words to find the 30 highest words, then plots the words and their word count"""
	freq_words = top_words(dictionary,30)
	x = freq_words.keys()
	y = freq_words.values()
	#used the following code to write the dictionary to a file to create bubble plots online
	w = csv.writer(open("output2.csv", "w"))
	for key, val in freq_words.items():
   		w.writerow([key, val])
   	#code to plot bargraphs 
	data = Data([
	    Bar(
	        x=x,
	        y=y
	    )
	])
	plot_url = py.plot(data, filename=name)

def line_sentiment(alllines,chapter_begins,filename):
	"""This function determines the sentiment of each line in a text file, and places the lines and their sentiment number into
	various dictionaries in order to then plot the sentiment ranges in different colors."""
	lines_chapters = {}
	for i in range(0,len(chapter_begins)-1):
		start = chapter_begins[i]
		end = chapter_begins[i+1]
		while start < end:
			lines_chapters[start] = i+1 
			start+=1
	very_happy = {}
	happy = {}
	neutral = {}
	neg = {}
	very_neg = {}
	new_v_h = {}		
	new_h = {}
	new_n = {}
	new_neg = {}
	new_v_neg = {}
	for i,n in enumerate(alllines):
		sent = sentiment(n)[0]
		if sent >= .5:
			very_happy[i] = sent
		elif (sent > 0) and (sent < .5):
			happy[i] = sent
		elif sent == 0:
			neutral[i] = sent
		elif (sent < 0) and (sent >= -0.5):
			neg[i] = sent
		else:
			very_neg[i] = sent
	for i in lines_chapters.keys():
		c = lines_chapters.get(i)
		if i in very_happy.keys():
			new_v_h[c] = new_v_h.get(c,0)+1 
		if i in happy.keys():
			new_h[c] = new_h.get(c,0)+1
		if i in neutral.keys():
			new_n[c] = new_n.get(c,0)+1
		if i in neg.keys():
			new_neg[c] = new_neg.get(c,0)+1
		if i in very_neg.keys():
			new_v_neg[c] = new_v_neg.get(c,0)+1
	#sentiment_by_lines(very_happy,happy,neutral,neg,very_neg,filename)
	sentiment_by_lines(new_v_h,new_h,new_n,new_neg,new_v_neg,filename)

def sentiment_by_lines(range1,range2,range3,range4,range5,filename):
	"""This function takes 5 dictionaries and a filename in order to graph a bar graph of line number vs. sentiment"""
	trace5 = Bar(
	    x=range1.keys(),
	    y=range1.values(),
	    name='Very Positive',
	    marker=Marker(
	        color='rgb(255,1,1)' 
	        )
	    )
	trace4 = Bar(
	    x=range2.keys(),
	    y=range2.values(),
	    name='Positive',
	    marker=Marker(
	        color='rgb(255,146,1)'
	    )
	)
	trace3 = Bar(
	    x=range3.keys(),
	    y=range3.values(),
	    name='Neutral',
	    marker=Marker(
	        color='rgb(255,235,1)'
	    )
	)
	trace2 = Bar(
	    x=range4.keys(),
	    y=range4.values(),
	    name='Negative',
	    marker=Marker(
	        color='rgb(1,226,34)'
	    )
	)
	trace1 = Bar(
	    x=range5.keys(),
	    y=range5.values(),
	    name='Very Negative',
	    marker=Marker(
	        color='rgb(1,255,255)'
	    )
	)
	data = Data([trace1,trace2,trace3,trace4,trace5])
	layout = Layout(
		autosize=False,
    	width=2500,
    	height=700,
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
	"""This is the main, overarching function which opens a text file and gets every line from it. For the use of other
	functions, this function separates lines into chapters and removes punctuation and uppercase formats in order to count the
	frequency of words."""
	#open file, create dictionary and list of chapters 
	lines = open(filename).readlines() 
	word_count = {}
	name_count = {}
	place_count = {}
	count = 0 
	chapters = []
	names = ['Rickard','Lyarra','Brandon','Catelyn','Tully','Eddard','Ned','Lyanna','Benjen','Robb','Jeyne','Sansa','Arya','Bran','Rickon','Jon','Snow','Stark','Roose','Bolton','Ramsay','Hodor','Osha','Poole','Jojen','Meera','Reed','Maeker','Daeron','Aerion','Maester','Aemon','Aegon','Rhae','Daella','Duncan','Rhalle','Aerys','Rhaella','Elia','Martell','Rhaegar','Viserys','Drogo','Daenerys','Aegon','Rhaego','Targaryen','Arryn','Lysa','Robert','Jon Arryn','Lannister','Tywin','Cersei','Jaime','Joffrey','Baratheon','Myrcella','Tommen','Tyrion','Kevan','Lancel','Bronn','Gregor','Clegane','Sandor','Podrick','Pod','Steffon','Stannis','Selyse','Renly','Margaery','Tyrell','Mya','Gendry','Edric','Shireen','Stone','Melisandre','Davos','Seaworth','Brienne','Beric','Dondarrion','Greyjoy','Balon','Theon','Asha','Euron','Victarion','Aeron','Doran','Arianne','Quentyn','Trystane','Obara','Oberyn','Nymeria','Tyene','Sarella','Ellaria','Areo','Hotah','Petyr','Baelish','Edmure','Roslin','Brynden','Walder','Loras','Mace','Olenna','Jeor','Mormont','Yoren','Samwell','Sam','Tarly','Janos','Slynt','Alliser','Thorne','Mance','Rayder','Ygritte','Val','Bowen','Varys','Pycelle','Barristan','Selmy','Arys','Oakheart','Ilyn','Payne','Qyburn','Khal','Syrio','Forel','Jaqen','H"ghar','Illyrio','Mopatis','Thoros','Duncan','Ser']
  	places = ['Westeros','Essos','Braavos','Vaes Dothrak','White Harbor','Lys','The North','Duskendale','Black Bay','Lhazosh','Iron Islands','Vale','Westerlands','Stormlands','The Reach','Dorne','Seven Kingdoms','Qohor','Slaver"s Bay','Shivering Sea','Summer Sea','Valyria','Astapor','Yunkai','Meereen','Sothoros','The Neck','Winterfell','The Wall','Beyond the Wall','Iron Islands','Pyke','Great Wyk','Old Wyk','Harlaw','Saltcliffe','Blacktyde','Orkmont','Riverlands','Trident','Harrenhal','Riverrun','Tumblestone River','Red Fork','The Twins','Eyrie','Bloody Gates','Alyssa"s Tears','Casterly Rock','Lannisport','Highgarden','Oldtown','Citadel','Hightower','Storm"s End','Crownlands','Dragonstone','King"s Landing','Red Keep','Iron Throne','Sunspear','Free Cities','Lys','Myr','Pentos','Lorath','Norvos','Volantis','Tyrosh','Dothraki Sea','Rhoyne','Lhazar','Red Waste','Qarth','Worm River','Plaza of Pride','Asshai','Shadow Lands','Ibben','Summer Islands','Yi Ti']
  	for line in range(0,len(lines)):
  		if (lines[line] in ['\n','\r\n']):
  			count+=1
  			if count > 4: 
  				chapters.append(line)
  				count = 0
  		else:
  			count = 0
  		words = lines[line].split()
  		for word in words:
  			punctuation = re.compile(r'[.?!,":;-]') 
  			word = punctuation.sub('', word)
  			if word not in names+places:
				word = word.lower()
			word_count[word] = word_count.get(word,0)+1
	for i in names:
		if i in words:
			name_count[i] = name_count.get(i,0)+1
	for j in places:
		if j in words:
			place_count[j] = place_count.get(j,0)+1
	#plot_frequency(name_count,filename)
	#plot_frequency(place_count,filename)
	#plot_frequency(word_count,filename)
	line_sentiment(lines,chapters,filename)
	
print book_analysis('AGameOfThrones1.txt')

