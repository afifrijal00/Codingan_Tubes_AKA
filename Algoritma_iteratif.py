def cari_nim_iteratif(array, nim_cari):
    for i in range(len(array)):
        if array[i] == nim_cari: 
            return i
    return -1 

array_nim = [f"23111022{i}" for i in range(1, 1001)]

nim_cari = input("Masukkan NIM yang ingin dicari: ")

hasil = cari_nim_iteratif(array_nim, nim_cari)

if hasil != -1:
    print(f"NIM ({nim_cari}) tersebut adalah mahasiswa Tel-U yang terdapat pada indeks {hasil}.")
else:
    print(f"NIM ({nim_cari}) tersebut bukan mahasiswa Tel-U.")
