# While Loop

angka = 1
while(angka <= 10): # kondisi while artinya selama kondisi blm terpenuhi, maka...
   print(angka)
   angka += 1

# For Loop 

listItem = list(range(1,11,2)) # format range  (start, stop, stack)
print(listItem)
for item in range(1,11,2): # item pertama kali = 1 pada saat loop pertama
	print(item)

# For Loop Drawing

z=''
for item in range(0,5):
   z += ' * '
print(z) # z = z + '*'

# Loop Drawing 2

z=''
for item in range(0,5):
   z += ' * \n' 
print(z) # \n = enter (turun ke bawah) 

# Loop In Loop 

z=''
for item in range(5): #item isinya mulai dari = 0
   for item1 in range(5):
      z += '*'
   z += '\n'
print(z)

# Loop In Loop 2

z=''
for item in range(5):
   for item1 in range(0, item+1):
      z += '*'
   z += '\n'
print(z)

# Loop Statement Break (statement yang hanya muncul dalam loop(baik di while, maupun for in))

print('Contoh Break')
for i in range(10) : 
   if i == 5 :
      break
   else : 
      print(i)

# Loop Statement Pass (menjalankan di bawahnya)

a = list(range(0,3))

print("contoh pass")
for item in a :
   if not item :
      pass
   else : 
      print(item *2)
   print(item)

# Loop Statement Continue (menjalankan di bawahnya kembali ke awal)

a = list(range(0,3))

print("contoh continue")
for item in a :
   if not item :
      continue
   else : 
      print(item *2)
   print(item)