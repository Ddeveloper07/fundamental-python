# Mendeklarasikan array dengan list
var_list = [1,2,3]
# Mencari lokasi memori setiap elemen di atas
for elemen in var_list:
    print(id(elemen))

# Mendefinisikan isi array
var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr)

# Mendefinisikan nilai default
var_arr_default = [0 for i in range(10)]

# Mengubah nilai default
for i in range(10):
    var_arr_default[i] = i

print(var_arr_default)

# Mengakses elemen array
print(var_arr_default[4])