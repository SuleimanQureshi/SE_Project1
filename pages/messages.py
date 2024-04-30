import streamlit as st
from PIL import Image
from numpy import asarray
import streamlit.components.v1 as components
with st.container():
    col3213, col321, col34, col444 = st.columns([20,40,40,60])
    with col3213:
        if st.button("Back", key="fsdahddkfashjkaf"):
            st.switch_page("main.py")

st.title("Messages")


image = Image.open('employee.jpg')
img = asarray(image)
image = Image.open('user.jpg')
img2 = asarray(image)
#st.sidebar.success("")
col1, mid1, mid2 ,col2 = st.columns([30,20,30,30])
with mid1:
    st.image(img,width = 100)
with mid2:
    st.write("""
            ### Potential Employee Name
            """)
with st.container():
    with st.chat_message(name="human", avatar = img):
        st.write("We got a match through SwiftHire! Your company seems like an excellent fit for me. Let's talk details?")
    with st.chat_message(name="user", avatar = img2):
        st.write("Looking at your profile and skills. You would fit right in. Let's meet at Habib University for your interview. Kindly let me know if you would be available this Tuesday at 10:00 A.M.?")
    with st.chat_message(name="human", avatar = img):
        st.write("Thank you. The time works for me. Looking forward to working alongside your team.")

    #st.chat_message(name="user", message="moni")
    st.chat_input(placeholder="Your message")


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
