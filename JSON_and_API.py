# Load JSON: json_data
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])
    
"""
Now it's your turn to pull some movie data down from the Open Movie Database (OMDB) using their API. 
The movie you'll query the API about is The Social Network. 
Recall that, in the video, to query the API about the movie Hackers, 
Hugo's query string was 'http://www.omdbapi.com/?t=hackers' and had a single argument t=hackers.

Note: recently, OMDB has changed their API: you now also have to specify an API key. 
This means you'll have to add another argument to the URL: apikey=72bc447a.
"""

# Import requests package
import requests

# Assign URL to variable: url. 
#/?
url = "http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network"

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])



Checking out the Wikipedia API

You're doing so well and having so much fun that we're going to throw one more API at you: 
the Wikipedia API (documented here). 
https://www.mediawiki.org/wiki/API:Main_page

You'll figure out how to find and extract information from the Wikipedia page for Pizza. 
What gets a bit wild here is that your query will return nested JSONs, that is, JSONs with JSONs, 
but Python can handle that because it will translate them into dictionaries within dictionaries.

The URL that requests the relevant query from the Wikipedia API is

https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza

# Import package
import requests

# Assign URL to variable: url
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)



