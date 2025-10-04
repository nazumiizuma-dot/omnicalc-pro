# OmniCalc Pro (Delivered ZIP)

This is a ready-to-run prototype of **OmniCalc Pro** (FastAPI backend + React frontend).
Run locally with Docker Compose.

## Quickstart (Docker)
```bash
# extract zip and cd into folder
docker-compose up --build
```
- Backend: http://localhost:8000
- Frontend: http://localhost:5173

## Run tests
Backend:
```bash
cd backend
pytest -q
```

Frontend:
```bash
cd frontend
npm ci
npm run dev
```

## Notes
- No secrets are included.
- This prototype includes 10 calculator modules (see backend/app/calculators).
- For production hardening, follow README in repo.

---

### 🚀 Cara Menjalankan

#### 💻 1. Windows / Laptop

1. Pastikan sudah menginstal **Python 3.9+**  
2. Buka **Command Prompt** atau **PowerShell**  
3. Jalankan perintah berikut:
   ```bash
   git clone https://github.com/nazumiizuma-dot/omnicalc-pro.git
   cd omnicalc-pro
   pip install -r requirements.txt
   python main.py

🧮 Omnicalc Pro — Smart Calculation & Analysis Tool

🎯 Latar Belakang & Ide
Banyak orang, terutama pelajar dan mahasiswa, sering kesulitan melakukan perhitungan kompleks dengan cepat dan efisien. Mulai dari matematika dasar, konversi, hingga simulasi ekonomi kecil. Dari situ saya berpikir untuk membuat Omnicalc Pro, alat kalkulasi multifungsi berbasis Python dan web hybrid, yang bisa digunakan di laptop maupun Android.
Tujuannya sederhana: mempermudah kehidupan sehari-hari dan kegiatan belajar, sekaligus menunjukkan bagaimana Python bisa menjadi jembatan antara AI dan aplikasi praktis di dunia nyata.

🤖 Fitur Utama
Kalkulator Umum & Ilmiah berbasis Python
UI berbasis HTML/CSS + Script Integration
Optimized Modular System, bisa dikembangkan ke AI logic
Docker & Makefile untuk environment yang mudah dijalankan di Windows/Linux/Android (via Termux)
Ramah untuk pelajar dan tugas akademik

💡 Inspirasi
Proyek ini terinspirasi dari konsep “multi-tool” digital seperti Google Calculator dan WolframAlpha, tapi saya kembangkan dengan sentuhan personal dan open-source agar bisa digunakan semua orang tanpa biaya.

📦 Struktur Proyek (ringkas)
Omnicalc-Pro/
├── main.py
├── core/
│   ├── calculator.py
│   ├── converter.py
│   └── ...
├── web/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── Dockerfile
├── Makefile
└── README.md

#🚀 Cara Menjalankan

💻 1. Windows / Laptop
1. Pastikan sudah install Python 3.9+
> Download Python
2. Buka Command Prompt / PowerShell
3. Jalankan perintah berikut:
git clone https://github.com/nazumiizuma-dot/omnicalc-pro.git
cd omnicalc-pro
pip install -r requirements.txt
python main.py
4. Jika berbasis web, buka file index.html di browser

📱 2. Android (via Termux)
1. Install Termux dari F-Droid / Play Store
2. Jalankan:
pkg update && pkg upgrade
pkg install python git
git clone https://github.com/nazumiizuma-dot/omnicalc-pro.git
cd omnicalc-pro
pip install -r requirements.txt
python main.py
3. Untuk tampilannya, buka hasil localhost (jika berbasis web) via termux-open-url http://localhost:5000

3. Docker (Opsional)
Jika ingin test di environment bersih:
docker build -t omnicalc-pro .
docker run -it omnicalc-pro

4. Visual Studio Code (GUI Mode)
1. Buka folder project di VS Code
2. Pastikan Python extension aktif
3. Klik kanan main.py → Run Python File
4. Untuk mode web: tekan Go Live jika pakai ekstensi Live Server

💭 Catatan Pribadi
Saya tidak berencana mengembangkan proyek ini terus-menerus, karena fokus utama saya ada di bidang finance global, ekonomi makro–mikro, dan analisis sistem pasar dunia.
Proyek ini lebih seperti proof of concept—bahwa saya bisa membuat sesuatu yang fungsional, meskipun bukan prioritas utama saya.

Sedikit spoiler untuk masa depan—berdasarkan analisis saya:
Menjelang 2030, dunia pelan-pelan masuk ke fase perubahan besar—bukan cuma soal teknologi yang makin canggih, tapi juga tentang gimana manusia harus belajar beradaptasi biar nggak ketinggalan. Banyak pekerjaan yang dulu kelihatan aman sekarang mulai goyah karena otomatisasi dan AI yang terus berkembang. Profesi kayak data entry, kasir, resepsionis, customer service, telemarketer, operator pabrik, admin, akuntan junior, teller bank, sopir, kurir, analis data dasar, HRD operasional, fotografer produk, proofreader, penulis konten ringan, analis hukum pemula, jurnalis berita cepat, desainer grafis standar, editor video basic, call center, sampai guru bimbel online generik —semuanya diprediksi bakal tergantikan hampir 90% oleh sistem otomatis, robot, dan AI yang kerja lebih cepat, murah, dan jarang salah.

Tapi di sisi lain, justru muncul peluang baru buat mereka yang bisa mikir kreatif, peka sama manusia, dan nggak takut bereksperimen. Pekerjaan kayak peneliti AI, analis etika teknologi, pengembang sistem otonom, seniman digital, konselor mental, penulis kreatif, desainer pengalaman (UX), analis strategi global, atau profesi lintas bidang yang butuh human touch—semua itu bakal naik daun karena nggak bisa digantikan mesin.

Sayangnya, kemajuan ini datang bareng sisi gelapnya juga. Ekonomi global makin berat, pertumbuhan melambat, dan utang publik dunia hampir nyentuh total GDP global. Krisis air dan pangan makin terasa—gletser mencair, sawah kekeringan, irigasi kacau—sampai risiko gagal panen naik 4–5 kali lipat. Akibatnya, harga bahan pokok melonjak, kesenjangan sosial makin dalam, dan migrasi besar-besaran mulai nggak bisa dihindarin.

Intinya, 2030 bukan cuma soal siapa yang paling pintar pakai teknologi, tapi siapa yang paling cepat beradaptasi. Dunia bakal terus berubah, dan satu-satunya cara buat tetap bertahan adalah belajar, berevolusi, dan nggak berhenti jadi manusia di tengah dunia yang makin digital.
