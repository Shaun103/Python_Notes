# ______________Table Contents______________

# Dictionaries
# Adding to a dictionary 
# finding out data is not in a dictionary
# Iterating through a dictionary 
# popitems
# copy method
# pop - method 
# fromkeys method
# Update method
# ______________Table Contents______________

# Dictionaries

user_id = 209
message = 'D5 E5 C5 C4 G4'
language = 'English'
datetime = "20230215T124231Z"
location = (44.5900533, -104.715556)

post = {
    "user_id": 209, 
    "message": "D5 E5 C5 C4 G4", 
    "language": "English", 
    "datetime": "20230215T124231Z", 
    "location": (44.5900533, -104.715556)
}

# inputs - "Keys"
# outputs - "Values"

# print(type(post))

# #___________________________________________

# # Adding to a dictionary 

# post2 = dict(message = "SS Cotopaxi", language = "English")
# print(post2)

# post2['user_id'] = 209
# post2["datetime"] = "19771116T093001Z"
# print(post2)

# #___________________________________________

# # finding out data is not in a dictionary 

# print(post['message'])
# # # print(post2['location'])  ## will give you an error, "location" is not in post2

# #___________________________________________

# # # Option 1

# if 'location' in post2:
#     print(post2['location'])
# else:
#     print("The post does not contain a location value.")

# #___________________________________________

# # # Option 2

# try:
#     print(post2['location'])
# except KeyError:
#     print("The post does not have a location.")

# #___________________________________________

# # # Option 3

# print(dir(post2))
# print(help(post2.get))

# loc = post2.get('location', None)
# print(loc)


# #___________________________________________

# # Iterating through a dictionary 

# for key in post.keys():
#     value = post[key]
#     print(key, '=', value)

# for key, value in post.items():
#     print(key, '=', value)

#___________________________________________

# pop - removes desired item

# print(dir(post))
# print(help(post.pop))

# print(dir(post))
# print(help(post.pop))   

# post.pop('message')
# print('Poped items: ')
# for key, value in post.items():
#     print(key, '=', value)

#___________________________________________

# popitems()  - captures last item
# print(dir(post))

# print(help(post.popitem))
# print(post.popitem())

#___________________________________________ 

# # copy method - Makes a shallow copy of a dictionary 

# print(dir(post))
# print(help(post.copy)) 

# x = post.copy()

# print(x)
# x.pop('message')
# print(x)

#___________________________________________

# fromkeys - Create a new dictionary with keys from iterable and values set to value.

# print(dir(post))
# print(help(post.fromkeys)) 

# x = ('key1', 'key2', 'key3')
# y = 1, 2, 3, 4

# myPost = {}

# x = myPost.fromkeys(x, 1)
# print(x)

#___________________________________________

# # Update method - adds on to existing dictionary  

# print(dir(post))
# print(help(post.update))

# x.update({
#         "color": "Red",
#         "type": "None",
#         "size": "large",
#         "cost": "expensive"
#         })

# for values, keys in x.items():
#     print(values, keys)


#___________________________________________

# # clear - removes all items from dictionary 

# print(help(post.clear))

# post.clear()
# print(post)

#___________________________________________