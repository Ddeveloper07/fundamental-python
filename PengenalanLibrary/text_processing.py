# String
testString = "Dicksa"

# 1. upper()
print(testString.upper())

# 2. lower()
print(testString.lower())

# 3. title()
print(testString.title())

# 4. split('c')
print(testString.split('c'))

# 5. zfill(15)
print(testString.zfill(15))

"""
Penjelasan :
upper(): Ubah setiap huruf dalam string menjadi huruf kapital. 
lower(): Ubah setiap huruf dalam string menjadi huruf kecil.
split(): Pisahkan teks berdasarkan delimiter (karakter pemisah).
title(): Jadikan setiap awal kata kapital.
zfill(): Tambahkan nol di awal string sebanyak nilai yang ada pada parameter.

"""

# Regex => sebuah cara untuk mencari teks berdasarkan pola tertentu
import re # Import modul regex

pola= '^a....s$' # ^a berarti kita ingin mencari teks dengan awalan 'a', dan s$ berarti kita ingin mencari string berakhiran 's'.
string_tes= 'abysss'
hasil= re.match(pola, string_tes)

if hasil:
    print("Pencarian berjaya.")
else:
    print("Pencarian gagal.")

"""
Note :
beberapa modul perlu diimpor terlebih dahulu untuk bisa digunakan.
"""