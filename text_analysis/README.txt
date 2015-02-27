My book analysis code is in the text_analysis.py code, and the instructions to get the various graphs are as follows:
1. Get the top 30 words frequently mentioned in the text:
  In function book_analysis, on line 206, uncomment the function call on line 247, and ensure all the other function calls around 
  it are commented out. The function will open the lines of a text file and remove punctuation and capitalization as needed.
  The function call line will call plot_frequency, the function on line 32. This function calls another function, top_words found 
  on line 13, which iterates through a dictionary to find the 30 most common words. Returning to plot_frequency, the data found 
  through top_words will then be plotted. 
2. See the number of mentions for each character:
  In function book_analysis, on line 206, uncomment the function call on line 245, and ensure all the other function calls around 
  it are commented out. The function will open the lines of a text file, remove punctuation and capitalization as needed, and 
  find the number of mentions for each character and place. The function call line will call plot_frequency, the function on line 32. This function calls another function, top_words found 
  on line 13, which iterates through a dictionary to find the 30 most frequently mentioned characters. Returning to 
  plot_frequency, the data found through top_words will then be plotted. 
3. See the number of mentions for each place: 
  In function book_analysis, on line 206, uncomment the function call on line 246, and ensure all the other function calls around 
  it are commented out. The function will open the lines of a text file, remove punctuation and capitalization as needed, and 
  find the number of mentions for each character and place. The function call line will call plot_frequency, the function on line 32. This function calls another function, top_words found 
  on line 13, which iterates through a dictionary to find the 30 most frequently mentioned places. Returning to 
  plot_frequency, the data found through top_words will then be plotted. 
4. Run sentiment analysis by chapter:
  In function book_analysis, on line 206, uncomment the function call on line 248, and ensure all the other function calls around 
  it are commented out. The function will open the lines of a text file, remove punctuation and capitalization as needed, and 
  find the number of mentions for each character and place. The function call line will call line_sentiment, found on line 79.
  This function will find the sentiment of each line and sort the values into separate dictionaries. Next, each line sentiment
  will be sorted into the relating chapter. To graph sentiment by chapter, comment out line 129 and uncomment line 130. This
  will call sentiment_by_lines, found on line 132. This plots the chapter-sentiment data.
5. Run sentiment analysis by line: 
  In function book_analysis, on line 206, uncomment the function call on line 248, and ensure all the other function calls around 
  it are commented out. The function will open the lines of a text file, remove punctuation and capitalization as needed, and 
  find the number of mentions for each character and place. The function call line will call line_sentiment, found on line 79.
  This function will find the sentiment of each line and sort the values into separate dictionaries. Next, each line sentiment
  will be sorted into the relating chapter. To graph sentiment by line, comment out line 130 and uncomment line 129. This
  will call sentiment_by_lines, found on line 132. This plots the line-sentiment data.

NOTE: If you do not have plot.ly or an account, the graphing code will most likely show an error. The graphs produced are found
in the GameOfThronesGraphs folder that is also in this repo. 
