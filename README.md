## Situs Web: [https://shafira-ramadhina-tugas.pbp.cs.ui.ac.id](https://shafira-ramadhina-tugas.pbp.cs.ui.ac.id)

# TUGAS 2

## Cara Implementasi Checklist:

### Pembuatan Proyek Django Baru:

- **Step 1:** Mengaktifkan Virtual environment pada direktori baru.
- **Step 2:** Melakukan instalasi seluruh dependencies dalam virtual environment dengan query `pip install -r requirements.txt` menambahkan sejumlah query yang dibutuhkan di dalam file `requirements.txt`.
- **Step 3:** Buat proyek Django baru dengan nama "tugas2" menggunakan perintah `django-admin startproject tugas2`.

### Pembuatan Aplikasi "main" pada Proyek:

- **Step 1:** Memberikan izin akses untuk web app pada file `settings.py` dengan mengisi bagian `ALLOWED_HOST` dengan `"*"` dan tambahkan `'main'` ke dalam bagian `INSTALLED_APPS`.
- **Step 2:** Jalankan aplikasi main dengan query `python manage.py startapp main` untuk membuat aplikasi "main" pada direktori utama yang akan digunakan untuk mengelola proyek.

### Routing pada Proyek:

- **Step 1:** Untuk meneruskan pemrosesan request ke URL tingkat proyek, buat pemetaan untuk file `urls.py` pada bagian proyek "tugas2" dengan mengimpor fungsi `include` dari `django.urls` dan menambahkan query `path('main/', include('main.urls'))` dalam list path `urlpatterns`.

### Pembuatan Model pada Aplikasi "main":

- **Step 1:** Deklarasi atribut-atribut yang akan menjadi objek model yang dibutuhkan proyek dalam file `models.py` dengan tipe data yang sesuai. Setidaknya terdapat variable "name" dengan tipe data CharField, amount dengan tipe data IntegerField, dan descriptioin dengan tipe data TextField. Model ini berguna untuk menyimpan data dan logika aplikasi.
- **Step 2:** Buat berkas migrasi untuk model yang telah diperbarui dengan menjalankan perintah `python manage.py makemigrations`.
- **Step 3:** Aplikasikan hasil migrasi ke database dengan menjalankan perintah `python manage.py migrate`.

### Pembuatan Fungsi pada views.py:

- **Step 1:** Untuk merender tampilan HTML dengan data dari model, impor `render` dari modul `django.shortcut`.
- **Step 2:** Deklarasikan fungsi `show_main` yang akan mengatur request HTTP, mengirimkan data ke tampilan yang diinginkan, dan merender tampilan dari file `main.html`.

### Pembuatan Routing pada urls.py Aplikasi "main":

- **Step 1:** Untuk mengatur rute URL khusus fitur-fitur dalam aplikasi "main", buat file `urls.py` pada direktori "main". Impor `path` dari modul `django.urls` dan fungsi `show_main` dari modul `main.views` untuk mendefinisikan pola URL dan menentukan tampilan yang akan ditampilkan saat URL diakses.

### Deployment ke Adaptable:

- **Step 1:** Sebelum melakukan deployment, pastikan template HTML telah diimplementasi dengan baik dan melakukan testing django untuk memeriksa apakah code program yang dibuat sudah berjalan sesuai yang diinginkan. Apabila telah sesuai, lakukan add, push, dan commit proyek ke repository GitHub. Saat ini aplikasi telah berjalan dalam lokal.
- **Step 2:** Untuk menjalankan aplikasi yang dapat diakses secara online melalui internet, lakukan deployment aplikaso django pada platform hosting yang dalam hal ini adalah Adaptable.io dengan langkah pertama adalah pembuatan akun yang terhubung dengan akun GitHub
- **Step 3:** Buat aplikasi baru yang dihubungkan dengan repository GitHub yang berisi proyek tugas2. Kemudian sesuaikan template deployment, tipe basis data, python version, dan start command sesuai dengan yang digunakan. Setelah itu beri nama aplikasi sesuai yang diinginkan, dalam hal ini adalah "firtix".
- **Step 4:** Tunggu proses deployment hingga selesai dan peroleh situs web yang dapat diakses secara online.

### Bagan Request Client ke Web Aplikasi Berbasis Django:
- **Bagan:**
            Client's Web Browser
                    |
                    v
        Django Web Application
                    |                    
    urls.py <-------+--------->  views.py
                |                   |
                v                   v
            models.py           main.html
- **Penjelasan:**
Client membuat request ke DJango dengan mengakses URL melalui sebuah web browser. Kemudian, request tersebut diteruskan ke **urls.py** untuk di-mapping ke fungsi view yang sesuai. Selanjutnya, fungsi view akan memproses request dan mengakses data yang diperlukan dari **models.py**. Setelah data diperoleh, fungsi view akan mengirimkan respon ke client dalam bentuk HttpResponse. HttpResponse ini akan di-render menggunakan berkas HTML yang sesuai. Dalam proses ini, **urls.py** bertanggung jawab untuk menghubungkan URL yang diakses oleh client dengan fungsi view yang akan memproses request tersebut, **views.py** bertanggung jawab untuk memproses request dan merender **main.html** dengan data dari **models.py** dan mengirimkan respon ke client dalam bentuk HttpResponse, serta **models.py** bertanggung jawab untuk mengakses data yang diperlukan oleh fungsi view sehingga dapat ditampilkan pada web browser milik client.

## Mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment sangat berguna ketika kita membutuhkan dependencies yang berbeda-beda antara project satu dengan lainnya yang berjalan pada satu sistem operasi yang sama. Dalam pengembangan aplikasi web berbasis Django, virtual environment sangat diperlukan karena setiap proyek Django memiliki kebutuhan dependencies yang berbeda-beda. Dengan menggunakan virtual environment, kita dapat mengisolasi dependencies yang dibutuhkan oleh setiap proyek Django sehingga tidak akan terjadi konflik antar dependencies.
Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, sangat disarankan untuk menggunakan virtual environment karena dapat membantu menghindari masalah dependencies yang berkonflik dan memudahkan dalam manajemen dependencies.

## Apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya?
MVC, MVT, dan MVVM adalah pola arsitektur perangkat lunak yang digunakan untuk memisahkan tanggung jawab visualisasi, pemrosesan, dan manajemen data pada aplikasi UI.

### MVC (Model-View-Controller)

MVC merupakan pola arsitektur yang paling umum digunakan dengan tiga Komponennya, yaitu Model, View, dan Controller. Komponen **Model** yang akan menentukan jenis data dan logika bisnis, mengambil dan memanipulasi data, berkomunikasi dengan controller, berinteraksi dengan database, serta memperbarui view. Komponen **View** yang akan menampilkan data ke pengguna dan menyediakan berbagai komponen representasi data. Sedangkan, komponen **Controller** yang akan memanipulasi model dan merender view dengan menjadi jembatan antar keduanya.

### MVT (Model-View-Template)

MVT merupakan pola arsitektur yang serupa juga dengan MVC. MVT bermanafaat sebagai pemisah tugas agar kode program lebih terstruktur dan mudah dikelola. Dengan MVT, kode dapat digunakan kembali di berbagai bagian aplikasi lainnya dan strukturnya yang memungkinkan pengembangan paralel untuk tiap-tiap komponen sangat mendukung skalabilitas. Tiga komponen yang digunakan dalam MVT adalah Model, View, dan Template. Komponen **Model** yang bertugas menangani data dan logika aplikasi. Komponen **View** bertugas menerima permintaan HTTP dan mengembalikan respons HTTP. Sementara, komponen **Template** bertugas menentukan tampilan UI yang akan digunakan untuk merender data.

### MVVM (Model-View-ViewModel) 

MVVM merupakan pola arsitektur yang menekankan pada pemisahan logika presentasi dari logika bisnis. Tiga komponen yang digunakan dalam MVVM adalah Model, View, dan ViewModel. Komponen **Model** bertanggung jawab menentukan jenis data dan logika bisnis. Komponen **View** bertanggung jawab atas interface grafis antar pengguna dan pola desain serta menampilkan output dari data yang telah diproses. Sedangkan, komponen **ViewModel** merupakan abstraksi dari **View** dan sebagai penyedia pembungkus data model untuk ditautkan. ViewModel terdiri dari Model yang diubah menjadi View, dan berisi query.

### Perbedaan antara MVC, MVT, dan MVVM

Perbedaan utama antar ketiganya terletak pada cara ketiganya mengatur dan memisahkan komponen dalam pengembangan perangkat lunak. MVC memisahkan aplikasi menjadi Model (data dan logika bisnis), View (tampilan), dan Controller (pengendali interaksi pengguna). MVT yang khususnya dalam kerangka kerja Django, memasukkan Template yang memisahkan tampilan dari logika pengendali, tetapi tidak memiliki pengendali interaksi yang eksplisit seperti MVC. MVVM menggunakan ViewModel sebagai perantara antara Model (data) dan View (tampilan), dengan ViewModel mengelola tampilan dan interaksi pengguna, memungkinkan pemisahan yang lebih kuat antara tampilan dan logika bisnis.

# TUGAS 3

## Perbedaan Form POST dan Form GET dalam Django

Dalam Django, terdapat dua metode untuk mengirim data dari client ke server: **POST** dan **GET**. Utamanya, perbedaan antar keduanya, yaitu:
- **POST**: Data dikirim dalam body request, sehingga menjadi lebih aman dan tidak terlihat di URL. POST biasanya digunakan untuk mengirim data yang sensitif seperti password dan informasi pribadi lainnya.
- **GET**: Data dikirim melalui URL, sehingga mudah dilihat dan diakses oleh orang lain. GET biasanya digunakan untuk mengambil data dari server.
Sehingga, penggunaannya akan bergantung pada tingkat keperluan keamanan dari jenis data yang akan dikirimkan.

## Perbedaan Utama antara XML, JSON, dan HTML dalam Konteks Pengiriman Data

Pengiriman data antar client dan server dapat menggunakan berbagai jenis format seperti, XML, JSON, dan HTML. Perbedaan utama antara ketiganya, yaitu:
- **XML**: Format penyimpan dan pengiriman datanya terstruktur. Format ini biasanya digunakan untuk mengirim data yang kompleks dan memiliki banyak atribut, sehingga mempermudah untuk data dipahami.
- **JSON**: Format pengirim datanya berbentuk objek. JSON ini lebih simple dan mudah dibaca oleh manusia jika dibandingkan dengan XML.
- **HTML**: Format ini biasa digunakan dalam pembuatan halaman web. HTML berfungsi untuk mengirim data yang ditampilkan pada halaman web.
Dari ketiga format tersebut, pemilihannya akan bergantung pada kebutuhan aplikasi dan jenis data yang akan ditransfer. Seperti, misalnya, JSON yang sering digunakan dalam pertukaran data antara aplikasi web modern.

## Mengapa JSON Sering Digunakan dalam Pertukaran Data antara Aplikasi Web Modern?

JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena beberapa keunggulannya. Jika dibandingkan dengan format lain seperti XML, JSON memiliki struktur data yang lebih ringan, sehingga server dapat mengambil dan mengolah data lebih efisien, yang mana hal tersebut sangat berguna dalam aplikasi web yang membutuhkan respons cepat. Dari segi keterbacaannya oleh manusia, format JSON menyajikan data yang lebih mudah dibaca oleh manusia dengan struktur datanya yang sederhana dan jelas. Dengan begitu, akan lebih mudah untuk dilakukan pengembangan secara manual ketika hal tersebut diperlukan. Selain itu, JSON sangat cocok untuk digunakan dalam aplikasi web modern yang sering menggunakan JavaScript. JSON dapat dengan mudah diproses dalam JavaScript. Penggunaannya akan memudahkan komunikasi data antar server dan browser, mendukung pemrosesan asinkron, dan mengoptimalkan kinerja aplikasi. Dalam era aplikasi web modern saat ini, berfokus pada kecepatan dan efisiensi. JSON dapat dikatakan sebagai format yang telah populer untuk pertukaran data antara client dan server dengan cepat dan efisien.

## Cara Implementasi Checklist:
Update: Dari progress minggu sebelumnya, saya menghapus **appName** dan **appDesc** serta menambah **amount** sebagai jumlah stock dari suatu item. Kemudian saya melakukan **migrate** ulang.

### 1. Routing dari `main/` ke `/`

Untuk menyesuaikan konvensi yang ada, dilakukan pengubahan routing dari `main/` ke `/` dengan mengganti path `main/` ke `' '` pada list urlpatterns yang ada di file `urls.py` dalam subdirektori **tugas2**.

### 2. Implementasi Skeleton sebagai Kerangka Views

Skeleton ini berfungsi sebagai kerangka views yang akan menjadikan kerangka dari situs web yang akan dibuat nantinya menjadi konsisten dan minim kemungkinan terjadinya redudansi. Implementasi ini dilakukan sebelum kita membuat form registrasi. Caranya adalah dengan membuat `base.html` dalam folder **templates** yang diletakan pada root folder. Kemudian meng-update isi dari `'DIRS'` pada file `settings.py` menjadi `[BASE_DIR / 'templates']`. Terakhir, update file `main.html` dengan meng-extend `base.html` yang telah dibuat. Pada bagian ini, saya menambahkan sejumlah code untuk meng-implementasikan style tampilan dari `main.html`, seperti warna background, format card, bentuk dan warna button, padding, tata letak, dan sebagainya.

#### Implementasi BONUS
Untuk mengimplementasikan fitur yang menampilkan informasi jumlah item yang telah ditambahkan, saya menambahkan code `<p class="item-count">Kamu menyimpan {{ products|length }} item pada aplikasi ini.</p>` pada `main.html`. Saya mengambil length dari product yang sebelumnya menyimpan seluruh object Product sebagai jumlah dari item yang telah tersimpan. Kemudian code `class="item-count"` yang saya tambahkan bertujuan untuk mengimplementasikan style CSS yang telah saya buat dalam `item-count` pada file yg sama.

### 3. Membuat Form Input Data dan Menampilkan Data Produk Pada HTML

Untuk membuat halaman form input data, pertama-tama dilakukan dengan membuat file `forms.py` pada direktori **main** yang akan berisikan struktur dari form. Buat class yang akan menyimpan setiap `Product` yang diinputkan sebagai object dari `Product` itu sendiri dengan fields yang terdiri dari `"name"`, `"price"`, `"description"`, dan `"amount"`. 
Kemudian, pada file `views.py` ditambahkan sejumlah import dan membuat fungsi `create_product` dengan parameter `request` dan fungsi `show_main`. Fungsi `create_product` digunakan untuk menyimpan input data form setelah divalidasi. Kemudian dikembalikan ke halaman `main`. Fungsi `show_main` akan menyimpan variable `name`, `class`, dan seluruh object `Product` dalam database kemudian di-render ke `main.html`. Setelah kedua file dibuat, di-import ke dalam file `urls.py` yang berada pada folder **main** dan ditambahkan path `path('create-product', create_product, name='create_product'),` dalam list `urlpatterns`.
Selanjutnya, untuk implementasikan pembuatan tampilan halaman create-product dalam file `create_product.html` yang diletakkan pada folder **templates** dalam folder **main**. Dalam file tersebut, fields form yang sebelumnya telah dibuat, ditampilakan dalam bentuk table dengan perintah `{{ form.as_table }}`. Kemudian saya membuat beberapa code untuk mengatur style tampilan halaman seperti serupa dengan style pada `main.html`. Terakhir, buat tampilan informasi products yang telah ditambahkan dalam bentuk sebuah tabel di `main.html` dan lakukan redirrect dari button `Add New Product` ke halaman form yang baru saja dibuat yaitu `create_product`.

### 4. Pengembalian Data dalam Bentuk XML dan JSON
#### XML
Untuk menampilkan data dalam format XML, buat sebuah fungsi dalam file `views.py` pada folder **main**, yang dalam penugasan ini diberi nama `show_xml`. fungsi ini akan menerima parameter `request` dan menyimpan seluruh data object Product dalam sebuah variable yang kemudian ditranslate menjadi format XML emnggunakan `serializers` untuk di-return dalam bentuk `HttpResponse`. Agar fungsi dapat berjalan, perlu ditambahkan import `serializers` dan `HttpResponse` dari modul django. Kemudian, untuk menampilkan data berdasarkan id, buat sebuah fungsi bernama `show_xml_by_id` yang berfungsi sama dengan fungsi sebelumnya namun dengan tambahan parameter `id`. Setelah itu, import kedua fungsi tersebut dalam file `urls.py` pada folder **main** dan tambahkan path `path('xml/', show_xml, name='show_xml'),` dan `path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id')` ke dalam list `urlpatterns`. Sampai step ini, kita sudah dapat melihat data dalam bentuk XML melalui http://localhost:8000/xml ataupun http://localhost:8000/xml/[id] untuk menampilkan hasilnya.

