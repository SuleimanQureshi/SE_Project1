import streamlit as st
from PIL import Image
from numpy import asarray
import streamlit.components.v1 as components
with st.container():
    col3213, col321, col34, col444 = st.columns([20,40,40,60])
    with col3213:
        if st.button("Back", key="fsdahddddkfashjkaf"):
            st.switch_page("main.py")

st.title("Search")


image = Image.open('search3.jpg')
img1 = asarray(image)
image = Image.open('employee.jpg')
img = asarray(image)
#st.sidebar.success("")
col1, mid1, mid2  = st.columns([30,30,30])

with mid1:
    st.text_input(label="",placeholder="Search")
with mid2:
    st.write("")
    st.write("")
    st.image(img1,width = 45)
    
col1, mid1, mid2 ,col2 = st.columns([10,30,30,10])
with mid1:
    st.write("Bob 1 (99%)")
    st.image(img,width = 200)
    st.write("Bob 3 (92%)")
    st.image(img,width = 200)
    st.write("Bob 5 (86%)")
    st.image(img,width = 200)

with mid2:
    st.write("Bob 2 (93%)")
    st.image(img,width = 200)
    st.write("Bob 4 (90%)")
    st.image(img,width = 200)
    st.write("Bob 6 (85%)")
    st.image(img,width = 200)
    




col5, col6, col7, col8 = st.columns([60,60,60,60])

with col5:
    if st.button("Home",use_container_width=True):
        st.switch_page("main.py")
with col6:
    if st.button("Messages",use_container_width=True):
        st.switch_page("pages/messages.py")
with col7:
    if st.button("Search",use_container_width=True):
        st.switch_page("pages/search.py")
with col8:
    if st.button("Profile",use_container_width=True):
        st.switch_page("pages/profile.py")
