Nama : Micheline Wijaya Limbergh 
NPM : 2306207013
Kelas : PBP D 

PWS : http://micheline-wijaya-palugada.pbp.cs.ui.ac.id/

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery diperlukan agar memastikan bahwa semua user mendapatkan informasi yang sama meski website bersifat dinamis (isi dari website tidak statis). Data delivery ini dimuat dalam suatu proses bernama render dimana didalamnya, database, backend, dan frontend mengintegrasikan kode mereka. Biasanya pengintegrasian terssebut menggunakan suatu API. 
2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya yang lebih baik adalah JSON. Alasannya sama dengan mengapa JSON lebih populer dibandingkan dengan XML. Hal ini dikarenakan format output JSON dapat lebih mudah dimengerti dan lebih ringkas meski untuk orang awam sekalipun yang tidak mengerti cara ngoding menggunakan tag html. Di lain pihak, format output XML masih dalam format yang menggunakan tag html meski nama dari tag tersebut merupakan hal custom. JSON bisa menjadi lebih ringkas juga jika data disimpan dengan bentuk array. 
3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Fungsi dari method is_valid() adalah untuk memvalidasi isi dari input user. Fungsi ini memastikan bahwa field yang wajib sudah diisi oleh user. Lalu juga memeriksa apakah data yang diisi sesuai dengan tipe yang diinginkan. Dalam fungsi ini juga ada cleaning data dimana ketika is_valid() == True, maka data akan di normalize dengan menggunakan method cleaned_data. Setelah diberishkan baru akan dapat diakses dan digunakan di dalam platform. Fungsi ini juga menangani eror dimana jika data tidak valid akan mengembalikan False beserta pesan kesalahan pada form pada tampilan pengguna. 
4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
CSRF token ditambahkan untuk memastikan bahwa setiap request yang dikirim ke aplikasi kita merupakan request secure, yang berasal dari pengguna asli. Hal ini dikarenakan bisa saja terjadi CSRF (Cross Site Request Forgery). Sehingga, dengan menggunakan csrf_token, setiap form akan memiliki token yang unik. 
Lebih mendalam, biasanya attackers akan coba untuk inject CSRF payload seperti ini : 
<form action:"https://example.com/password/change" method="POST">
  <input type="hidden" name="password" calue="changed_password" />
</form>
<script>
  document.forms[0].submit()
</script>
Ketika user visits this site, scriptnya bakal tereksekusi dan lead ke ngebuat request mengganti password dimana passwordnya terganti menjadi "changed_password"
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Menginstall tailwind css 
- Merombak ulang kode frontend (html dan css)
- Mengubah base.html sehingga ada block code 
- Mengganti main.html dan menambahkan header dan cards
- Menambahkan form add_product.html untuk menampilkan button
- Menambahkan settings.py ('Dirs': [BASE_DIR / 'templates'])
- Menambah id pada models.py memakai uuid (import)
- Melakukan migrasi setelah mengubah model 
- Membuat fungsi create_product_entry dengan memanggil fungsi is_valid() dan request method POST untuk memasukan hasil form ke database 
- Menambahkan fungsi show_main untuk mendefinisikan data form (Product.objects.all())
- Menambahkan semua URLS
- Debugging agar gambarnya muncul meski upload dari laptop dengan menambahkan : 
  MEDIA_URL = '/media/'
  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
  pada settings.py dan mengubahs setingan dari image di file html 
- Membuat semua fungsi XML dan JSON beserta XML Get By ID dan JSON Get By ID pada views.py lalu memanggilnya ke urls.py dan membuat pathnya
- Menggunakan postman untuk GET data
- git add ., git push, git pull, git commit. 
- Mengurus PWS (secret code, settings.py link)

-------------------------------------------------------------------------------------
Tugas 4 
Nama : Micheline Wijaya Limbergh 
NPM : 2306207013
Kelas : PBP D 

*Step by step mengerjakan :*
1. Menambahkan html untuk login dan register
2. Menambahkan import messages dan user creation form ke views.py 
3. Menambahkan fungsi register, login, dan logout di views.py
4. Buat urls
5. Restriksi akses ke halaman main dengan ngeimpor decorator login_required dan taro di atas fungsi show_main pada file views.py
6. Nampilin detail informasi kapan last login dengan nambahin last_login (fungsi show_main di file views.py) di context dan di render ke html.
5. Menghubungkan product dengan user dengan menambahkan kode : 
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   mengubah potongan create product supaya mencegah django ga langsung simpen ke database tapi di modifikasi dulu. 
  6. Ubah nama_pemilik menjadi username dari yang login di fungsi show_main pada views.py
  7. git add . git commit, git pull, git push
  8. Migrate models
  9. Tes apakah sudah bisa dengan membuat dua akun (regist)

*Apa perbedaan antara HttpResponseRedirect() dan redirect()*
  Perbedaannya hanya terletak pada bagaimana penulisan url dari setiap page. 
  Ketika menggunakan HttpResponseRedirect(), harus menuliskan lengkap pathnya 
  Contoh : return HttpResponseRedirect('/home/add_list/')
  Ketika menggunakan redirect(), bisa nulis lengkap atau menggunakan nama dari URL 
  pattern yang ada di urls.py (web dinamis), lalu bisa juga menggunakan objek 
  sehingga secara otomatis diarahkan ke halaman yang sesuai dengan objek itu. 
  Contoh : return redirect('home:add_list')

*Jelaskan cara kerja penghubungan model Product dengan User!*
  Menggunakan ForeignKey yang menunjukkan antara produk dengan pengguna. ForeignKey 
  ini ada di field user. user = models.ForeignKey(User, on_delete=models.CASCADE). 
  Field itu ditambahkan di model Product sehingga tiap product akan terkait dengan 
  pengguna sehingga jika akun pemilik terhapus, data product juga akan terhapus. Kita
   akan ambil dan menambilkan product yang hanay dimiliki oleh sang user dengan 
   menggunakan filter. Product.objects.filter(user=request.user)

*Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.*
  Authentication --> ngecek atau verifikasi pengguna saat login
  Authorization --> nention hak akses setelah pengguna berhasil login. Batasan apa atau sejauh mana yang boleh dilakukan oleh pengguna. 
  Django meriksa username dan pass lalu menandai pengguna sebagai authenticated jika berhasil, menggunakan session pula untuk mengecek status. Django mengelola autentikasi dengan django.contrib.auth dan batasin akses pengguna menggunakan dekorator @login_required. 

*Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?*
Django mengingat menggunakan session ID. Jadi pengguna yang login dengan session cookies akan disimpen ID nya di browser sehingga tiap kali ada request, mereka bisa dikenali. Cookies juga bisa digunain kalo ada web belanja dimana ada tombol keranjang. Meski belom login, biasanya tombol keranjang masih bekerja dan user masih dapat melihat barang apa saja yang sudah mereka simpan. Tidak semua cookies aman karena jika tidak terenkripsi atau rentan terhadap serangan XSS dan CSRF bisa berakhir pada data breach.