#### JSON
Untuk menampilkan data dalam format XML, hanya perlu melakukan langkah yang sama dengan XML dan disesuaikan dengan JSON seperti prnamaan fungsinya menjadi `show_json` dan `show_json_by_id`. Kemudian menambahkan import kedua fungsi tersebut pada file `urls.py` dalam folder **main** dan tambahkan pula path `path('json/', show_json, name='show_json'),` dan `path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),` ke dalam list `urlpatterns`. Setelah seluruh tahapan ini selesai, maka kita sudah dapat melihat hasilnya melalui http://localhost:8000/json ataupun http://localhost:8000/json/[id] untuk menampilkan data dari satu object saja berdasarkan id.

### 5. Add, Push, dan Commit ke GitHub

Sebagai tahap terakhir, setelah di-deploy seperti pada tugas minggu sebelumnya, push ke dalam repository GitHub menggunakan perintah berikut pada terminal:
```bash
git add .
git commit -m "<pesan_commit>"
git push -u origin main
```

## Dokumentasi Postman
### HTML
![Main Page](/documentations/postman_html_main.png)
![Main Page](/documentations/postman_html_create_product.png)

### XML
![XML Preview](/documentations/postman_xml.png)
![XML by ID Preview](/documentations/postman_xml_id.png)

### JSON
![JSON Preview](/documentations/postman_json.png)
![JSON by ID Preview](/documentations/postman_json_id.png)

# TUGAS 4

## Cara Implementasi Checklist:

### 1. Implementasi Fungsi Registrasi, Login, dan Logout

- **Step 1:** Pastikan sudah menjalankan virtual environment
- **Step 2:** Karena saya akan menggunakan fungsi `redirect` saat setelah berhasil melakukan register, maka saya mengimport fungsi `register` terlebih dahulu dari module `django.shortcuts`. Kemudian, agar memudahkan pembuatan form register, saya menggunakan template formulir bawaan dengan meng-import `UserCreationForm` dari module `django.contrib.auth.forms`. Selain itu, saya juga meng-import fungsi `messages` dari module `django.contrib` untuk menampilkan pesan informasi ketika berhasil register atau login. Semua import ini dilakukan di file `views.py` yang berada pada direktori **main**.
- **Step 3:** Pada file yang sama, saya membuat fungsi `register`, `login_user`, dan `logout_user` yang menerima parameter `request`. Pada fungsi **register**, pertama saya membuat `UserCreationForm` baru dari yang sudah di-import sebelumnya dengan memasukkan QueryDict berdasarkan input dari user pada `request.POST`. Kemudian, diperiksa validasi inputnya. Apabila valid, data yang diterima dari form tersebut disimpan dan dibuat menjadi satu akun. Setelah itu, akan muncul message ketika register berhasil dan di-redirect ke login page. Pada fungsi **login_user**, Pertama-tama username dan password yang diinput user diautentikasi. Apabila berhasil diautentikasi akan di-login sesuai akun user dan di-redirect ke main page. Apabila tidak akan keluar pesan informasi bahwa username atau password yang dimasukkan salah. Pada fungsi **logout_user**, apabila fungsi dipanggil akan langsung di-logout dari akun dan di-redirect ke login page.
- **Step 4:** Tahap selanjutnya adalah membuat file html untuk `register.html` dan `login.html` untuk menjalankan fungsinya untuk ditampilkan di web app. Kedua file diletakan pada direktori `main/templates` bersama dengan file `main.html` dan `create_product.html` yang sudah ada sebelumnya. 
- **Step 5:** Ketiga fungsi yang telah dibuat pada `views.py` di-import ke `urls.py` yang ada pada direktori `main` agar dapat dilakukan pemanggilan fungsi tersebut. Kemudian, saya menambahkan path untuk ketiga fungsi tadi ke dalam list `urlpatterns` pada file yang sama.

### 2. Restriksi Akses Halaman Main

Untuk mengatur agar pengguna diharuskan login dahulu sebelum memperoleh akses ke halaman main, dilakukan import `login_required` dari module `django.contrib.auth.decorators`. Kemudian tambahkan code `@login_required(login_url='/login')` tepat di atas fungsi `show_main` yang ada pada file `views.py` di direktori `main` yang mengartikan halaman main hanya dapat diakses oleh pengguna yang sudah login (terautentikasi).

### 3. Penggunaan Cookies
Untuk dapat melihat penggunaan cookies ketika mengakses halaman main, saya menambahkan data last login. Maka dari itu, perlu menambahkan module `datetime` pada file `views.py` di direktori `main`. Kemudian, perlu meng-update sebagian isi dari fungsi `login_user` dengan menambahkan code `response.set_cookie('last_login', str(datetime.datetime.now()))` di dalam conditional ketika data input login berhasil diautentikasi. Kemudian, perlu penambahan `'last_login': request.COOKIES['last_login'],` ke dalam variable `context` pada fungsi `main` yang ada di `views.py` di direktori `main`. Setelah itu juga menambahkan `response.delete_cookie('last_login')` dalam fungsi `logout_user` sebelum response tersebut di-return. Terakhir, baru dilakukan pemanggilan pada `main.html` berupa data last login. Cookie yang telah dibuat hanya akan bertahan sampai user melakukan logout.

### 4. Menghubungkan Model `Product` dengan `User`

