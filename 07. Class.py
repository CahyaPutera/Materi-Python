# Class 
# (membuat 'blueprint' artinya object yang di masukkan ke dalam class akan memiliki properties yang sama)

# class classy : 
#     my_class = 5

# contoh = classy()
# print(contoh.my_class)

# Init function (digunakan dalam class untuk assign property dari luar ke dalam class)

# class Manusia :
#     def __init__(self, name, age) :
#         self.nama = name 
#         self.umur = age

# cornell = Manusia('cornell', 27)
# print(cornell)
# print(cornell.nama)
# # print(cornell.umur)
# cornell.umur = 35
# print(cornell.umur)
# cornell.job = 'data scientist'
# print(cornell.__dict__)
# print(cornell.__dict__['nama'])

# Object method

class Manusia :
    def __init__(self, nama, umur) : #Fungsi class untuk pertama menggunakan 'self'
        self.name = nama 
        self.age = umur
    
    def salamkenal(self) :
        print('nama saya adalah {} dan saya berumur {} tahun'.format(self.name, self.age))

# cornell = Manusia('cornell', 27)
# print(cornell)
# print(cornell.name)
# # print(cornell.umur)
# cornell.umur = 35
# print(cornell.age)
# cornell.job = 'data scientist'
# print(cornell.__dict__)
# print(cornell.__dict__['name'])
# cornell.salamkenal()

# Inheritance

class Anak(Manusia):
    pass

anak1 = Anak('Cornellius', 27)
anak1.salamkenal()

# Super (mewarisi semua method & properties)

class anak(Manusia):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.kelamin = gender

Nel = anak('Nel', 21, 'Male')
Nel.salamkenal()
