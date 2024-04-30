import streamlit as st
from PIL import Image
from numpy import asarray
import streamlit.components.v1 as components
from streamlit_extras.stylable_container import stylable_container 

if st.button("Back"):
    st.switch_page("main.py")

st.title("Company Overview")

st.markdown("""
<style>     
.element-container:has(#button-after)  + div button {
 padding: 10px 20px;
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

with stylable_container(
    key="container_with_border",
    css_styles="""
        {
            border: 1px solid rgba(49, 51, 63, 0.2);
            border-radius: 0.5rem;
            padding: calc(1em - 1px)
            width: 100%;
            padding: 10px;
            background-color: #dddddd;
            border-radius: 10px;
            display: flex;
            justify-content: space-between;
        },
        
        button {
            padding: 1px 48px;
            background-color: #459AFF;
            color: orange;
            border: none;
            border-radius: 3px;
            cursor: pointer;
            font-size: 16px;
            float: right;
        }
        
        """,
):
        st.write("""
                 ## About us
                  """)
        st.write("Welcome to XYZ Enterprises! We're more than just a company; we're a community of passionate individuals dedicated to making a difference in the world of technology.")
        st.write("At XYZ Enterprises, our mission is simple: to revolutionize the way people access information.")
st.markdown("""
<style>     
.element-container:has(#button-after)  + div button {
 padding: 10px 20px;
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

with stylable_container(
    key="container_with_border",
    css_styles="""
        {
            border: 1px solid rgba(49, 51, 63, 0.2);
            border-radius: 0.5rem;
            padding: calc(1em - 1px)
            width: 100%;
            padding: 10px;
            background-color: #dddddd;
            border-radius: 10px;
            display: flex;
            justify-content: space-between;
        },
        
        button {
            padding: 1px 48px;
            background-color: #459AFF;
            color: orange;
            border: none;
            border-radius: 3px;
            cursor: pointer;
            font-size: 16px;
            float: right;
        }
        
        """,
):
        st.write("""
                ## Company info
                """)
        st.write("At Tech Innovations Inc., we're pioneering the future of technology with our innovative solutions and innovative products. With a team of passionate and skilled professionals, we're dedicated to pushing the boundaries of what's possible in the digital landscape.")
        st.write("Our company culture fosters creativity, collaboration, and continuous learning. We believe in empowering our employees to unleash their full potential and thrive in a dynamic and supportive environment. From developers to designers, marketers to project managers, every member feels part of the team. ")
        
        
st.write("""
            # Media Wall
            """)
image = Image.open('stonk.jpeg')
sronk = asarray(image)
image = Image.open('happy.jpg')
img = asarray(image)
image = Image.open('happ2.jpg')
img2 = asarray(image)
image = Image.open('succ.jpeg')
succ = asarray(image)
col5, col6, col7, col8 = st.columns([60,60,60,60])

with col5:
    st.image(sronk, width=120)
with col6:
    st.image(img, width=130)
with col7:
    st.image(img2, width=130)
with col8:
    st.image(succ, width=130)