Kita perlu menghubungkan setiap objek Product yang akan dibuat dengan pengguna yang membuatnya, agar pengguna yang sedang terotorisasi hanya akan melihat produk-produk yang telah dibuat sendiri. Untuk itu, tambahkan import `user` dari module `django.contrib.auth.models` pada file `models.py` di direktori `main`. Kemudian buat model `user = models.ForeignKey(User, on_delete=models.CASCADE)` pada model `Product` yang telah ada sebelumnya. Dengan begitu, satu produk dengan satu user akan terhubung melalui sebuah relationship dan setiap produk akan terasosiasikan dengan seorang user. Kemudian, sejumlah potongan code ditambahkan ke dalam fungsi `create_product` yang berguna untuk mencegah Django agar tidak langsung menyimpan objek yang telah dibuat dari form langsung ke database sehingga memungkinkan kita untuk memodifikasi objek tersebut terlebih dahulu sebelum disimpan ke database. Dalam kasus ini, kita akan mengisi field `user` dengan objek `User` dari return value `request.user` yang sedang terotorisasi untuk menandakan bahwa objek tersebut dimiliki oleh pengguna yang sedang login. Setelah itu, untuk menampilkan objek Product yang terasosiasikan dengan pengguna yang sedang login, perlu ditambahkan potongan code ke dalam fungsi `show_main` yang hanya akan mengambil `Product` yang dimana field `user` terisi dengan objek `User` yang sama dengan pengguna yang sedang login. Lalu, mengganti variable `name` menjadi `request.user.username`. Setelah selesai semua, tahap terakhir adalah melakukan migrasi model untuk menyimpan perubahan.

## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
 
`UserCreationForm` merupakan template formulir yang sudah disediakan oleh Django dan integrasi dengan Django. Template formulir ini berguna untuk memudahkan kita membuat formulir pembuatan akun pengguna tanpa harus membuat code manual. Formulir ini memiliki 3 field, yaitu username, password, dan konfirmasi password. 
**Kelebihan:** 
- Memberikan kemudahan pengaplikasian karena kita tidak perlu merancang coding-an dari awal.
- Adanya validasi bawaan sehingga input dapat diverifikasi secara otomatis dengan aturan yang telah ditetapkan.
- Walaupun sudah ada field dan aturan validasinya sendiri, kita juga dapat secara fleksibilitas melakukan kustomisasi seperti menambahkan field atau mengubah validasi yang ada.
**Kekurangan:**
- Meski fleksibilitas dalam kustomisasi termasuk ke dalam kelebihan, tetapi hal tersebut juga dapat menjadi kekurangan karena dalam penambahan atau pengubahan codenya juga bisa menjadi rumit
- Jika ingin membuat aplikasi dengan tingkat otentikasi yang lebih tinggi (seperti memerlukan input email, nomor telephone, dsb), mungkin form ini kurang cocok untuk digunakan.
- Tidak mendukung autentikasi sosial , seperti register menggunakan Google account misalnya. Untuk mengimplementasikan hal tersebut perlu dilakukan secara terpisah.

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

Authentication dan authorization adalah 2 hal berbeda yang berkaitan dengan keamanan pengguna. 
**Authentication** merupakan proses pemverifikasian identitas pengguna dengan memastikan entitas yang saat ini sedang mencoba mengakses sistem adalah diri mereka sendiri (yang telah di claim sebelumnya). Kemudian, outputnya adalah berupa entitas yang sudah diautentikasi, namun belum dipastikan mendapat izin atau tidaknya atas hak akses. Contoh dari penggunaan authentication adalah ketika kita melakukan login akun SIAK dengan menggunakan kata sandi.
Di sisi lain, **authorization** merupakan proses pemberian atau penolakan izin atas akses terhadap suatu data terhadap entitas yang telah diautentikasi. Output dari proses ini adalah berupa hak akses itu sendiri, seperti akses apa yang diperbolehkan atau tidaknya. Contoh penggunaan authorization adalah ketika kita membuka file gdocs yang hanya diberikan permission untuk diakses menggunakan email ui yang telah melewati autentikasi username dan password SIAK sebelumnya. 
Singkatnya, authentication yang akan bekerja memeriksa kredensial, sedangkan authorization bekerja memeriksa izin. Keduanya akan saling terlibat satu sama lain dalam mengamankan web app kita sehingga keduanya sangat penting.

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

Cookies adalah data atau informasi yang disimpan di komputer pengguna saat pengguna mengakses situs web. Tujuan penggunaannya bisa beragam, mulao dari menyimpan preferensi pengguna, mengelola sesi pengguna, hingga melacak aktivitas pengguna. Sesi pengguna dalam hal ini mengartikan bahwa cookies yang hanya berlaku selama sesi pengguna aktif dan akan terhapus ketika pengguna keluar dari situs, logout, atau menutup browser. Dengan adanya cookies, memungkinkan server web untuk mengingat pengguna dan informasi terkait pengguna ketika pengguna mengakses situs web kembali.
## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Penggunaan cookies dalam pengembangan web dapat aman secara default apabila digunakan dengan benar. Namun, jika penggunaannya tidak benar dapat menjadi risiko yang perlu dihindari. Seperti informasi sensitif yang meliputi kata sandi atau data pribadi lainnya yang tidak dienkripsi secara memadai akan berpotensi terhadap risiko keamanan data pengguna itu sendiri. Kemudian, apabila data telah tercuri, maka pengguna tidak dapat mengambil alih kembali akun pengguna. Selain dicuri, cookies ini juga dapat menjadi target serangan XSS (penyisipan script berbahaya). Untuk menghindarinya, sebaiknya pastikan dienkripsi dengan aman menggunakan HTTPS sehingga ketika melakukan pengiriman ookies dari klien ke server atau sebaliknya, data telah dienkripsi dengan baik dan aman secara default.

# TUGAS 5

## Manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya?

