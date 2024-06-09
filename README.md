# [ANALISIS DATA PENJUALAN MENGGUNAKKAN KODE PYTHON]

# Soal:
Diberikan sebuat file bernama “Online_Retail_Data.csv”. Analisis lah data dalam file tersebut mulai dari total penjualan produk selama satu tahun, total penjualan setiap bulannya, total penerimaan (revenue) setiap bulannya, dan tren penjualan produk setiap bulan.

# Jawaban:
•	Langkah 1: Impor Data
1.	Impor library yang diperlukan untuk analisis data dan visualisasi.
2.	Baca data penjualan dari file CSV “Online_Retail_Data.csv” dan simpan ke dalam DataFrame.
   
•	Langkah 2 Data Cleaning: Bersihkan data dari 
1.	Features yang data type nya tidak sesuai
2.	Duplicate, missing value, atau outliers
3.	Distribusi yang tidak masuk akal
   (https://github.com/rindusiregar/TUGAS-UAS-RINDU-SIREGAR-AKUNTANSI-158/blob/master/pictures/dataclening.png)
•	Langkah 3: Analisis dan Visualisasi
1.	Membuat variable yang berisi penghitungan total penjualan produk selama satu tahun, total penjualan setiap bulannya, total penerimaan (revenue) setiap bulannya, dan tren penjualan produk setiap bulan.
2.	Visualisasikan setiap hasil dari variabell yang telah  dibuat menggunakan grafik.
   (https://github.com/rindusiregar/TUGAS-UAS-RINDU-SIREGAR-AKUNTANSI-158/blob/master/pictures/datavisualisasi.png)
 
Hasil Analisis
# Total Penjulan Produk
(https://github.com/rindusiregar/TUGAS-UAS-RINDU-SIREGAR-AKUNTANSI-158/blob/master/pictures/salesbyproduct.png)
Dari grafik dan hasil analisis diatas dapat dilihat bahwa penjualan produk tidak merata untuk setiap jenisnya. Produk dengan prnjualan tertinggi ialah beware of the cat metal sign dengan total penjualan dalam setahun sejumlah 600 unit. Peringkat dua tertinggi ialah way out metal sign dan diikuti oleh home sweet home metal sign. Sedangkan produk dengan total penjualan terendah yang tidak melebihi 10 unit beberapa diantaranya ialah ant white sweatheart table with 3 draw, baking set 9 piece retrospot, hall cabinet with 3 drawers, metal wall shelf unit with hooks, pink and lilac qualited throw, pink kashmiri occasional table, dll.

# Total Penjualan Dan Total Revenue Setiap Bulan
(https://github.com/rindusiregar/TUGAS-UAS-RINDU-SIREGAR-AKUNTANSI-158/blob/master/pictures/salesandrevenue.png)
Dalam tahun berjalan, total penjualan terbanyak dan revenue tertinggi terjadi di bulan Januari dengan total 6.414 unit dan dengan revenue  $16.426. Dan penjualan paling sedikit terjadi di bulan Oktober dengan total 51 unit namun dengan revenue $2.875 yang berada pada peringkat 7. Sedangkan revenue terendah terjadi di bulan Maret dengan total $696 dengan penjualan sebanyak 176 unit yang berada di peringkat 5. Perbedaan antara total penjualan dengan total revenue yang hubungannya tidak bersfiat  positif (ketika penjualan naik maka revenue akan naik) ini bisa terjadi disebabkan beberapa faktor salah satu diantaranya yaitu produk yang terjual pada bulan Oktober (penjualan paling sedikit) memilki harga yang lebih tinggi dibandingkan dengan produk-produk yang terjual pada bulan Maret.

# Tren Penjualan Produk Setiap Bulan
(https://github.com/rindusiregar/TUGAS-UAS-RINDU-SIREGAR-AKUNTANSI-158/blob/master/pictures/topproducteverymonth.png)
Tren penjualan selama setahun setiap bulannya dapat dilihat pada grafik dan hasil analisi. Dapat disimpulkan bahwa produk dengan penjualan tertinggi setiap bulannya selalu berganti. Namun pada bulan Maret dan  Mei penjualan tertinggi ialah produk “Manual”.
