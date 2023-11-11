# Deklarasi Matriks

# 1. Deklarasi sekaligus inisialisasi nilai matriks
matriks = [[1, 0, 1, 0, 1],
           [0, 1, 0, 1, 0],
           [1, 0, 1, 0, 1]]

print(matriks)

# 2. Deklarasi dengan menggunakan nilai default
matriks_default = [[0 for j in range(4)] for i in range(3)]

print(matriks_default)

# Akses Elemen Matriks
var_mat = [[1, 2, 3, 4, 5], 
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]

print(var_mat[0][0])