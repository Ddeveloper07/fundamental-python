# Library file management => kumpulan library yang dirancang untuk membantu pengguna dalam mengelola dan berinteraksi dengan berkas dan direktori pada sistem file

# Os => berguna untuk fungsi-fungsi yang berkaitan dengan sistem operasi, misalnya open(), path(), getcwd(), dan fungsi lainnya
import os
print(os.getcwd)

# JSON (JavaScript Object Notation)
"""
Perbedaan dengan pickle
1. JSON adalah format text-serialization dan umumnya menggunakan Unicode atau UTF-8. Sementara pickle bersifat binary serialization.
2. JSON dapat dibaca dengan mudah oleh manusia, sementara pickle tidak dapat.
3. JSON dapat dioperasikan dan digunakan di luar ekosistem python. Pickle adalah Python-specific.
4. JSON secara default hanya dapat merepresentasikan subset dari built-in type pada python.
5. Pickle dapat merepresentasikan hampir (jika tidak seluruh) tipe Python dan secara default melakukan kompresi data.
"""

# Contoh code JSON sederhana
import json

# contoh JSON:
x = '{ "nama":"Buchori", "umur":22, "kota":"New York"}'

# parse x:
y = json.loads(x)

print(y["umur"])

# Pickle atau pickling adalah istilah mengubah objek menjadi byte stream, sedangkan unpickling adalah perilaku sebaliknya
import pickle
# cd

# Mengekstrasi berkas pickle dan menaruhnya pada sebuah variabel
pickle_masuk = open("dict.pickle", "rb")
contohDictionary = pickle.load(pickle_masuk)
pickle_masuk.close()

print(contohDictionary)
