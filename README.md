# Python-Tuples
Introduction to Python Tuples

Tuple: ()
List: []
Dictionary: {}


Tuple: immutable 
List: mutable

    post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# Tuple unpacking
title, sub_heading, content = post

# Equivalent to Tuple unpacking
    title = post[0]
    sub_heading = post[1]
    content = post[2]

#Results
    print(title)
    print(sub_heading)
    print(content)

# Adding new elements

    post += ('published',) # post = post + ('published',) 
    print(post)

# title, sub_heading, content, status = post

    print(title)
    print(sub_heading)
    print(content)
    print(status)

# id on a server
    print(id(post))

# List Nested in Tuples

post += (
    [
    'one: ["tuple_01", "tuple_02"]',
    'two: ["tuple_03", "tuple_04"]',
    ],
    [
    'three: ["tuple_05", "tuple_06"]',
    'four: ["tuple_07", "tuple_08"]',
    ]
)

print(post)

print(post[:2])

