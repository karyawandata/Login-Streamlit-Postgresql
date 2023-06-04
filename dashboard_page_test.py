import streamlit as st

# Halaman dashboard test
def dashboard_page_test():
    st.title("Dashboard")
    st.write(f"Selamat datang di halaman dashboard, {st.session_state.username}!")
    st.write("dashboard test.")

if __name__ == '__main__':
    dashboard_page_test()