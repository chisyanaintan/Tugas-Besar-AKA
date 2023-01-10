def jumlah(n: int) -> int:
    total = 0
    for i in range(n, 0, -1):
        total += i
    return total

n = int(input("Masukkan nilai n : "))
import datetime
start = datetime.datetime.now()
print("Hasil penjumlahan dari 1 hingga",n, "adalah", jumlah(n))
end = datetime.datetime.now()
waktu = end - start
print("Execution Time = ", waktu.microseconds, "microseconds")