**Element Selector**
Element selector berguna untuk memberikan styling yang sama pada element-elemen sejenis, seperti misalnya mengganti font atau warna pada setiap teks dengan elemen paragraf `<p>`. Element selector digunakan ketika kita ingin menyeragamkan format untuk suatu jenis elemen.

**ID Selector**
ID Selector berguna untuk memberikan styling khusus (unik) pada elemen-elemen tertentu saja, seperti misalnya memberikan typhography khusus untuk sebuah teks berelemen paragraf `<p>` yang berbeda dengan teks dengan elemen `<p>` lainnya. ID selector digunakan ketika kita ingin memberi gaya khusus pada satu elemen spesifik.

**Class Selector**
Class selector berguna untuk memberikan styling yang sama pada sekelompok elemen, baik yang sama atau berbeda, seperti misalnya memberikan layout khusus seperti background-color dan padding untuk sekelompok elemen yang terdiri dari teks `<h1>`, `<p>`, dan `<table>`. Class selector digunakan ketika kita ingin mengelompokkan sejumlah elemen dengan gaya yang sama.

## HTML5 Tag

- **`<!DOCTYPE html>`:**
    Digunakan sebagai deklarasi versi HTML dalam dokumen untuk memberi tahu browser bahwa kita menggunakan HTML5. Dengan tag ini, kita memberikan panduan kepada komputer untuk memahami bagaimana struktur dokumen tersebut dirancang.
- **`<html>`:**
    Digunakan untuk menandai awal dan akhir dari dokumen HTML atau dengan kata lain menetapkan batas halaman.
- **`<nav>`:**
    Digunakan untuk mengelompokkan elemen untuk navigasi, seperti navbar.
- **`<head>`:**
    Berisi informasi meta atau informasi latar belakang terkait dokumen, misalnya seperti judul, karakter set, dan tautan ke stylesheet.
- **`<body>`:**
    Digunakan sebagai penandan area utama dimana konten dokumen HTML ditempatkan, seperti misalnya teks, gambar, tautan, atau elemen-elemen lainnya.
- **`<div>`:**
    Digunakan sebagai elemen penanda untuk mengelompokkan elemen-elemen HTML dan mengimplementasikan styling tertentu pada sekelomopk elemen tersebut.
- **`<title>`:**
    Digunakan untuk membuat judul dokumen yang nantinya akan muncul di judul browser pada tab.
- **`<ul>`, `<ol>`, `<li>`:**
    Digunakan untuk membuat daftar tak terurut (`<ul>`), daftar terurut (`<ol>`), dan item daftar (`<li>`).
- **`<h1>`/`<h2>`/`<h3>`/dst:**
    Digunakan untuk membuat teks dengan masing-masing ukurannya. Misalnya, `<h1>` untuk judul besar dan `<h2>` untuk judul yang sedikit lebih kecil, dan seterusnya.
- **`<p>`:**
    Digunakan untuk membuat paragraf teks.
- **`<a>`:**
    Digunakan untuk membuat tautan (hyperlink) ke halaman lain. Seperti misalnya ketika suatu button di-klik akan masuk ke halama lainnya bergantung pada hyperlink yang dicantumkan.
- **`<img>`:**
    Digunakan untuk meng-insert gambar dalam dokumen. Ada pula `<svg>` untuk meng-insert gambar dalam format `.svg`.
- **`<form>`:**
    Digunakan untuk membuat tampilan formulir, seperti dalam formulir login atau register.
- **`<input>`:**
    Digunakan untuk membuat berbagai jenis input, seperti teks, sandi, atau button. Masing-masingnya difungsikan dengan type tertentu.
- **`<footer>`:**
    Digunakan untuk membuat footer yang berisi informasi penutup di bagian akhir dari dokumen, seperti misalnya informasi hak cipta dan tautan ke halaman lain.


## Perbedaan antara margin dan padding

Box model pada CSS merupakan suatu box yang membungkus setiap elemen HTML yang terdiri dari content, padding, border, dan margin. Untuk perbedaan tersendiri antara **margin** dan **padding** terletak pada posisi area yang dikosongkan. Pada **padding**, kita akan memberi space untuk area sekitar (luar) content. Sedangkan pada **margin**, kita akan memberi space untuk area sekitar (luar) border.

## Perbedaan antara framework CSS Tailwind dengan Bootstrap dan kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

**Tailwind**
Framework CSS Tailwind membuat tampilan dengan pendekatan "utility-first" yang menggabungkan kelas-kelas utilitas yang telah didefinisikan sebelumnya. Dari segi ukuran file CSS, jika dibandingkan dengan Bootstrap, Tailwind mempunyai file CSS yang lebih kecil dan hanya akan memuat kelas-kelas utilitas yang ada. Tailwind CSS menawarkan fleksibilitas dan adaptabilitas tinggi terhadap proyek. Namun, Tailwind CSS memiliki pembelajaran yang lebih curam karena memerlukan pemahaman terhadap kelas-kelas utilitas yang tersedia dan bagaimana menggabungkannya untuk mencapai tampilan yang diinginkan.

**Bootstrap**
Framework CSS Bootstrap menggunakan gaya dan komponen yang telah didefinisikan, yang memiliki tampilan yang sudah jadi dan dapat digunakan secara langsung. Dari segi ukuran file CSS, jika dibandingkan dengan Tailwind, Bootstrap memiliki file CSS yang lebih besar karena termasuk banyak komponen yang telah didefinisikan. Tampilan yang dihasilkan dari Bootstrap cenderung lebih konsisten di seluruh proyek karena komponen yang digunakan telah didefinisikan. Untuk pembelajarannya, Bootstrap memiliki pembelajaran yang lebih cepat untuk pemula karena dapat mulai dengan komponen yang telah didefinisikan.

