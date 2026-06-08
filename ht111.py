#pip install streamlit-local-storage
#pip install streamlit
from pathlib import Path
import streamlit as st
#from streamlit_local_storage import LocalStorage
st.write("view")
st.markdown("""
<style>
section[data-testid="stSidebar"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)
#localS = LocalStorage()



st.title("이미지 컬렉션 이벤트")
