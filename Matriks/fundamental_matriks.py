# Array => jenis struktur data 1 dimensi yang menyimpan data secara linier
# Matriks =>  kumpulan data yang diatur dalam bentuk tabel dua dimensi dengan setiap elemennya terdefinisi berdasarkan baris dan kolom.

# Membuat matriks
# matriks = [[1, 2, 3], 
#            [4, 5, 6], 
#            [7, 8, 9]]

# print(matriks)

# Membuat matriks menggunakan library numpy
import numpy

# matriks_numpy = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(matriks_numpy)

# Membandingkan ukuran memory yang digunakan matriks python dan matriks numpy
import sys

var_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_array = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Ukuran keseluruhan elemen list dalam bytes = ",sys.getsizeof(var_list)*len((var_list)))
print("Ukuran keseluruhan elemen NumPy dalam bytes = ",var_array.size*var_array.itemsize)