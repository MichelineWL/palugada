Nama : Micheline Wijaya Limbergh 
NPM : 2306207013
Kelas : PBP D 

PWS : http://micheline-wijaya-palugada3.pbp.cs.ui.ac.id/


Cara saya mengimplementasikan checklist step by step 
// Membuat sebuah proyek Django baru 
1. Membuat github
2. Menarik github (clone) ke dalam repositori lokal
3. Membuat env dan emnjalankannya
4. Membuat requirements.txt dan menginstall dependencies didalamnya
5. Membuat proyek django bernama "palugada"
6. Menambahkan 2 string ke dalam ALLOWED_HOSTS pada settings.py
7. Menjalankan server (manage.py) untuk mengetes apakah sudah ada
8. Push ke github (Sebelumnya menambahkan .gitignore terlebih dahulu agar tidak semua berkas dan direktori dilacak oleh git)
//  Membuat aplikasi dengan nama main pada proyek tersebut.
1. Setelah mengaktifkan env, membuat aplikasi main dengan menjalankan perintah: python manage.py startapp main lalu mendaftarkannya ke settings.py (INSTALLED_APPS)
// Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
1. Pada urls di palugada, saya meng-include main.urls
// Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib.
1. Pada tahap ini saya hanya membuat suatu class bernama Product lalu mengisi atribut wajib sesuai dengan tipe yang diberikan pada informasi Tugas 2
//  Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
1. Pada tahap ini saya membuat fungsi show_main dan didalamnya terdapat beberapa atribut beserta datanya, termasuk beberapa atribut tambahan yaitu nama_toko, nama_pemilik, dan kelas_pemilik
2. Melakukan render agar data tersebut bisa masuk ke template html
// Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
1. pada urls di main, saya mendefinisikan app_main lalu membuat ppath dengan memanggil show_main
//  Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
1. Buat PWS 
2. Masukin urlnya ke settings.py 
3. Menjalankan procet command pada PWS
4. Isi username dan password 
5. Ubah nama branch menjadi main
6. Push PWS main:master



Bagan request client ke web aplikasi berbasis Django beserta responsenya. 
Mengaitkan bagan dengan urls.py, views.py, models.py, dan berkas HTML 

Client <-----> NGINX <------> Server <-----> Database 
    -----------------------------------> HTTP Request
    <----------------------------------- HTTP Response

Client <-----> NGINX <------> Server <-----> Database 
   👇🏻                          👆🏻
   |                             |
   |                             |
  URLS ----- Model ----- View ----- HTML

Client(user) ketika melakukan suatu aksi (contoh: double click/pencet button di web) akan
 secara otomatis melakukan suatu request melalui HTTP yang biasa dibungkus oleh Security 
 Socket Layer (SSL) menjadi HTTPS. Setelah dilakukan request (URLS nangkap request), model 
 yang sudah berisi aturan dari view akan digunakan oleh view. Data dari view akan digunakan
 oleh HTML (render: jika menggunakan selain django biasa dinamakan dengan integrasi (fetch API)). 
 Data yang harus disimpan juga akan disimpan ke dalam database saat render dilakukan (GET API). 
 Selanjutnya, bersamaan dengan hal tersebut dilakukan router (jika di react.js menggunakan router) 
 untuk mendefinisikan path atau url yang dapat diakses oleh user. Keempat hal ini kemudian dikirim 
 dalam bentuk HTTP Response.


Fungsi git dalam pengembangan perangkat lunak sangatlah banyak. Hal utama dari git adalah 
bagaimana membantu developer untuk bekerja membuat program. Hal ini dikarenakan git dapat 
melacak perubahan yang terjadi pada kode sedetail mungkin. Bahkan, jika git digunakan pada 
semua anggota dalam tim yang bekerja untuk membuat suatu proyek, dapat melakukan branch agar 
masing masing dari developer dapat membagi tugas dan kemudian dapat merge ketika selesai pada 
branch main. Selain itu, ketika developer ingin mengulang kode dari kode terakhir yang sudah 
di commit, developer dapat meng clone ulang atau control Z sampai terakhir kali push. Pada commit 
pun, developer dapat memspesifikasi perubahan apa yang dilakukan. Apakah feat, fix, refactor, dan 
sebagainya (frontend). Dengan sistem git, developer dapat work from far tanpa harus melakukan 
coding pada satu laptop saja. 


Framework Django dijadikan permulaan pembelajaran perangkat lunak karena konektivitas dari 
frontend dan backend yang menjadi satu kesatuan. Mulai dari harus mendefinisikan tipe dan 
menyediakan data (backend) sampai pada menampilkannya (HTML CSS JS --> frontend) yang disambungkan 
menggunakan render. Kompleksitas dari Django masih lebih sederhana dibandingkan ketika menggunakan 
framework lain contohnya react.js, atau mongodb, dan sebagainya dimana developer akan ngoding di 2 
tempat, menggunakan bahasa yang berbeda, dan harus melakukan integrasi terhadap frontend dan backend. 


Model pada Django disebut sebagai ORM karena django memetakan objek ke tabel-tabel dalam basis 
data yang relasional. Dengan demikian developer tidak harus menulis langsung query SQL. Sehingga 
ketika melakukan CRUD lebih mudah tanpa perlu menulis SQL secara manual. Compact dengan berbagai 
jenis database yang didukung oleh Django pula.