"""
todo:
Buatlah sebuah fungsi bernama "minimal" dengan ketentuan berikut.
- Menerima dua buah argumen berupa number, yaitu a dan b.
- Mengembalikan nilai terkecil antara a atau b.
- Bila nilai keduanya sama, kembalikan dengan nilai a.
"""
def minimal(a, b):
    """
    Fungsi ini digunakan untuk menentukan nilai minimal.

    Args:
        a (int): bilangan pertama.
        b (int): bilangan kedua.

    Returns:
        int: mengembalikan nilai terkecil antara a / b tetapi jika keduanya sama maka yang akan dikembalikan adalah a.
    """
    if a < b:
        return a
    elif a > b:
        return b
    else:
        return a

print(minimal(11, 12))