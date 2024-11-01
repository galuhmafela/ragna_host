import streamlit as st

option = st.sidebar.selectbox(
    "Pilih Kategori UMKM",
    ("Kuliner", "Kesehatan", "Agribisnis", "Kerajinan Tangan", "Produk Kecantikan", "Digital"),
    index=None,
    placeholder="Silahkan pilih asistensi dengan spesialisasi diatas",
)

if option == "Kuliner":
    st.chat_message("assistant").write("Ada memilih asisten dengan spesialisasi khusus di bidang Kuliner")
    if prompt := st.chat_input("Say something"):
        st.chat_message("user").write(prompt)
        st.chat_message("assistant").write(f"Echo: {prompt}")

if option == "Kesehatan":
    st.chat_message("assistant").write("Ada memilih asisten dengan spesialisasi khusus di bidang Kesehatan")
    if prompt := st.chat_input("Say something"):
        st.chat_message("user").write(prompt)
        st.chat_message("assistant").write(f"Echo: {prompt}")

if option == "Agribisnis":
    st.chat_message("assistant").write("Ada memilih asisten dengan spesialisasi khusus di bidang Agribisnis")
    if prompt := st.chat_input("Say something"):
        st.chat_message("user").write(prompt)
        st.chat_message("assistant").write(f"Echo: {prompt}")

if option == "Kerajinan Tangan":
    st.chat_message("assistant").write("Ada memilih asisten dengan spesialisasi khusus di bidang Kerajinan Tangan")
    if prompt := st.chat_input("Say something"):
        st.chat_message("user").write(prompt)
        st.chat_message("assistant").write(f"Echo: {prompt}")

if option == "Produk Kecantikan":
    st.chat_message("assistant").write("Ada memilih asisten dengan spesialisasi khusus di bidang Produk Kecantikan")
    if prompt := st.chat_input("Say something"):
        st.chat_message("user").write(prompt)
        st.chat_message("assistant").write(f"Echo: {prompt}")
    
if option == "Digital":
    st.chat_message("assistant").write("Ada memilih asisten dengan spesialisasi khusus di bidang Digital")
    if prompt := st.chat_input("Say something"):
        st.chat_message("user").write(prompt)
        st.chat_message("assistant").write(f"Echo: {prompt}")