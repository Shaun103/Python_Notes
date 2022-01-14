#  ____________Table Contents______________

# json.load(f) - allows you to load JSON data from a file (file like objects)
# json.loads(s) - allows you to load JSON data from a string
# json.dump(j, f) - converts any type into JSON type
# json.dump(j, f) - writes JSON object to file (file-like object)
# json.dumps(j) - output JSON object as string
        
#_________________________________

# Reading from a file with json (json to python)
# Access the data with dictionary keys
# json created value (python to json)
# Writting to a file with JSON

# ____________Table Contents______________

path = '/Users/User/Desktop/Python/Python_Socratica/JSON/movie_1.txt'

import json

#________________________________________________

# print(dir(json)) # view the methods (dump, dumps & load, loads methods)

json_file = open(path, encoding="utf-8")
movie = json.load(json_file)
json_file.close()

# #________________________________________________

# # Reading from a file with json (json to python)

print("\n")
print(movie)  # # prints the entire file
json.dumps(movie, ensure_ascii=False) # # convert to valid json format, ensure non-ascii characters
print(type(movie))  # # python sees the JSON file as a dictionary

#_________________________________________________

# Access the data with dictionary keys

print(movie['title'])
print(movie['actors'])
print(movie['release_year'])

#_________________________________________________

# modifying and exporting to a new file 
# uses parts from previous movie object

movie['title'] = "The Powerpuff Girls"
movie['actors'] = ["The professor", "Blossom", "Bubbles", "Buttercup"]
print(movie)
path = '/Users/User/Desktop/Python/Python_Socratica/JSON/movie_3.txt' # saving as another file
file3 = open(path, 'w', encoding="utf-8")
json.dump(movie, file3, ensure_ascii=False, indent=5, separators=(',', ': '))

#_________________________________________________

# json created value (python to json)
# All characters are ascii

tron_movie = {}

value = """{
        "title": "Tron: Legacy",
        "composer": "Daft Punk", 
        "release_year": 2010,
        "budget": 170000000,
        "actors": null,
        "won_oscar": false,
        "**new column**": "************",
        "date": "09/10/2021"
        }"""

tron = json.loads(value) # parse through the information 
print(tron['title'])
tron['title'] = 'Tron: Legacy'
path = '/Users/User/Desktop/Python/Python_Socratica/JSON/tron_movie.txt'
file = open(path, 'w', encoding="utf-8")
json.dump(tron, file, ensure_ascii=False, indent=4, separators=(',', ': '))
file.close()
print('....JSON file created!')

#_________________________________________________

# Writting to a file with JSON

movie2 = {} # empty dictionary

movie2["title"] = "Minority Report"
movie2["director"] = "Steven Spielberg"
movie2["composer"] = "John Williams"
movie2["actors"] = ["Tom Cruise", "Colin Farrell", "Samantha Morton", "Max von Sydow"]
movie2["budget"] = 102000000
movie2["cinematographer"] = "Janusz Kami\u0144"

path = '/Users/User/Desktop/Python/Python_Socratica/JSON/movie_2.txt'

file2 = open(path, 'w', encoding="utf-8")

json.dump(movie2, file2, ensure_ascii=False, indent=4, separators=(',', ': '))

file2.close()

#_________________________________________________