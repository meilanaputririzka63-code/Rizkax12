# ===========================================
# Program Klulusan Siswa
# ===========================================

while True: 
    nilai_siswa = int(input("\nMasukkan nilai siswa: "))
    
    if nilai_siswa >= 75:
        print("Tuntas")
        break
    else:
        ulang = input("Nilai kurang. Apakah ingin mengulang? (Ya/Tidak): ")
          
        if ulang.lower() == "ya":
            continue
        else:
            print("Tidak Tuntas")
            break