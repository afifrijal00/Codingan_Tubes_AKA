import time

def cari_nim_binary_rekursif(array, nim_cari, low, high):
    if low > high:  
        return -1
    
    mid = (low + high) // 2 
    if array[mid] == nim_cari:  
        return mid
    elif array[mid] < nim_cari:  
        return cari_nim_binary_rekursif(array, nim_cari, mid + 1, high)
    else:  
        return cari_nim_binary_rekursif(array, nim_cari, low, mid - 1)

array_nim = [f"23111022{i}" for i in range(1, 1001)]

# Meminta input NIM yang ingin dicari
nim_cari = input("Masukkan NIM yang ingin dicari: ")

# Mencatat waktu sebelum pencarian
start_time = time.time()

# Melakukan pencarian
hasil = cari_nim_binary_rekursif(array_nim, nim_cari, 0, len(array_nim) - 1)

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
