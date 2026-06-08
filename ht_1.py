#pip install os
#pip install streamlit
from pathlib import Path
import streamlit as st
from streamlit_local_storage import LocalStorage
#st.markdown(""
#    .main {
#        background-color: #0a0a2e;
#        color: white;
#    }
#)
#file_path = Path("desktop", "cpp", "ht") / "ht.png"
st.title("site1")
file_path = Path("ht.png")
st.write('view')
#if file_path.exists():
#    st.write('exist')

#else:
#    st.write('errorrr')

view = [1, 2, 3, 4, 5]
view
file_content = file_path.read_bytes()

#with open(file_path, "rb") as file:
#    file_content = file.read()

st.download_button(
    label="Download image",
    data=file_content,
    file_name="ht.png",
    mime="image/png",
    )
localS.setItem("site1", "done")

st.link_button("For more  information:", "https://www.science.org/")