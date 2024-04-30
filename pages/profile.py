import streamlit as st
from PIL import Image
from numpy import asarray
import streamlit.components.v1 as components
from streamlit_extras.stylable_container import stylable_container 
with st.container():
    col3213, col321, col34, col444 = st.columns([20,40,40,60])
    with col3213:
        if st.button("Back", key="fsdaddhkfashjkaf"):
            st.switch_page("main.py")

image = Image.open('user.jpg')
img = asarray(image)

col1, mid1, mid2 ,col2 = st.columns([30,50,20,30])
with col1:
    st.image(img,width = 100)
with mid1:
    st.write("""
            ## Employer Name
            """)
    st.write("Employer Description")
    st.markdown("""
        <style>     
        .element-container:has(#button-after)  + div button {
        padding: 1px 20px;
                    background-color: #459AFF;
                    color: orange;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 16px;
        }</style>
        <div id="button-2"></div>
        """, unsafe_allow_html=True)
        #st.markdown('<div id="button-2"></div>', unsafe_allow_html=True)
    st.markdown('<div id="button2"> </div> <span id="button-after"></span>', unsafe_allow_html=True)
    if st.button('Updates/Notifications'):
        st.switch_page("pages/noti.py")
with col2:
    st.markdown("""
        <style>     
        .element-container:has(#button-after)  + div button {
        padding: 1px 20px;
                    background-color: #459AFF;
                    color: orange;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 16px;
        }</style>
        <div id="button-2"></div>
        """, unsafe_allow_html=True)
        #st.markdown('<div id="button-2"></div>', unsafe_allow_html=True)
    st.markdown('<div id="button2"> </div> <span id="button-after"></span>', unsafe_allow_html=True)
    if st.button('Privacy Settings'):
        st.switch_page("pages/privacy.py")


image = Image.open('search3.jpg')
img1 = asarray(image)
image = Image.open('job.jpeg')
img = asarray(image)
image = Image.open('engineermaintenance.jpg')
img2 = asarray(image)
image = Image.open('job2.jpg')
img3 = asarray(image)
image = Image.open('cyb.jpg')
img4 = asarray(image)
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
    st.write("Robotics Engineer 23 matches")
    st.image(img,width = 200)
    st.write("Software Engineer 20 matches ")
    st.image(img3,width = 200)
    st.write("Accountant 10 matches")
    st.image(img3,width = 200)

with mid2:
    st.write("Cybersecurity 21 matches")
    st.image(img4,width = 200)
    st.write("Hiring Manager 12 matches")
    st.image(img3,width = 200)
    st.write("Maintenance Engineer 1 match")
    st.image(img2,width = 200)
    
    
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
