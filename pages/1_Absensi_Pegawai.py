import streamlit as st
import datetime

# Judul untuk Halaman Absensi
st.title("👨‍💼 Menu Absensi Pegawai KPU Banjarnegara")
st.header("Rekam Kehadiran Harian")

# --- Form Absensi ---
with st.form("absensi_form"):
    st.markdown("### Formulir Absen")
    
    nik = st.text_input("Masukkan NIK Anda", max_chars=16)
    nama = st.text_input("Nama Lengkap")
    waktu_sekarang = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Pilihan Jenis Absen
    jenis_absen = st.radio(
        "Pilih Jenis Absen:",
        ('Absen Masuk', 'Absen Pulang', 'Absen Dinas Luar')
    )

    # Tombol Submit
    submitted = st.form_submit_button("Rekam Absensi")

    if submitted:
        if nik and nama:
            # --- PENTING: Simulasi Penyimpanan Data ---
            # Di sini adalah tempat Anda MENGIRIM DATA ke Google Sheets atau Database.
            
            # Tampilan hasil (Simulasi)
            st.success(f"Absensi **{jenis_absen}** berhasil direkam!")
            st.markdown(f"**NIK:** {nik}")
            st.markdown(f"**Nama:** {nama}")
            st.markdown(f"**Waktu:** {waktu_sekarang}")
            
            # Catatan untuk pengembangan
            st.warning("Data ini belum disimpan permanen. Perlu integrasi database cloud.")
        else:
            st.error("Mohon isi NIK dan Nama Anda.")

# --- Tampilan Data (Simulasi) ---
st.subheader("Rekap Absensi Hari Ini (Simulasi)")
st.info("Tampilan ini akan menampilkan data dari database cloud Anda.")
