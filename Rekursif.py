def jumlah(n: int) -> int:
    if n == 0:
        return 0
    else:
        return n + jumlah(n - 1)


n = int(input("Masukkan nilai n : "))

import datetime
start = datetime.datetime.now()
print("Hasil penjumlahan dari 1 hingga",n, "adalah", jumlah(n))
end = datetime.datetime.now()
waktu = end - start
print("Execution Time = ", waktu.microseconds, "microseconds")
