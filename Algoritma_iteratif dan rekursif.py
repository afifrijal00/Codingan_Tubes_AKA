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

# Data NIM array
array_nim = [f"23111022{i}" for i in range(1, 1001)]

def main_menu():
    while True:
        print("\nMenu:")
        print("1. Cari NIM menggunakan algoritma iteratif")
        print("2. Cari NIM menggunakan algoritma rekursif")
        print("3. Tampilkan waktu eksekusi pencarian NIM")
        print("4. Keluar")

        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            nim_cari = input("Masukkan NIM yang ingin dicari: ")
            hasil = cari_nim_binary_iteratif(array_nim, nim_cari)
            if hasil != -1:
                print(f"NIM ({nim_cari}) tersebut adalah mahasiswa Tel-U yang terdapat pada indeks {hasil}.")
            else:
                print(f"NIM ({nim_cari}) tersebut bukan mahasiswa Tel-U.")
        
        elif pilihan == "2":
            nim_cari = input("Masukkan NIM yang ingin dicari: ")
            hasil = cari_nim_binary_rekursif(array_nim, nim_cari, 0, len(array_nim) - 1)
            if hasil != -1:
                print(f"NIM ({nim_cari}) tersebut adalah mahasiswa Tel-U yang terdapat pada indeks {hasil}.")
            else:
                print(f"NIM ({nim_cari}) tersebut bukan mahasiswa Tel-U.")
        
        elif pilihan == "3":
            nim_cari = input("Masukkan NIM yang ingin dicari: ")

            # Iteratif
            start_iterative = time.time()
            cari_nim_binary_iteratif(array_nim, nim_cari)
            end_iterative = time.time()

            # Rekursif
            start_recursive = time.time()
            cari_nim_binary_rekursif(array_nim, nim_cari, 0, len(array_nim) - 1)
            end_recursive = time.time()

            print(f"Waktu eksekusi algoritma iteratif: {end_iterative - start_iterative:.6f} detik")
            print(f"Waktu eksekusi algoritma rekursif: {end_recursive - start_recursive:.6f} detik")
        
        elif pilihan == "4":
            print("Terima kasih telah menggunakan program ini.")
            break
        
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Menjalankan program
main_menu()
