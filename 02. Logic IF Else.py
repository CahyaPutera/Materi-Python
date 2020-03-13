# Comparison Operators

# x = 5
# y = '5'
# print(x == y) # y = string
# print(x > int(y))
# print(x >= int(y))
# print(x < int(y))
# print(x <= int(y))

# Logical Operators

# x = 5
# y = '5'
# z = 6
# print(x==int(y) and int(y)<z)
# print(x==int(y) or int(y)<z)
# print(not(x==int(y) or int(y)<z))

# If, else, If else

# nilai = int(input('masukkan nilai : '))
# if (nilai > 80) :
#    print('Excellent!')
# elif (nilai >= 60 and nilai <= 80) :
#    print('Good job!')
# else :
#     print("Don't give up!")

# Latihan 1

# angka = int(input("masukkan angka : "))
# if (angka % 2) == 0:
#    print("Angka {} tergolong Genap" .format(angka))
# else:
#    print("Angka {} tergolong Ganjil" .format(angka))

#  Latihan 2

# massa = float(input('masukkan massa : '))
# tinggi = float(input('masukkan tinggi : ')) / 100

# IMT = massa / (tinggi**2)

# if IMT < 18.5 :
#    k = ('Berat Badan Kurang')
# elif IMT >= 18.5 and IMT <= 24.9 :
#    k = ('Berat Badan Ideal')
# elif IMT >= 25.0 and IMT <= 29.9 :
#    k = ('Berat Badan Berlebih')
# elif IMT >= 30.0 and IMT <= 39.9 :
#    k = ('Berat Badan Sangat Berlebih')
# else : 
#    k = ('Obesitas')

# print ('Massa {} kg & Tinggi {} m' .format(massa, tinggi))
# print ('IMT = {}, {}' .format(IMT, k))
