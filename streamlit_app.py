import streamlit as st
from PIL import Image

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="KPU Kabupaten Banjarnegara",
    page_icon="🗳️",
    layout="centered"
)

# --- Fungsi untuk Menampilkan Gambar ---
def load_image(image_path):
    """Mencoba memuat gambar, menangani error jika file tidak ditemukan"""
    try:
        return Image.open(image_path)
    except FileNotFoundError:
        st.error(f"Error: File gambar '{image_path}' tidak ditemukan. Pastikan ada di folder yang sama.")
        return None

# --- Judul dan Subjudul ---
st.title("🗳️ KOMISI PEMILIHAN UMUM")
st.header("KABUPATEN BANJARNEGARA", divider='blue')

# --- Tampilkan Gambar Logo ---
logo_path = 'logo_kpu.png'
logo = load_image(logo_path)

if logo:
    # Mengubah ukuran gambar agar tidak terlalu besar
    # Sesuaikan angka 400x200 sesuai proporsi logo Anda
    st.image(logo, caption='Logo KPU Banjarnegara', width=200)

# --- Informasi Selamat Datang ---
st.markdown("""
    ## Selamat Datang di Laman Resmi Kami
    
    Kami adalah penyelenggara Pemilihan Umum dan Pemilihan Kepala Daerah di wilayah Kabupaten Banjarnegara.
    
    **Tugas kami** adalah memastikan proses demokrasi berjalan jujur, adil, dan transparan.
    
    ---
""")

# --- Bagian Informasi Tambahan ---
with st.expander("Klik untuk Melihat Informasi Kontak"):
    st.markdown("""
        ### Kontak KPU Kabupaten Banjarnegara
        
        | Item | Detail |
        | :--- | :--- |
        | 🌐 **Website** | [banjarnegara.kpu.go.id](https://banjarnegara.kpu.go.id) |
        | 📧 **Email** | kpu.banjarnegara@gmail.com (Contoh) |
        | 📍 **Alamat** | Jl. Selamanik No. 10, Banjarnegara |
        | 📞 **Telepon** | (0286) xxxxxxx |
    """)

with st.expander("Klik untuk Melihat Visi & Misi"):
    st.markdown("""
        ### Visi KPU
        ... (Masukkan Visi KPU Banjarnegara di sini) ...
        
        ### Misi KPU
        1. ...
        2. ...
        3. ...
    """)

# --- Pesan Penutup ---
st.info("📣 Sukseskan Pemilu! Suara Anda Menentukan Masa Depan Bangsa.")