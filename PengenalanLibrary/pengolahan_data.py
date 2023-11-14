import pandas as pd

# Membuat DataFrame dari dictionary
data = {
    'Nama': ['John', 'Jana', 'Bobe', 'Mauren'],
    'Usia': [21, 22, 23, 24],
    'Pekerjaan': ['Engineer', 'Freelance', 'Designer', 'Jurnalistic']
}

df = pd.DataFrame(data)

# Menampilkan DataFrame
print('--------------')
print('Hasil Percobaan Library Pandas')
print(df)
print('--------------')

"""
Keterangan:
Pada contoh diatas, kita membuat DataFrame dari dictionary dan menampilkannya ke layar.
"""

# NumPy
import numpy as np

matriks = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('--------------')
print('Hasil Percobaan Library Pandas')
print(matriks)
print('--------------')

"""
Keterangan:
Pada kode di atas, kita mengimpor library numpy sebagai np terlebih dahulu
untuk mengambil fungsi-fungsi atau kode yang berada pada library tersebut.
"""

# Matplotlib
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Membuat plot garis
plt.plot(x, y)

# Menambahkan judul dan label sumbu
plt.title("Contoh plot garis")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")

# Menampilkan plot
plt.show()

"""
Keterangan:
pada kode di atas kita akan membuat visualisasi berdasarkan data dari variabel x dan y.
"""

# Seaborn
import seaborn as sns 

# Contoh data
tips = sns.load_dataset('tips') # Memuat dataset tips dari Seaborn

# Contoh plot histogram
sns.histplot(tips['total_bill'], kde=True)
plt.title('Histogram Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()

"""
Keterangan:
pada contoh di atas, kita menggunakan seaborn untuk melakukan visualisasi berdasarkan dataset tips.
Dataset ini adalah bawaan dari library seaborn yang dapat anda gunakan.
"""