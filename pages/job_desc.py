import streamlit as st
from PIL import Image
from numpy import asarray
import streamlit.components.v1 as components
from streamlit_extras.stylable_container import stylable_container 
with st.container():
    col3213, col321, col34, col444 = st.columns([20,40,40,60])
    with col3213:
        if st.button("Back", key="fsdahkfashjkaf"):
            st.switch_page("pages/jobs.py")

st.title("Job Description")
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
            
            """,
    ):
        st.title("Software Engineer")
        st.write("""Location: Karachi, Pakistan

Minimum Qualification: Bachelor's degree in Computer Science, Software Engineering, or related field.

Minimum Experience: 3 years of professional experience in software development.

Responsibilities:
Design, develop, and maintain software applications using modern programming languages and frameworks.
Collaborate with product managers, designers, and other stakeholders to define project requirements and specifications.
Write clean, efficient, and well-documented code following industry best practices.
Conduct code reviews, identify areas for improvement, and mentor junior team members.
Troubleshoot and debug issues, perform root cause analysis, and implement effective solutions.
Stay up-to-date with emerging technologies and trends in software development.

Requirements:
Bachelor's degree in Computer Science, Software Engineering, or related field.
Minimum of 3 years of professional experience in software development.
Proficiency in one or more programming languages such as Java, Python, C++, or JavaScript.
Strong understanding of software design principles, data structures, and algorithms.
Experience with web development frameworks (e.g., Spring Boot, Django, React) is a plus.
Excellent problem-solving skills and attention to detail.
Ability to work independently and collaboratively in a fast-paced environment.
Strong communication and interpersonal skills.""")