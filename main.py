# Tuple: ()
# List: []
# Dictionary: {}


# Tuple: immutable 
# List: mutable

post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# Tuple unpacking
title, sub_heading, content = post

# Equivalent to Tuple unpacking
# title = post[0]
# sub_heading = post[1]
# content = post[2]

print(title)
print(sub_heading)
print(content)

# Adding new elements

post += ('published',) # post = post + ('published',) 

print(post)

title, sub_heading, content, status = post

print(title)
print(sub_heading)
print(content)
print(status)

# id on a server
print(id(post))




