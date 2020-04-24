
# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Prettify the BeautifulSoup object: pretty_soup
pretty_soup = soup.prettify()

# Print the response
print(pretty_soup)


##Turning a webpage into data using BeautifulSoup: getting the text

# Get the title of Guido's webpage: guido_title
guido_title = soup.title

# Print the title of Guido's webpage to the shell
print(guido_title)

# Get Guido's text: guido_text
guido_text = soup.get_text()

# Print Guido's text to the shell
print(guido_text)


# Turning a webpage into data using BeautifulSoup: getting the hyperlinks

# Find all 'a' tags (which define hyperlinks): a_tags
# Use the method find_all() to find all hyperlinks in soup, remembering that hyperlinks are defined by the HTML tag <a> but passed to find_all() without angle brackets; store the result in the variable a_tags.
a_tags = soup.find_all('a')
   
# Print the URLs to the shell
for link in a_tags:
    print(link.get('href'))


      
"""
A little bit of Twitter text analysis

Now that you have your DataFrame of tweets set up, you're going to do a bit of text analysis to count how many tweets contain the words 
'clinton', 'trump', 'sanders' and 'cruz'. 
In the pre-exercise code, we have defined the following function word_in_text(), 
which will tell you whether the first argument (a word) occurs within the 2nd argument (a tweet).

import re

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)

    if match:
        return True
    return False
You're going to iterate over the rows of the DataFrame and calculate how many tweets contain each of our keywords! 
The list of objects for each candidate has been initialized to 0.
"""

# Initialize list to store tweet counts
[clinton, trump, sanders, cruz] = [0, 0, 0, 0]

# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])


"""
Plotting your Twitter data

Now that you have the number of tweets that each candidate was mentioned in, you can plot a bar chart of this data. 
You'll use the statistical data visualization library seaborn, which you may not have seen before, but we'll guide you through. 
You'll first import seaborn as sns. You'll then construct a barplot of the data using sns.barplot, passing it two arguments:

a list of labels and
a list containing the variables you wish to plot (clinton, trump and so on.)
"""
# Import packages
import seaborn as sns
import matplotlib.pyplot as plt

# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz']

# Plot the bar chart
# Complete the arguments of sns.barplot:
#The first argument should be the list of labels to appear on the x-axis (created in the previous step).
#The second argument should be a list of the variables you wish to plot, as produced in the previous exercise 
#(i.e. a list containing clinton, trump, etc).

ax = sns.barplot(cd, [clinton, trump, sanders, cruz])
ax.set(ylabel="count")
plt.show()

   
