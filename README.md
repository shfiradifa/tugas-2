## Situs Web: [https://firtix.adaptable.app](https://firtix.adaptable.app)

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
