import time
import matplotlib.pyplot as plt

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

# Membuat array NIM dari 2311102201 hingga 231110221000 secara otomatis
array_nim = [f"23111022{i:03}" for i in range(1, 1001)]
nim_to_search = "23111022999"  # Menggunakan NIM terakhir untuk kasus terburuk

# Mengukur waktu eksekusi algoritma iteratif
iterative_times = []
for size in range(1, len(array_nim) + 1, 100):  # Ambil sampel setiap 100 elemen
    start_time = time.time()
    cari_nim_binary_iteratif(array_nim[:size], nim_to_search)
    end_time = time.time()
    iterative_times.append(end_time - start_time)

# Mengukur waktu eksekusi algoritma rekursif
recursive_times = []
for size in range(1, len(array_nim) + 1, 100):  # Ambil sampel setiap 100 elemen
    start_time = time.time()
    cari_nim_binary_rekursif(array_nim[:size], nim_to_search, 0, size - 1)
    end_time = time.time()
    recursive_times.append(end_time - start_time)

# Plot hasil perbandingan waktu eksekusi
sizes = list(range(1, len(array_nim) + 1, 100))
plt.figure(figsize=(10, 6))
plt.plot(sizes, iterative_times, label='Binary Search Iterative', marker='o')
plt.plot(sizes, recursive_times, label='Binary Search Recursive', marker='x')
plt.title('Perbandingan Running Time: Binary Search Iterative vs Recursive')
plt.xlabel('Ukuran Array (jumlah NIM)')
plt.ylabel('Running Time (detik)')
plt.legend()
plt.grid()
plt.show()
