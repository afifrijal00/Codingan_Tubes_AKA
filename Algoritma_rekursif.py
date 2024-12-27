def cari_nim_rekursif(array, nim_cari, index=0):
    if index >= len(array): 
        return -1
    if array[index] == nim_cari: 
        return index
    return cari_nim_rekursif(array, nim_cari, index + 1) 

array_nim = [f"23111022{i}" for i in range(1, 1001)]

nim_cari = input("Masukkan NIM yang ingin dicari: ")

hasil = cari_nim_rekursif(array_nim, nim_cari)

if hasil != -1:
    print(f"NIM ({nim_cari}) tersebut adalah mahasiswa Tel-U yang terdapat pada indeks {hasil}.")
else:
    print(f"NIM ({nim_cari}) tersebut bukan mahasiswa Tel-U.")
