############################
# contoh = [i for i in range (5)]
# print (contoh)

#################

#sama dengan di bawah untuk looping list
# for i in range (5):
#     for  i in range (2):
#         i*j

# contoh = [i*j for i in range (5) for j in range(2)]
# print (contoh)

# ############################### list comprehension
# contoh = [str(i*j) if i < 3 or i == 4 else i+j for i in range(5) for j in range (2)]
# print (contoh)

# buah = ['Jeruk', 'Nanas', 'Apel', 'Mangga', 'Pir', 'Kiwi', 'Semangka']
# # ###### jika jumlah di dalam integer lebih dari 4 maka print huruf 1 dan 2  dar 
# tugas_buah = [ i[:2] if len(i)>4 else 'buah lain' for i in buah]
# print (tugas_buah) 
