# todo:
# Sebuah variabel array diberikan dengan ketentuan berikut.
# - Variabel array bernama "var_array" dengan nilai dari 0 hingga 100.
# - Hitung nilai rata-rata dari elemen array tersebut.
# - Simpan hasil perhitungan dalam variabel bernama "result".

var_array = [i for i in range(101)]
jumlah_data = 0
banyak_data = len(var_array)

for i in range(len(var_array)):
    jumlah_data = jumlah_data + var_array[i]
    if i == len(var_array)-1:
        result = jumlah_data/banyak_data

print(jumlah_data)
print(result)