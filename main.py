import streamlit as st
from PIL import Image
from numpy import asarray
import streamlit.components.v1 as components
from streamlit_extras.stylable_container import stylable_container 

html_code1 = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello Rectangle</title>
    <style>
        .rectangle {
            width: 150px;
            height: 40px;
            border: 2px solid black;
            text-align: center;
            line-height: 36px;
        }
    </style>
</head>
<body>
    <div class="rectangle">
        <span>32</span>
    </div>
</body>
</html>
'''
html_code2 = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello Rectangle</title>
    <style>
        .rectangle {
            width: 150px;
            height: 40px;
            border: 2px solid black;
            text-align: center;
            line-height: 36px;
        }
    </style>
</head>
<body>
    <div class="rectangle">
        <span>35</span>
    </div>
</body>
</html>
'''
html_code3 = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello Rectangle</title>
    <style>
        .rectangle {
            width: 150px;
            height: 40px;
            border: 2px solid black;
            text-align: center;
            line-height: 36px;
        }
    </style>
</head>
<body>
    <div class="rectangle">
        <span>3</span>
    </div>
</body>
</html>
'''
html4 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Company Overview</title>
    <style>
        .container {
            width: 100%; /* Set width to 100% */
            padding: 20px;
            background-color: #dddddd;
            border-radius: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .button {
            padding: 10px 20px;
            background-color: #459AFF;
            color: orange;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        .button:hover {
        opacity: 0.8;
        }
        .spacer {
            margin-top: 20px; /* Add space between elements */
        }
    </style>
</head>
<body>
    <div class="spacer"></div> <!-- Spacer element -->
    <div class="container">
        <div>Company Overview</div>
        <button class="button" onclick="viewAndEdit()">View and Edit</button>
    </div>
    <script>
        function viewAndEdit() {
            // Call your function here
            console.log("View and Edit button clicked");
        }
    </script>
</body>
</html>
"""
html5 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Job Listing</title>
    <style>
        .container {
            width: 100%;
            padding: 20px;
            background-color: #dddddd;
            border-radius: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .button {
            padding: 10px 20px;
            background-color: #459AFF;
            color: orange;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        .button:hover {
        opacity: 0.8;
        }
        .spacer {
            margin-top: 20px; /* Add space between elements */
        }
    </style>
</head>
<body>
    <div class="spacer"></div>
    <div class="container">
    <div>Job Listings</div>
    <button class="button">View and Edit</button>
    </div>
</body>
</html>
"""

html6 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Analytical Insights</title>
    <style>
        .container {
            width: 100%;
            padding: 20px;
            background-color: #dddddd;
            border-radius: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .button1 {
            padding: 10px 48px;
            background-color: #459AFF;
            color: orange;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        .button1:hover {
        opacity: 0.8;
        }
        .spacer {
            margin-top: 20px; /* Add space between elements */
        }
    </style>
</head>
<body>
    <div class="spacer"></div>
    <div class="container">
        <div>Analytical Insights</div>
        <button class="button button1">View</button>
    </div>
</body>
</html>
"""

image = Image.open('user.jpg')
img = asarray(image)
#st.sidebar.success("")
col1, mid, col2 = st.columns([30,30,50])
with col1:
    st.image(img,width = 150)
with mid:
    st.write("""
            ## Employer Name
            Employer Description
            """)
st.markdown("""<hr style="height:10px;border:none;color:#EBAF15;background-color:#EBAF15;" /> """, unsafe_allow_html=True)
col3, mid2, col4 = st.columns([60,60,40])
with col3:
    st.write("Interested Candidates")
    #st.text_area(label="Output Data:", value="output", height=15)
    st.markdown(html_code1, unsafe_allow_html=True)

with mid2:
    st.write("Profile Views")
    st.markdown(html_code2, unsafe_allow_html=True)

with col4:
    st.write("Connections")
    st.markdown(html_code3, unsafe_allow_html=True)
st.markdown("""<hr style="height:10px;border:none;color:#EBAF15;background-color:#EBAF15;" /> """, unsafe_allow_html=True)

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
    col5, col6, col7, col8 = st.columns([60,40,40,60])
    with col5:
        st.write("")
        st.write("Company Overview")
    with col8:
        if st.button("View and Edit"):
            st.switch_page("pages/overview.py")

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
    col5, col6, col7, col8 = st.columns([60,40,40,60])
    with col5:
        st.write("")
        st.write("Job Listings")
    with col8:
        if st.button("View and Edit",key="job_listing"):
            st.switch_page("pages/jobs.py")

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
    col5, col6, col7, col8 = st.columns([60,40,40,45])
    with col5:
        st.write("")
        st.write("Analytical Insights")
    with col8:
        if st.button("View"):
            st.switch_page("pages/analytic.py")
st.write("\n")
st.write("\n")
st.write("\n")
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




