import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan Nama Anda")
parser.add_argument('-t', '--tanggallahir', required=True, help="Masukkan Tanggal Lahir Anda")
args = parser.parse_args()

print("Terimakasih telah menggunakan parser.py, "+args.nama+" yang lahir pada tanggal "+args.tanggallahir)

"""
Note:
Berkas panggildicoding.py harus dipanggil dengan parameter -n atau --nama.
Jika kita memanggil berkas tanpa parameter -n, berkas akan meminta parameter n atau nama.
Jika kita memanggil dengan -n NAMAKITA atau --nama NAMAKITA, berkas akan menampilkan Terima kasih telah menggunakan panggildicoding.py NAMAKITA.
Jika kita memanggil --help, tampil help dengan penjelasan "Masukkan Nama Anda".

Berkas panggildicoding.py harus dipanggil dengan parameter n/nama dan t/tanggallahir.
Format tanggal lahir adalah dd-mm-yyyy.
Jika kita memanggil berkas tanpa parameter, berkas akan menolak.
"""