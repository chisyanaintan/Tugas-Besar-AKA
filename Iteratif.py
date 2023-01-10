def jumlah(n: int) -> int:
    total = 0
    for i in range(n, 0, -1):
        total += i
    return total


n = int(input("Masukkan nilai n : "))
print("Hasil penjumlahan dari 1 hingga",n, "adalah", jumlah(n))
