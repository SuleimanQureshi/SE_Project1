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

st.title("Active Job Listings")
with st.container():
    with stylable_container(
        key="container_with_border",
        css_styles="""       
            {
                border: 1px solid rgba(49, 51, 63, 0.2);
                border-radius: 0.5rem;
                padding: calc(1em - 1px)
                width: 100%;
                padding: 10px;
                background-color: #D9D9D9;
                border-radius: 10px;
                display: flex;
                justify-content: space-between;
            }
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
        with stylable_container(
        key="container_with_border",
        css_styles="""       
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
            
            """,):col5, col8 = st.columns([60,60])
        with col5:
            st.title("Job Title A")
            st.write("Location: Karachi, Pakistan")
            st.write("Minimum Qualification: Bachelors")
            st.write("Minimum Experience: 3 years")
        with col8:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            if st.button("View Job Description", key = "d"):
                st.switch_page("pages/job_desc.py")
            
        with stylable_container(
        key="container_with_border",
        css_styles="""       
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
            
            """,):col5, col8 = st.columns([60,60])
        with col5:
            st.title("Job Title B")
            st.write("Location: Moscow, Russia")
            st.write("Minimum Qualification: Masters")
            st.write("Minimum Experience: 1 year")
        with col8:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            if st.button("View Job Description", key = "B"):
                st.switch_page("pages/job_desc.py")
            
            
        with stylable_container(
        key="container_with_border",
        css_styles="""       
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
            
            """,):col5, col8 = st.columns([60,60])
        with col5:
            st.title("Job Title C")
            st.write("Location: Toronto, Canada")
            st.write("Minimum Qualification: Certification")
            st.write("Minimum Experience: Fresh Candidate")
        with col8:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            if st.button("View Job Description", key = "C"):
                st.switch_page("pages/job_desc.py")



with st.container():
    with stylable_container(
        key="container_with_borderd",
        css_styles="""       
            button {
                padding: 1px 48px;
                background-color: #8A8383;
                color: white;
                border: none;
                border-radius: 3px;
                cursor: pointer;
                font-size: 16px;
                float: right;
            }
            
            """,
    ):
        if st.button("View Past Job Offerings",use_container_width=True):
                st.switch_page("pages/past.py")