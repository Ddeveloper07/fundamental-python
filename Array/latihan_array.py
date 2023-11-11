# Mencari nilai terbesar dalam array
# Kita memiliki array yang beranggotakan nilai integer dengan elemen indeks ke-0 adalah 1, elemen indeks ke-1 adalah 7, elemen indeks ke-2 adalah 2, elemen indeks ke-3 adalah 89, elemen indeks ke-4 adalah 3.

# Algoritma two pointers
var_arr = [1, 7, 2, 89, 3]

left_pointer = var_arr[0]

for i in range(1, len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer

print(f"Elemen terbesar: {left_pointer}")

# Kita menggunakan perulangan "for" untuk mengakses semua indeks dari indeks ke-1 hingga panjang array. Untuk mengetahui panjang array, kita menggunakan fungsi "len()", yang  bertujuan menghitung panjang atau banyaknya elemen dari list, set, dan string.
