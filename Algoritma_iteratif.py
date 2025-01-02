import time

def cari_nim_binary_iteratif(array, nim_cari):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == nim_cari:
            return mid
        elif array[mid] < nim_cari:
            low = mid + 1
        else:
            high = mid - 1

    return -1

array_nim = [f"23111022{i}" for i in range(1, 1001)]

nim_cari = input("Masukkan NIM yang ingin dicari: ")
start_time = time.time()

# Melakukan pencarian
hasil = cari_nim_binary_iteratif(array_nim, nim_cari)

# Mencatat waktu setelah pencarian
end_time = time.time()

# Menghitung waktu eksekusi
running_time = end_time - start_time

# Menampilkan hasil pencarian dan waktu eksekusi
if hasil != -1:
    print(f"NIM ({nim_cari}) tersebut adalah mahasiswa Tel-U yang terdapat pada indeks {hasil}.")
else:
    print(f"NIM ({nim_cari}) tersebut bukan mahasiswa Tel-U.")

print(f"Waktu yang dibutuhkan untuk pencarian: {running_time:.6f} detik.")
