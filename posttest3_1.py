print("Tentukan Nilai yang di inginkan : ")
N = int(input(""))
for x in range(N):
    if (10 ** x > N):
        break
    else:
        print(x)

print("Nilai terkecil dari 10^x > n adalah", 10 ** x)