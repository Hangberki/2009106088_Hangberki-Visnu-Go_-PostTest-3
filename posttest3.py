def total(jumlah):
	total= jumlah * 2000
	print("ini jumlah yang harus anda bayar RP.%i" % total)

def total2(jumlah):
	total = jumlah *2500
	print("ini jumlah yang harus anda bayar RP.%i" % total)

def diskon1(jumlah):
	harga = jumlah * 2000
	diskon = harga * (10/100)
	total = harga - diskon
	print("dikarenakan anda memesan lebih dari 10 pcs")
	print("maka kami berikan potongan harga sebesar 10%")
	print("ini total harga dari pesanan anda RP.%i" % total)
	print("silahkan dibayarr ngab")

def diskon2(jumlah):
	harga = jumlah * 2500
	diskon = harga * (8/100)
	total = harga - diskon
	print("dikarenakan anda memesan lebih dari 8 pcs")
	print("maka kami berikan potongan harga sebesar 8%")
	print("ini total harga dari pesanan anda RP.%i" % total)
	print("silahkan dibayarr ngab")

def batas(samadengan):
	a =("="*50)
	print(a)


print("       ==========================")
print("       ===== SELAMAT DATANG =====")
print("       === DI RUMAH TAKOYAKI ====")
print("       ==========================")
print("")
print("")


daftar_menu = {
	"1. pedes nyantai" : "RP.2000.00/pcs ",
	"2. pedes Gila" : "RP.2500.00/pcs "
}

batas ("")
print("Ini daftar menu yang kami miliki disini:")


for X,Y in daftar_menu.items():
	print(X,Y)


batas("")
print("kami lagi ada diskon akhir tahun yaitu:")
print("1. setiap pembelian kesepuluh varian pedes nyantai")
print("   akan di berikan potongan harga sebesar 10% ")
print("2. setiap pembelian kedelapan varian pedes Gila")
print("   akan di berikan potongan harga sebesar 8% ")
print("=" * 50)

print("Masukan menu apa yang ingin kaian beli :")
pemesanan = int(input(""))
batas("")

if pemesanan ==1:
	print("silahkan masukan berapa pcs yang kalian inginkan:")
	isi = int(input(""))
	if isi < 10:
		total(isi)

	elif isi >= 10 and isi <= 45 :
		diskon1(isi)

	elif isi > 45:
		print("""maaf kami tidak memiliki cukup stock untuk
			memenuhi pesanan anda""")

	else:
		""

elif pemesanan == 2:
	print("silahkan masukan berapa pcs yang kalian inginkan:")
	isi2 = int(input(""))
	if isi2 < 8:
		total2(isi2)

	elif isi2 >=8 and isi2 <=40:
		diskon2(isi2)

	elif isi2 >40:
		print("""maaf kami tidak memiliki cukup stock untuk
			memenuhi pesanan anda""")

	else:
		""

batas("")
print("          SILAHKAN DI TUNGGU!!!")
print("TERIMAKASIH SUDAH MEMESAN DI RUMAH TAKOYAKI")