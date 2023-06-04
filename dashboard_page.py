import streamlit as st

# Halaman dashboard
def dashboard_page():
    st.title("Dashboard")
    st.write(f"Selamat datang di halaman dashboard, {st.session_state.username}!")
    st.write("Ini adalah konten dashboard.")

if __name__ == '__main__':
    dashboard_page()