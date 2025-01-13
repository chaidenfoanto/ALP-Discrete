# Dokumentasi Tugas Implementasi Teori Graf dengan Python

## Biodata
**ALP Matematika Diskrit**  
Nama: Chaiden Richardo Foanto  
NIM: 0806022310023

## 1. Tujuan
Tugas ini bertujuan untuk mengimplementasikan konsep teori graf menggunakan bahasa pemrograman Python, termasuk operasi-operasi dasar seperti:
- Menambahkan simpul (nodes) dan sisi (edges).
- Visualisasi graf dengan bobot pada sisi.
- Perhitungan jalur terpendek.
- Analisis struktur graf seperti derajat simpul, minimum spanning tree (MST), eksentrisitas, dan lainnya.

## 2. Struktur File
- **GraphTheory.py**: Berisi kelas `GraphTheory` yang mengimplementasikan berbagai metode manipulasi dan analisis graf menggunakan pustaka `networkx` dan `matplotlib`.
- **main.py**: Berisi implementasi dari kelas `GraphTheory` untuk membuat graf, menambahkan simpul dan sisi, serta memvisualisasikan graf dan hasil analisis.

## 3. Penjelasan Kode

### **GraphTheory.py**
#### Kelas `GraphTheory`:
- Menggunakan pustaka `networkx` untuk representasi graf.
- Memiliki metode utama:
  - `add_node(node)`: Menambahkan simpul ke graf.
  - `add_edge(u, v, weight=1)`: Menambahkan sisi antara simpul `u` dan `v` dengan bobot.
  - `visualize_graph()`: Visualisasi graf dengan bobot pada sisi.
  - `shortest_path(start, end)`: Menghitung jalur terpendek berdasarkan bobot.
  - `visual_shortest_path(start, end)`: Visualisasi jalur terpendek pada graf.

#### Metode Tambahan:
- `degree_of_node(node)`: Menghitung derajat simpul.
- `is_connected()`: Memeriksa apakah graf terhubung.
- `minimum_spanning_tree()`: Menghitung Minimum Spanning Tree (MST).
- `all_pairs_shortest_paths()`: Menghitung semua pasangan jalur terpendek.
- `eccentricity_of_node(node)`: Menghitung eksentrisitas simpul (jika graf terhubung).

### **main.py**
- Membuat instance kelas `GraphTheory`.
- Menambahkan simpul dan sisi dengan bobot tertentu.
- Menampilkan visualisasi graf.
- Menghitung dan menampilkan jalur terpendek.
- Menampilkan analisis graf:
  - Derajat simpul.
  - Status apakah graf terhubung.
  - Minimum Spanning Tree (MST).
  - Eksentrisitas simpul tertentu.

## 4. Contoh Output

### Visualisasi Graf
Graf ditampilkan dengan simpul (nodes) berwarna biru dan bobot pada sisi (edges).

### Jalur Terpendek
Jalur terpendek antara simpul 1 dan 5:
```plaintext
Jalur: [1, 3, 5]
```

### Derajat Simpul
Derajat simpul 3:
```plaintext
Derajat simpul 3: 3
```

### Apakah Graf Terhubung?
```plaintext
Apakah graf terhubung?
True
```

### Minimum Spanning Tree (MST)
```plaintext
Minimum Spanning Tree (MST):
[(2, 4, {'weight': 2.7}), (3, 4, {'weight': 1.8}), (1, 3, {'weight': 3.2}), (3, 5, {'weight': 2.7})]
```

### Eksentrisitas Simpul
Eksentrisitas simpul 1:
```plaintext
Eksentrisitas simpul 1: 3
```

## 5. Cara Menjalankan Kode

1. Pastikan Python3 sudah terinstal.
2. Instal pustaka yang dibutuhkan:
    ```bash
    pip install networkx matplotlib
    ```
3. Jalankan program:
    ```bash
    python main.py
    ```
4. Hasil akan ditampilkan di terminal, dan graf akan divisualisasikan melalui jendela matplotlib.

## 6. Kesimpulan
Kode yang telah dibuat berhasil mengimplementasikan operasi-operasi teori graf menggunakan Python. Dengan menggunakan pustaka `networkx` dan `matplotlib`, graf dapat divisualisasikan, dianalisis, dan dimodifikasi secara efisien. Semua metode tambahan (derajat simpul, MST, eksentrisitas, dll.) berfungsi sesuai tujuan tugas.
