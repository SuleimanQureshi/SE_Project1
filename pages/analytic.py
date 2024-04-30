import streamlit as st
from PIL import Image
from numpy import asarray
import streamlit.components.v1 as components
from streamlit_extras.stylable_container import stylable_container 
with st.container():
    col3213, col321, col34, col444 = st.columns([20,40,40,60])
    with col3213:
        if st.button("Back", key="fsdahkfashjkaf"):
            st.switch_page("main.py")
image = Image.open('first.jpg')
first1 = asarray(image)

image = Image.open('thrid.jpg')
third = asarray(image)


image = Image.open('second.jpg')
sec = asarray(image)

image = Image.open('four.jpg')
four = asarray(image)
image = Image.open('f.jpg')
final = asarray(image)
first, second = st.columns(2)
with first:
    st.write("""
             ## Application Activity
             """)
    st.image(first1, width=250)
    
with second:
    st.write("""
             ## Top Applied Job
             """)
    st.image(sec, width=210)
    
a,b,c = st.columns(3)
with b:
    st.write("""
             ## Recruitment Analysis
             """)

first, second,x,z = st.columns(4)
with first:
    st.image(third, width=100)
    
with second:
    st.image(four, width=390)
    
    
first, second = st.columns(2)
with first:
    st.write("""
             ## Top Message Activity Jobs
             """)
    st.image(final, width=210)
    
with second:
    st.write("""
             ## Top Applied Job
             """)
    st.image(final, width=210)
    