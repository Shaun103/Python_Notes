# # _____________________Table Contents________________________

# Background information: URL
# urllib module
# Helpful reading information
# Learning various used functions
# Error google scraping
# URLs socratica video

# # _____________________Table Contents________________________

# ____________________________________________________________

# # Background information: URL 

# URL: U = uniform, R = resource, L = locator

# At the beginning you have the protocol (scheme)
# Protocol: http, https, ftp, ....  
# Host: en.wikipedia.org    #
# Port: http=80, https=443  # 
# Path: wiki/url            # 
# Querystring: key=value&life=42
# Fragment: History # used to jump to a section in a web page

# ____________________________________________________________

# urllib module

# Request: open URLs
# Response: (used internally by the request module)
# Error: contains error classes, request exceptions
# Parse: breaking up a url into many  pieces
# Robotparser: used to inspect what permissions for bots and crawlers

# ____________________________________________________________

import urllib
from urllib import request
from urllib import parse

# ____________________________________________________________

# # Helpful reading information

# print(dir(urllib))      # displays information 
# print(dir(request))     # focus on 'urlopen'

# ____________________________________________________________

# # Learning various used functions

resp = request.urlopen("https://wikipedia.org")

# print(type(resp))      # class type    

# print(dir(resp))       # displays all of the methods 

# print(resp.code)       # 200 code: ok - checks to see if connection is made

# print(resp.length)     # How large the response may be

# print(resp.peek())     # small look at the response(html), b' = bytes (binary) file 

# data = resp.read()       
# print(data)
# print(type(data))       

# print(len(data))        

# html = data.decode('utf-8')     # converts to a string type
# print(type(html))

# print(html)                     # prints the entire html page 

#________________________________________
# # Error google scraping
# # Error message, google wants to keep their information from being scraped

# resp = request.urlopen("https://www.google.com/search?q=socratica")

#________________________________________
# URLs socratica video 

# # https://www.youtube.com/watch?v=EuC-yVzHhMI&t=5m56s

qs = "v=" + "EuC-yVzHhMI" + "&" + "t=" + "5m56s"        # (ineeficient way) appending a video string 

# print(dir(parse))           # functions working with URLs (urlencode)

params = {"v": "EuC-yCzHhMI", "t": "5m56s"}
querystring = parse.urlencode(params)

url = "https://www.youtube.com/watch" + "?" + querystring       # building the url 

resp = request.urlopen(url)
print(resp.isclosed())      # False = still connected to the server
print(resp.code)            # code 200 = still good connection 

html = resp.read().decode("utf-8")   # read and decode server response
print(html[:500])                    # reads the first 500 characters