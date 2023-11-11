# Operasi 1 matriks
# Menghitung total semua elemen matriks.
# Mengalikan elemen matriks dengan konstanta.
# Transpose matriks.
# Inverse matriks.
# Menentukan determinan, dan sebagainya.

# Operasi 2 matriks:
# Menambahkan dua matriks.
# Mengalikan dua matriks.
# Pembagian dua matriks, dan sebagainya.

# 1. Mengalikan elemen matriks dengan konstanta
var_mat = [[5, 0],
           [1, -2]]

def_mat = [[0 for j in range(2)] for i in range(2)]

# kita akan melakukan perulangan berdasarkan dua kondisi. Kondisi pertama adalah perulangan berdasarkan banyaknya list di dalam matriks ([5, 0], [1, -2]) yang merepresentasikan baris. Kondisi kedua adalah perulangan berdasarkan banyaknya elemen pada setiap list (5,0 dan 1,-2).
for i in range(len(var_mat)):
    for j in range(len(var_mat[0])):
        def_mat[i][j] = var_mat[i][j] * 2

print(def_mat)

# Menggunakan library numpy
import numpy as np
var_mat_np = np.array([[5,0], 
                      [1, -2]])

result = var_mat_np * 2

print(result)