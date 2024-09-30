pecahan = [1, 2, 5, 10]
n = len(pecahan)  # Ini operasi buat nyari banyak angka di array (output = banyak elemen di pecahan)

def cariNilaiMin(P):
    pecahan.sort()  # Buat memastikan koin2 nya diurutin dari kecil ke besar
    
    # Inisiasi jawaban kosongan buat tempat array jawaban
    jawaban = []
    
    # Ketika P (total yg mau dicari) lebih dari pecahan[i]
    # P akan dikurangi nilai pecahan[i] dan pecahan[i] dimasukkan ke list jawaban
    # Sisa dari P akan dikurangi lagi dengan pecahan[i] dan pecahan[i] akan dimasukkan jawaban
    # Seterusnya sampai 0
    for i in range(n - 1, -1, -1):  # For loop untuk memilih dari pecahan dari belakang array ke depan array (Besar ke kecil)
        while P >= pecahan[i]:
            P -= pecahan[i]
            jawaban.append(pecahan[i])
    
    # Print jawaban berupa koin2 yang menyusun total P dengan jumlah minimum
    print(" ".join(map(str, jawaban)))

def main():
    n = int(input("Masukan jumlah koin : "))
    print(f"Koin minimal untuk mengganti {n}:", end=" ")
    cariNilaiMin(n)

if __name__ == "__main__":
    main()