Pemilihan yang tepat antara keduanya bergantung pada kebutuhan spesifik proyek dan preferensi developer. Jika kita mengutamakan kecepatan pengembangan dan responsive design yang cepat, Bootstrap akan menjadi pilihan yang lebih tepat. Namun, jika kita mencari fleksibilitas dan kebebasan yang lebih besar dalam desain serta telah memahami lebih dalam terkait framework CSS, Tailwind mungkin akan menjadi pilihan yang lebih sesuai.

## Cara Implementasi Checklist:

### 1. Menambahkan Bootstrap ke Aplikasi
Agar dapat memudahkan saya ketika ingin menggunakan templates yang disediakan framework CSS dari Bootstrap ataupun Tailwind, saya memasukkan kedua meta tag di dalam `base.html`

### 2. Menambahkan navbar pada Aplikasi
Saya mengambil template navbar dari framework Bootstrap dan disesuaikan dengan nama aplikasi saya, kemudian terdapat 2 button yang mengarahkan ke halaman `dashboard` dan `inventory` serta button logout di sudut kanan navbar. 

### 3. Menambahkan Fitur Edit pada Aplikasi
Sama seperti fitu delete sebelumnya, saya membuat fungsi `edit_product` dengan parameter `request` untuk menjalankan fitur edit product di `views.py`. Kemudian, di-import ke dalam file `urls.py` pada direktori `main` dan menambahkan path url-nya ke dalam `urlpatterns` di file yang sama. Lalu, saya membuat file html baru di dalam folder `templates` di direktori `main` yang berisikan tampilan halaman edit product. 

### 4. BONUS: Memberikan warna yang berbeda pada baris terakhir dari item pada inventori menggunakan CSS
Saya mengimplementasikan ini dengan menambahkan `{% if forloop.last %}class="latest-product"{% endif %}` dalam tag `<tr>`. Kemudian, pada file `style.css` di direktori `main/static/main/` saya menambahkan class selector `lastest-product` untuk mengkustomisasi tampilan warna background-nya. 

### 5. Kustomisasi Desain CSS Web App
Sebelumnya, saya menambahkan 2 halaman web, yaitu `home.html` yang menjadi tampilan awal ketika membuka web dan `inventory.html` yang berisikan tampilan `main.html` pada tugas sebelumnya. Kemudian, halaman `main.html` saya ubah menjadi tampilan dashboard. Kedua halaman tersebut saya tambahkan dengan membuat fungsi di `views.py` dan di-import ke `urls.py` di direktori `main` serta menambahkan url pattern-nya pula. Saya juga menambahkan fitur jumlah total items yang ada di inventory pada tampilan `main.html`.

Untuk tampilan desain CSS-nya, saya membuat file `style.css` seperti dari tugas-tugas sebelumnya untuk membuat css style. Untuk navbar sendiri, saya menggunakan template dari Bootstrap dan disesuaikan dengan tampilan yang saya inginkan. Kemudian, untuk tampilan secara keseluruhannya pertama-tama saya membuat design di figma kemudian baru diimplementasikan di vscode dengan membuat element-element selector (banyaknya class selector) di `style.css`. Implementasinya dilihat dari inspect tampilan yang sudah saya buat di figma.

# TUGAS 6

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Perbedaan antara asynchronous programming dengan synchronous programming terletak pada sistem/urutan pengerjaannya, dimana tugas-tugas dalam **asynchronous programming** dijalankan secara paralel atau independen tanpa menunggu tugas lain selesai,  dalam **synchronous programming** membutuhkan tugas-tugas untuk dijalankan secara berurutan dan menunggu tugas sebelumnya selesai sebelum melanjutkan.
## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Paradigma event-driven programming adalah paradigma pemrograman yang berfokus pada reaksi terhadap peristiwa-peristiwa (event) yang terjadi di sistem, seperti klik mouse, tekan tombol, atau keyboard input. Salah satu contoh penerapannya pada tugas ini adalah memanggil fungsi `addProduct` dengan menggunakan `fetch` API untuk mengirim permintaan POST ke endpoint add_product_ajax dengan data formulir. Setelah itu, baru fungsi `refreshProducts` dijalankan untuk memperbarui tampilan produk tanpa perlu me-refresh seluruh halaman.
## Jelaskan penerapan asynchronous programming pada AJAX.
 Asynchronous programming pada AJAX diterapkan dengan menggunakan objek XMLHttpRequest atau Fetch API untuk mengirim dan menerima data dari server secara asinkron, tanpa mengganggu tampilan halaman web sehingga halaman web dapat diperbarui secara dinamis tanpa perlu me-refresh seluruh halaman. 
## Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
Fetch API dan jQuery AJAX digunakan untuk melakukan permintaan AJAX, tetapi ada beberapa perbedaan di antara keduanya. Secara umum, Fetch API lebih baru dan lebih sesuai dengan standar web, sedangkan jQuery AJAX lebih lama dan lebih bergantung pada library jQuery. Beberapa perbedaan lebih jelas antara keduanya adalah:
- Secara default, Fetch API tidak akan mengirim atau menerima cookie apa pun dari server, sehingga menghasilkan permintaan yang tidak terautentikasi apabila situs bergantung pada pemeliharaan sesi penggunanya (perlu menyetel opsi inisialisasi credentials untuk mengirim cookie). Sementara itu, jQuery AJAX akan mengirim cookie secara default, kecuali jika opsi xhrFields.withCredentials disetel menjadi false. 
- Fetch API memiliki metode bawaan untuk berbagai jenis data, seperti arrayBuffer, blob, formData, json, dan text. Sedangkan jQuery AJAX hanya memiliki metode bawaan untuk json, jsonp, script, text, dan xml.
- Fetch API mengembalikan Promise yang tidak akan ditolak pada status kesalahan HTTP, seperti HTTP 404 atau 500 misalnya. Sebaliknya, Promise akan terselesaikan secara normal dan hanya akan ditolak pada kegagalan jaringan atau jika ada yang mencegah permintaan selesai. Sedangkan jQuery AJAX akan menolak Promise jika responsnya bukan status sukses (200-299) atau jika terjadi kesalahan jaringan.
Menurut saya, teknologi mana yang lebih baik untuk digunakan bergantung pada preferensi dan kebutuhan project. Namun, apabila kita perhatikan trend pengembangan web sekarang, Fetch API menjadi pilihan yang lebih baik menurut saya pribadi karena lebih modern, lebih fleksibel, dan lebih sesuai dengan standar web.
## Cara Implementasi Checklist:
### 1. Mengubah kode cards data item agar dapat mendukung AJAX GET dan melakukan pengambilan task menggunakan AJAX GET


