import streamlit as st
from PIL import Image
from numpy import asarray
import streamlit.components.v1 as components
from streamlit_extras.stylable_container import stylable_container 
with st.container():
    col3213, col321, col34, col444 = st.columns([20,40,40,60])
    with col3213:
        if st.button("Back", key="fsdahkfashjkaf"):
            st.switch_page("pages/profile.py")

image = Image.open('user.jpg')
img = asarray(image)
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(img, width = 200)
    st.write("""
            ## Employer Name
            # """)
    



col1, mid, col2 = st.columns([30,30,50])
with col1:
    st.write("""
         ### Username
         """)
st.write("""
         ### Website
         """)
st.write("""
         ### Bio
         """)

col3, mid2, col4 = st.columns([60,60,   10])
with col3:
    st.write("""
         ### Private Profile
         """)
    st.write("""
         ### Notifications
         """)
    st.write("""
         ### Receive Messages
         """)
with col4:
    st.write("")
    st.checkbox(label="",key="1",value=True)
    st.write("")
    st.checkbox(label="",key="23",value=True)
    st.write("")
    st.checkbox(label="",key="3",value=False)


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
