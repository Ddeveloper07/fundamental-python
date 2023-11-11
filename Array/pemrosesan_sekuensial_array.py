# Dikarenakan pemrosesan sekuensial melibatkan semua elemen di dalamnya, ada beberapa hal yang harus diperhatikan
# 1. Setiap elemen array diakses secara langsung melalui indeksnya (metode indexing)
# 2. Elemen pertama (first element) adalah elemen array dengan indeks terkecil yang selalu dimulai dari 0
# 3. Elemen selanjutnya (next element) dicapai melalui suksesor indeks.
# 4. Kondisi terhenti dicapai jika indeks yang diproses adalah indeks terbesar yang sudah terdefinisi.
# 5. Suatu array tidak boleh kosong, minimal memiliki satu elemen di dalamnya.

# Contoh pemrosesan sekuensial
var_arr = [1, 2, 3, 4, 5]

for i in range(len(var_arr)):
    current_element = var_arr[i] # Metode indexing
    next_index = i+1 # Suksesor indeks

    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None
        
    print(f"Current element: {current_element}, next elements: {next_element}")

# Contoh lain dari pemrosesan array
# 1. Mengisi array secara sekuensial
# 2. Menghitung nilai rata_rata elemen array
# 3. Mengalikan elemen array dengan suatu nilai.
# 4. Mencari nilai terbesar atau terkecil pada array.
# 5. Mencari indeks letak suatu nilai ditemukan pertama kali dalam array, dan sebagainya.