### 2. Membuat sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan item
Sebelumnya, saya mengahpus button `Add New product` pada tugas 5 dan menggantinya dengan button sesuai AJAX seperti berikut:
```html
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Add Book by AJAX</button>
```
Atribut `data-bs-toggle="modal"` akan membuka modal form secara pop-up dengan indikasi modal yang dibuka adalah yang memiliki ID `exampleModal` pada atribut `data-bs-target="#exampleModal"`. Untuk tampilan modal form tersebut, diimplementasi dengan kode berikut:
```html
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Product</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form id="form" onsubmit="return false;">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="name" class="col-form-label">Name:</label>
                        <input type="text" class="form-control" id="name" name="name"></input>
                    </div>
                    <div class="mb-3">
                        <label for="price" class="col-form-label">Price:</label>
                        <input type="number" class="form-control" id="price" name="price"></input>
                    </div>
                    <div class="mb-3">
                        <label for="description" class="col-form-label">Description:</label>
                        <textarea class="form-control" id="description" name="description"></textarea>
                    </div>
                    <div class="mb-3">
                        <label for="amount" class="col-form-label">Stock:</label>
                        <input type="number" class="form-control" id="amount" name="amount"></input>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Product</button>
            </div>
        </div>
    </div>
</div>
```
Untuk mendukung kode di atas, dibuat fungsi `addProduct` dalam bentuk kode script seperti berikut:
```html
<script>
    ...
    function addProduct() {
        fetch("{% url 'main:add_product_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(refreshProducts)

        document.getElementById("form").reset()
        return false
    }
    document.getElementById("button_add").onclick = addProduct
</script>
```
### 3. Membuat fungsi view baru untuk menambahkan item baru ke dalam basis data
Untuk menambahkan item baru ke dalam database, saya membuat fungsi baru, yaitu `add_product_ajax` dengan parameter `request` pada `views.py` yg akan menyimpan value `name`, `price`, `description`, dan `amount` pada request. Kemudian values tersebut disimpan ke dalam objek Product baru. Fungsi ini dibuat dengan kode berikut:
```html
@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        amount = request.POST.get("amount")
        user = request.user

        new_product = Product(name=name, price=price, description=description, amount=amount, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```
### 4. Membuat path `/create-ajax/` yang mengarah ke fungsi view yang baru dibuat dan mengubungkan form di dalam modal ke path `/create-ajax/`
Untuk menambahkan routing untuk fungsi `add_product_ajax`, dilakukan dengan menyisipkan path baru ke dalam `urlpatterns` pada file `urls.py` di direktori `main`. Path yang baru adalah sebagai berikut:
```html
path('create-product-ajax/', add_product_ajax, name='add_product_ajax')
```

### 5. Melakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar item terbaru tanpa reload halaman utama secara keseluruhan
Untuk me-refresh data produk secara asynchronous, dilakukan dengan membuat fungsi baru dalam bentuk kode script sebagai berikut:
```html
<script>
    ...
    async function refreshProducts() {
        document.getElementById("product_table").innerHTML = ""
        const products = await getProducts()
        let htmlString = `<tr>
            <th>Name</th>
            <th>Price</th>
            <th>Description</th>
            <th>Date Added</th>
        </tr>`
        products.forEach((item) => {
            htmlString += `\n<tr>
            <td>${item.fields.name}</td>
            <td>${item.fields.price}</td>
            <td>${item.fields.description}</td>
            <td>${item.fields.date_added}</td>
        </tr>` 
        })
        
        document.getElementById("product_table").innerHTML = htmlString
    }

    refreshProducts()
    ...
</script>
```
pada fungsi tersebut, `document.getElementById("product_table")` akan memperoleh elemen berdasarkan ID nya. Dalam hal ini, elemen yang dituju adalah tag <table> dengan ID `product_table` yang telah dibuat sebelumnya. Kemudian, `innerHTML = ""` akan mengosongkan isi child element dari elemen yang dituju. Lalu, setiap data diambil dari for each loop setiap productnya dengan `products.forEach((item))` menggunakan fungsi `getProducts()`. Kemudian, htmlString kita konkatenasi dengan data produk untuk mengisi tabel. Terakhir, `refreshProducts()` memungkinkan fungsi ini akan dipanggil setiap kali user membuka halaman web.

### 6. Melakukan perintah `collectstatic`
Untuk melakukan perintah `collectstatic`, hanya perlu menjalankan perintah `python manage.py collectstatic`.

### 7. Add, Push, dan Commit ke GitHub
Sebagai tahap terakhir, push ke dalam repository GitHub menggunakan perintah berikut pada terminal:
```bash
git add .
git commit -m "<pesan_commit>"
git push -u origin main
``` 