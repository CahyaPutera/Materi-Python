# # Dictionary

# d = { "key1" : "item1", "key2" : "item2", "kucing" : [3, "jerapah"] }
# print(d["key1"])
# print(d["key2"])
# print(d["kucing"])
# print(d["kucing"][1])

# # Dictionary inside dictionary

# d = { "key1" : { "key2" : "item2" }, "kucing" : [3, "jerapah"] }
# print(d["key1"])
# print(d["key1"]["key2"])
# print(d["kucing"])
# print(d["kucing"][1])

# # Tuples (tipe data seperti list tapi setelah di inisiasi isinya tidak bisa di rubah)

# t = (1, [0, "test"], { "a1" : True })
# print(t[2]["a1"])
# print(t[1][1])
# t[1][1] = "akan"
# print(t[1][1])
# t[1] = "mark"
# print(t[1])

# # Tuples inside tuples

# t = (1, [0, "test"], { "a1" : True }, (0,{ "test" : 5 },2))
# print(t[3][1]["test"])

# # Sets (object yang menjadikan isi di dalamnya unique items)

# s = { 1, 3, 1, 2, 2, 3, 'a', 'a', True, True, False, 'b', 1.4, 1.4 } #False dianggap 0, True dianggap 1
# print(s)
# print(list(s)[2]) #bisa di indexing asal di rubah jadi list dulu

# # List comprehension 

# listNum = [ 1, 2, 3, 4, 5]
# listNum = [item * 2 for item in listNum]
# print(listNum)

# # List comprehension 2

# def times2(num) :
#     return num * 2
# listNum = [ 1, 2, 3, 4, 5]
# listNum = [times2(item) for item in listNum]
# print(listNum)

# # Lambda expression (fungsi yang hanya bisa di pakai 1x penggunaan)

# def times2(num) :
#     return num * 2
# lambda num: num * 2

# # map Function (fungsi untuk mapping fungsi yang di masukkan dalam map ke setiap value yang iterable)

# # Tanpa lambda

# def times2(num) :
#     return num * 2
# listNum = [ 1, 2, 3, 4, 5]
# listNum = list(map(times2, listNum))
# print(listNum)

# # Dengan lambda

# listNum = [ 1, 2, 3, 4, 5];
# listNum = list(map(lambda z: z * 2 if z < 3 else z/2, listNum)); #z = iterable 
# print(listNum);

# filter Function (fungsi untuk mereturn data yang True)

# Tanpa lambda

# def genap(num) :
#     return num % 2 == 0
# listNum = [ 1, 2, 3, 4, 5]
# listNum = list(filter(genap, listNum))
# print(listNum)

# Dengan lambda

# listNum = [ 1, 2, 3, 4, 5]
# listNum = list(filter(lambda num: num % 2 == 0, listNum))
# print(listNum)

# listNum = 'ini string'
# listNum = list(filter(lambda num : num == 'i', listNum))
# print(listNum)
