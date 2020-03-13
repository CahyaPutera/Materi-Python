# # Search (hasil keluar dlm list)

import re

# months = ['February', 'March', 'April', 'May', 'June']

# for month in months :
#     if re.search (r'a', month): #outputnya True or False
#         print(month)

# Metacharacter (pola char dimana dia menggambarkan char lain)

# # fungsi ^ (mencari char yang diawali (^))

# hello_list = ['hello', 'world', 'hello world', 'helloworld', '1helloworld']
# for word in hello_list:
#     if re.search(r'^hello', word):
#         print(word)

# # fungsi $ (mencari char yang akhiri ($))

# hello_list = ['hello', 'world', 'hello world', 'helloworld', '1helloworld']
# for word in hello_list:
#     if re.search(r'world$', word):
#         print(word)

# # fungsi * (mencari char yang sebelum dan sesudah tanda (*))

# cat_list = ['ct', 'cat', 'caat', 'caaaat', 'cabt']
# for word in cat_list:
#     if re.search(r'ca*t', word):
#         print(word)

# # fungsi + (mencari char yang sebelum dan sesudah tanda (+) kondisi minimal char 1 kali)

# cat_list = ['ct', 'cat', 'caat', 'caaaat', 'cabt']
# for word in cat_list:
#     if re.search(r'ca+t', word):
#         print(word)


# # fungsi ? (mencari char yang sebelum dan sesudah tanda (?) kondisi minimal char 1 atau 0 kali)

# dash_list = ['dashboard', 'dash-board', 'dash--board']
# for item in dash_list:
#     if re.search(r'dash-?board', item):
#         print(item)

# #fungsi {n,m} (mencari char yang sebelum dan sesudah tanda ({n,m}}) sebanyak n, atau m kali)
# ab_list = {'ab', 'aob', 'aoob', 'aooob', 'aoooob'}
# for item in ab_list:
#     if re.search(r'ao{1,3}b', item):
#         print(item)

# # Sets (special char yang digunakan untuk matching string apapun di dlm [])
# # Findall (hasil keluar dlm string)

# string = 'February March April May June 123'
# match = re.findall(r'[a-zA-Z]+', string) # di tambahkan (+) keluarnya per huruf, (*) keluar spasi kosong
# print(match)

# # fungsi ^ (inverse)

# string = 'February March April May June 123'
# match = re.findall(r'[^a-zA-Z]+', string) # di tambahkan (+) keluarnya per huruf, (*) keluar spasi kosong
# print(match)

# # Special sequences (special char yang punya arti special, selalu dimulai dgn (\) dan di ikuti dgn char)
# Word Boundary 

# string = 'February March April May June'
# match = re.findall(r'M[a-zA-Z]+', string)
# print(match)

# float 

# word = 'I want to eat rice 100.11 and 1012.445'
# print(re.findall(r'[a-zA-Z]+|\d+\.\d+', word))
