import streamlit as st
import time

st.set_page_config(layout="wide")

c1, c2 = st.columns(2)
with c1:
    st.image("WhatsApp Image 2024-11-01 at 09.39.47.jpeg")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.link_button('🚨 Cek Daftar Barang Lartas', 'https://www.insw.go.id/intr', type="secondary", help="Lartas adalah singkatan dari Larangan dan Pembatasan, yaitu barang yang dibatasi atau dilarang dalam kegiatan ekspor dan impor. Pemerintah mengawasi ketat barang-barang Lartas dan mengharuskan izin khusus untuk perdagangan internasional.", use_container_width=True)

    with col2:
        st.link_button("Simulasi Biaya Ekspor","https://insw.go.id/intr/simulasi", type="secondary", use_container_width=True)

    with col3:
        st.link_button("Peraturan UMKM dan Ekspor","https://insw.go.id/intr/peraturan", type="secondary", use_container_width=True)
    
 
with c2:
    st.subheader('Dokumen Umum persyaratan ekspor')
    invoice = st.checkbox("Invoice")
    if invoice:
        st.code(f"""
                harus memuat: 
                Nomor dan tanggal invoice
                nama barang, harga per unit barang & total harga,
                nama dan alamat eksportir
                nama dan alamat importir
                keterangan rekening pembayaran
                dibuat menggunakan kop surat perusahaan eksportir
        """)
 
    PL = st.checkbox("Packing list")
    if PL:
        st.code(f"""
                Packing List harus berisi:
                nama barang
                nomor dan tanggal packing list
                jumlah kemasan dalam satuan (pack, pieces, ikat, kaleng, karton, karung, dll)
                berat bersih
                berat kotor
        """)

    BL = st.checkbox("Bill of Landing (B/L)")
    if BL:
        st.code(f"""
                Bukti pengiriman barang atau tanda terima yang dibuat oleh shipping company untuk eksportir. 
                B/L dikeluarkan setelah kapal berangkat dari Indonesia
                B/L dapat dipergunakan sebagai kepemilikan barang. 
                Eksportir yang memegang B/L adalah pemilik barang yang disebutkan dalam dokumen.
        """)
    
    PEB = st.checkbox("Pemberitahuan Ekspor Barang")
    if PEB:
        st.code(f"""
                Merupakan surat pemberitahuan yang dibuat oleh eksportir kepada bea dan cukai.
                Pembuatan PEB dapat dilakukan sendiri oleh eksportir atau diwakilkan forwarder.
        """)
        st.link_button("Belum memiliki PEB / BC 3.0? buat disini","https://portal.beacukai.go.id/portal/login", type="primary")
    
    
    SI = st.checkbox("Shipping Instruction")
    if SI:
        st.code(f"""
                Merupakan dokumen yang dibuat dan diberikan oleh eksportir kepada forwarder atau 
                shipping company untuk melakukan booking pada container dan ruang di kapal/pesawat.
                Dokumen ini biasanya bisa dikirim melalui email.
        """)

    COO = st.checkbox("Certificate of Origin (COO) atau Surat Keterangan Asal (SKA)")
    if COO:
        st.code(f"""
                Merupakan dokumen yang menerangkan bahwa barang yang diekspor berasal dari Indonesia.
        """)
        st.link_button("Belum memiliki COO / SKA? buat disini","http://ska.kemendag.go.id/", type="primary")
    
    COA = st.checkbox("Certificate of Analysis (COA)*")
    if COA:
        st.caption('khusus hasil industri kimia atau hasil pertanian')
        st.code(f"""
                Dokumen ini berisi hasil analisis dari produk yang diekspor.
                Dokumen COA dapat diminta dari pihak produsen atau diurus langsung sendiri oleh eksportir melalui labolatorium independen yang sudah terakreditasi.
        """)

    PC = st.checkbox("Phytosanitary Certificate*")
    if PC:
        st.caption('khusus produk pertanian, hewan dan ikan')
        st.code(f"""
                Dokumen ini menjadmin produk yang dieksport bebas dari kuman penyakir berupa jamur dan bakteri. 
                Dokumen ini diurus dan dikeluarkan oleh kantor Balai Karantina Pertanian yang terdapat di setiap pelabuhan ekspor atau bisa di kantor perwakilannya di beberapa kota.
        """)

    

st.subheader('Cek validitas dokumen ekspor')

s1, s2 = st.columns(2)
with s1:
    uploaded_file = st.file_uploader("Upload Dokumen")
    if uploaded_file is not None:
        # To read file as bytes:
        # bytes_data = uploaded_file.getvalue()
        # st.write(bytes_data)

        # # To convert to a string based IO:
        # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        # st.write(stringio)

        # # To read file as string:
        # string_data = stringio.read()
        # st.write(string_data)

        option = st.selectbox(
        "Pilih jenis dokumen yang diupload",
        ("Invoice", "Packing list", "Bill of Landing (B/L)"),
        )


with s2:
    _LOREM_IPSUM = """

     openai.error.RateLimitError: You exceeded your current quota, please check your plan and billing details.
    """

    def stream_data():
        for word in _LOREM_IPSUM.split(" "):
            yield word + " "
            time.sleep(0.02)
    if uploaded_file is not None:
        if st.button("Cek validitas dokumen"):
            st.write_stream(stream_data)