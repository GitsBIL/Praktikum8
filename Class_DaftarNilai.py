class DaftarNilai:
    def __init__(self):
        self.data_mahasiswa = []

    def tambah(self):
        print("\nTambah Data Mahasiswa")
        nim = input("Masukkan NIM Mahasiswa: ")
        nama = input("Masukkan Nama Mahasiswa: ")
        tugas = float(input("Masukkan Nilai Tugas: "))
        uts = float(input("Masukkan Nilai UTS: "))
        uas = float(input("Masukkan Nilai UAS: "))
        nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
        self.data_mahasiswa.append({
            "NIM": nim,
            "Nama": nama,
            "Tugas": tugas,
            "UTS": uts,
            "UAS": uas,
            "Nilai Akhir": nilai_akhir
        })
        print("Data berhasil ditambahkan!")

    def tampilkan(self):
        if not self.data_mahasiswa:
            print("\nDaftar Nilai Mahasiswa Kosong")
            return
        print("\nDaftar Nilai Mahasiswa:")
        print("="*77)
        print(f"| {'NIM':^10} | {'Nama':^15} | {'Tugas':^5} | {'UTS':^5} | {'UAS':^5} | {'Akhir':^7} |")
        print("="*77)
        for mahasiswa in self.data_mahasiswa:
            print(f"| {mahasiswa['NIM']:^10} | {mahasiswa['Nama']:^15} | {mahasiswa['Tugas']:^5} | {mahasiswa['UTS']:^5} | {mahasiswa['UAS']:^5} | {mahasiswa['Nilai Akhir']:^7.2f} |")
        print("="*77)

    def ubah(self, nama):
        for mahasiswa in self.data_mahasiswa:
            if mahasiswa["Nama"].lower() == nama.lower():
                print("Data ditemukan. Silakan perbarui.")
                mahasiswa["Nama"] = input("Masukkan Nama Baru: ")
                mahasiswa["Tugas"] = float(input("Masukkan Nilai Tugas Baru: "))
                mahasiswa["UTS"] = float(input("Masukkan Nilai UTS Baru: "))
                mahasiswa["UAS"] = float(input("Masukkan Nilai UAS Baru: "))
                mahasiswa["Nilai Akhir"] = (mahasiswa["Tugas"] * 0.3) + (mahasiswa["UTS"] * 0.35) + (mahasiswa["UAS"] * 0.35)
                print("Data berhasil diperbarui!")
                break
        else:
            print("Data dengan nama tersebut tidak ditemukan.")

    def hapus(self, nama):
        for mahasiswa in self.data_mahasiswa:
            if mahasiswa["Nama"].lower() == nama.lower():
                self.data_mahasiswa.remove(mahasiswa)
                print("Data berhasil dihapus!")
                break
        else:
            print("Data dengan nama tersebut tidak ditemukan.")

def main():
    daftar_nilai = DaftarNilai()

    while True:
        print("\nMenu:")
        print("[T]ambah, [L] Tampilkan data, [U]bah, [H]apus, [K]eluar")
        pilihan = input("Pilih menu: ").lower()

        if pilihan == "t": 
            daftar_nilai.tambah()

        elif pilihan == "l": 
            daftar_nilai.tampilkan()

        elif pilihan == "u": 
            nama = input("\nMasukkan Nama Mahasiswa yang ingin diubah: ")
            daftar_nilai.ubah(nama)

        elif pilihan == "h": 
            nama = input("\nMasukkan Nama Mahasiswa yang ingin dihapus: ")
            daftar_nilai.hapus(nama)

        elif pilihan == "k": 
            print("Terima kasih telah menggunakan program ini!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
