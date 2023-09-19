## Situs Web: [https://firtix.adaptable.app](https://firtix.adaptable.app)

# TUGAS 1

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
            models.py          items.html
- **Penjelasan:**
Client membuat request ke DJango dengan mengakses URL melalui sebuah web browser. Kemudian, request tersebut diteruskan ke **urls.py** untuk di-mapping ke fungsi view yang sesuai. Selanjutnya, fungsi view akan memproses request dan mengakses data yang diperlukan dari **models.py**. Setelah data diperoleh, fungsi view akan mengirimkan respon ke client dalam bentuk HttpResponse. HttpResponse ini akan di-render menggunakan berkas HTML yang sesuai. Dalam proses ini, **urls.py** bertanggung jawab untuk menghubungkan URL yang diakses oleh client dengan fungsi view yang akan memproses request tersebut, **views.py** bertanggung jawab untuk memproses request dan merender **items.html** dengan data dari **models.py** dan mengirimkan respon ke client dalam bentuk HttpResponse, serta **models.py** bertanggung jawab untuk mengakses data yang diperlukan oleh fungsi view sehingga dapat ditampilkan pada web browser milik client.

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

# TUGAS 2

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

### Routing dari `main/` ke `/`

Untuk menyesuaikan konvensi yang ada, dilakukan pengubahan routing dari `main/` ke `/` dengan mengganti path `main/` ke `' '` pada list urlpatterns yang ada di file `urls.py` dalam subdirektori **tugas2**.

### Implementasi Skeleton sebagai Kerangka Views

Skeleton ini berfungsi sebagai kerangka views yang akan menjadikan kerangka dari situs web yang akan dibuat nantinya menjadi konsisten dan minim kemungkinan terjadinya redudansi. Implementasi ini dilakukan sebelum kita membuat form registrasi. Caranya adalah dengan membuat `base.html` dalam folder **templates** yang diletakan pada root folder. Kemudian meng-update isi dari `'DIRS'` pada file `settings.py` menjadi `[BASE_DIR / 'templates']`. Terakhir, update file `main.html` dengan meng-extend `base.html` yang telah dibuat. Pada bagian ini, saya menambahkan sejumlah code untuk meng-implementasikan style tampilan dari `main.html`, seperti warna background, format card, bentuk dan warna button, padding, tata letak, dan sebagainya.

#### Implementasi BONUS
Untuk mengimplementasikan fitur yang menampilkan informasi jumlah item yang telah ditambahkan, saya menambahkan code `<p class="item-count">Kamu menyimpan {{ products|length }} item pada aplikasi ini.</p>` pada `main.html`. Saya mengambil length dari product yang sebelumnya menyimpan seluruh object Product sebagai jumlah dari item yang telah tersimpan. Kemudian code `class="item-count"` yang saya tambahkan bertujuan untuk mengimplementasikan style CSS yang telah saya buat dalam `item-count` pada file yg sama.

### Membuat Form Input Data dan Menampilkan Data Produk Pada HTML

Untuk membuat halaman form input data, pertama-tama dilakukan dengan membuat file `forms.py` pada direktori **main** yang akan berisikan struktur dari form. Buat class yang akan menyimpan setiap `Product` yang diinputkan sebagai object dari `Product` itu sendiri dengan fields yang terdiri dari `"name"`, `"price"`, `"description"`, dan `"amount"`. 
Kemudian, pada file `views.py` ditambahkan sejumlah import dan membuat fungsi `create_product` dengan parameter `request` dan fungsi `show_main`. Fungsi `create_product` digunakan untuk menyimpan input data form setelah divalidasi. Kemudian dikembalikan ke halaman `main`. Fungsi `show_main` akan menyimpan variable `name`, `class`, dan seluruh object `Product` dalam database kemudian di-render ke `main.html`. Setelah kedua file dibuat, di-import ke dalam file `urls.py` yang berada pada folder **main** dan ditambahkan path `path('create-product', create_product, name='create_product'),` dalam list `urlpatterns`.
Selanjutnya, untuk implementasikan pembuatan tampilan halaman create-product dalam file `create_product.html` yang diletakkan pada folder **templates** dalam folder **main**. Dalam file tersebut, fields form yang sebelumnya telah dibuat, ditampilakan dalam bentuk table dengan perintah `{{ form.as_table }}`. Kemudian saya membuat beberapa code untuk mengatur style tampilan halaman seperti serupa dengan style pada `main.html`. Terakhir, buat tampilan informasi products yang telah ditambahkan dalam bentuk sebuah tabel di `main.html` dan lakukan redirrect dari button `Add New Product` ke halaman form yang baru saja dibuat yaitu `create_product`.

### Pengembalian Data dalam Bentuk XML dan JSON
#### XML
Untuk menampilkan data dalam format XML, buat sebuah fungsi dalam file `views.py` pada folder **main**, yang dalam penugasan ini diberi nama `show_xml`. fungsi ini akan menerima parameter `request` dan menyimpan seluruh data object Product dalam sebuah variable yang kemudian ditranslate menjadi format XML emnggunakan `serializers` untuk di-return dalam bentuk `HttpResponse`. Agar fungsi dapat berjalan, perlu ditambahkan import `serializers` dan `HttpResponse` dari modul django. Kemudian, untuk menampilkan data berdasarkan id, buat sebuah fungsi bernama `show_xml_by_id` yang berfungsi sama dengan fungsi sebelumnya namun dengan tambahan parameter `id`. Setelah itu, import kedua fungsi tersebut dalam file `urls.py` pada folder **main** dan tambahkan path `path('xml/', show_xml, name='show_xml'),` dan `path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id')` ke dalam list `urlpatterns`. Sampai step ini, kita sudah dapat melihat data dalam bentuk XML melalui http://localhost:8000/xml ataupun http://localhost:8000/xml/[id] untuk menampilkan hasilnya.

#### JSON
Untuk menampilkan data dalam format XML, hanya perlu melakukan langkah yang sama dengan XML dan disesuaikan dengan JSON seperti prnamaan fungsinya menjadi `show_json` dan `show_json_by_id`. Kemudian menambahkan import kedua fungsi tersebut pada file `urls.py` dalam folder **main** dan tambahkan pula path `path('json/', show_json, name='show_json'),` dan `path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),` ke dalam list `urlpatterns`. Setelah seluruh tahapan ini selesai, maka kita sudah dapat melihat hasilnya melalui http://localhost:8000/json ataupun http://localhost:8000/json/[id] untuk menampilkan data dari satu object saja berdasarkan id.

### Add, Push, dan Commit ke GitHub

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