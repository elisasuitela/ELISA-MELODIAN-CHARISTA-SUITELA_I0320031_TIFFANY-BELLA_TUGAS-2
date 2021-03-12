print("Biodata & Kehidupan Kuliah")

nama = "Elisa Melodian Charista Suitela"
tempat_lahir = "Kudus"
tanggal_lahir = "4 September 2002"
alamat = "Jalan Raya Muncul KM 7, Desa Kalibeji, Kecamatan tuntang, Kabupaten Semarang"
golongan_darah = "B"
print("Nama Lengkap: ", nama, "\n", "Tempat Lahir: ", tempat_lahir, "\n", "Alamt: ", alamat, "\n", "Golongan Darah: ", golongan_darah)

nim = "I0320031"
kelas = "A"
angkatan = "2020"
prodi = "Teknik Industri"
fakultas = "Teknik"
universitas = "Universitas Sebelas maret"
print("NIM :", nim, "\n", "Kelas: ", kelas, "\n", "Angkatan: ", angkatan, "\n", "Program Studi: ", prodi, "\n", "Fakultas: ", fakultas, "\n", "Universitas: ", universitas)

tanggal_hari_1_kuliah = 17
bulan_hari_1_kuliah = 9
tahun_hari_1_kuliah = 2020
tanggal_sekarang = 13
bulan_sekarang = 3
tahun_sekarang = 2021
durasi_dalam_bulan = float(((tanggal_sekarang - tanggal_hari_1_kuliah) / 30) + (bulan_sekarang - bulan_hari_1_kuliah) + ((tahun_sekarang - tahun_hari_1_kuliah) * 12))
print("tanggal Hari Pertama Kuliah: ", tanggal_hari_1_kuliah, "\n", "Bulan Hari pertama Kuliah: ", bulan_hari_1_kuliah, "\n", "Tahun Hari pertama kuliah: ", tahun_hari_1_kuliah, "\n", "Sudah Kuliah di UNS Selama : ", durasi_dalam_bulan, "Bulan")

jarak_rumah_kampus_dalam_KM = 74
kecepatan_ratarata_dalam_KM_per_jam = 60
perkiraan_durasi_dalam_jam = float(jarak_rumah_kampus_dalam_KM / kecepatan_ratarata_dalam_KM_per_jam)
print("Jarak dari Rumah ke Kampus: ", jarak_rumah_kampus_dalam_KM, "KM", "\n", "Kecepatan Rata - Rata Perjalanan Rumah Kampus: ", kecepatan_ratarata_dalam_KM_per_jam, "KM/Jam", "\n", "Perkiraan Durasi Perjalanan Rumah Kampus: ", perkiraan_durasi_dalam_jam, "Jam")

kendaraan = "Motor Honda Vario 125"
jarak_tempuh_1_liter_bensin_dalam_KM = 50
harga_1_liter_bensin_pertalite_dalam_rupiah = 7650
kebutuhan_bensin = float(jarak_rumah_kampus_dalam_KM / jarak_tempuh_1_liter_bensin_dalam_KM)
perkiraan_biaya_bahan_bakar_dalam_rupiah = int(kebutuhan_bensin * harga_1_liter_bensin_pertalite_dalam_rupiah)
print("kendaraan Yang Digunakan: ", kendaraan, "\n", "Jarak Tempuh 1 Liter Bensin: ", jarak_tempuh_1_liter_bensin_dalam_KM, "KM", "\n", "Harga 1 liter pertalite: ","Rp. ", harga_1_liter_bensin_pertalite_dalam_rupiah, "\n", "Kebutuhan Bensin Untuk Sekali Perjalanan Rumah ke Kampus: ", kebutuhan_bensin, "\n", "Perkiraan Biaya Bahan Bakar untuk 1 kali Perjalanan Rumah Kampus: ", "Rp. ", perkiraan_biaya_bahan_bakar_dalam_rupiah )
