import streamlit as st
import psycopg2
from dashboard_page_test import dashboard_page_test
from dashboard_page import dashboard_page

# Koneksi ke database PostgreSQL
conn = psycopg2.connect(
    host="127.0.0.1",
    database="your_database",
    user="your_username",
    password="your_password"
)

# Membuat cursor
cursor = conn.cursor()

# Fungsi untuk melakukan login
def login(username, password):
    query = "SELECT * FROM userlogin WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    return result

# Halaman login
def login_page():
    st.title("Login")
    with st.form(key='login_form'):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        if submitted:
            result = login(username, password)
            if result:
                st.success("Berhasil Verifikasi user! , mohon klik Login sekali lagi untuk masuk ke Dashboard")
                # Set session state
                st.session_state.logged_in = True
                st.session_state.username = username
            else:
                st.error("Login gagal. Silakan coba lagi.")

# Halaman dashboard untuk username 'admin'
def dashboard_page_admin():
    st.title("Dashboard - Admin")
    st.sidebar.title("Sidebar")
    choice = st.sidebar.selectbox("Pilih tampilan", ("Tampilan1", "Tampilan2"))
    if choice == "Tampilan1":
        dashboard_page()
    elif choice == "Tampilan2" :
        dashboard_page_test()
    if st.sidebar.button("Log Out"):
        # Log out dan reset session state
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.experimental_rerun()

# Halaman dashboard untuk username 'test'
def dashboard_page_usertest():
    st.title("Dashboard - Test")
    st.sidebar.title("Sidebar")
    #choice1 = st.sidebar.selectbox("Pilih tampilan", ("Tampilan4"))
    #if choice1 == "Tampilan4":
    dashboard_page_test()
    if st.sidebar.button("Log Out"):
        # Log out dan reset session state
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.experimental_rerun()

# Menjalankan aplikasi
def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = ""

    if st.session_state.logged_in:
        if st.session_state.username == "admin":
            dashboard_page_admin()
        elif st.session_state.username == "test":
            dashboard_page_usertest()
    else:
        login_page()

if __name__ == "__main__":
    main()
