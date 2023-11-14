# Library web scraping => jenis library untuk membantu pengguna mengumpulkan data dari halaman web.

# Beberapa library untuk melakukan web scraping adalah berikut.

# 1. Beautifulsoup => library untuk mengambil data dari halaman web dan mengekstrak informasi yang diperlukan
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Pengambilan konten
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")

# Membuat objek BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Mencetak judul halaman
print("---------------")
print("Library BeautifulSoup")
print(soup.title)
print("---------------")

"""
Keterangan:
Pada contoh di atas, kita melakukan web scraping untuk mengambil judul dari halaman web "http://python.org/.
"""

# Urlib => lebih kompleks dari beautifulsoup dan kegunaanya sama dengan beautifulsoup

# Mencari indeks awal dan akhir
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")

# Mengekstrak dan mencetak judul halaman
title = html[start_index:end_index]

print("---------------")
print("Hasil Urllib")
print(title)
print("---------------")