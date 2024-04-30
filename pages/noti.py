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

st.title("Notifications")
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
        st.markdown("<h1 style='text-align: center; color: black;'>Updates & Notifications</h1>", unsafe_allow_html=True)
        st.markdown("""<hr style="height:10px;margin-left: auto; margin-right: auto;border:none;border-width:color:#EBAF15;background-color:#EBAF15;" /> """, unsafe_allow_html=True)
        st.write("New security patch available for download – keep your systems protected!")
        st.markdown("""<hr style="height:10px;margin-left: auto; margin-right: auto;border:none;border-width:color:#EBAF15;background-color:#EBAF15;" /> """, unsafe_allow_html=True)


        st.write("Important server maintenance scheduled for tonight – minimal downtime expected.")

        st.markdown("""<hr style="height:10px;margin-left: auto; margin-right: auto;border:none;border-width:color:#EBAF15;background-color:#EBAF15;" /> """, unsafe_allow_html=True)

        st.write("Join us for a virtual tech talk next Friday on AI advancements – RSVP now!")

        st.markdown("""<hr style="height:10px;margin-left: auto; margin-right: auto;border:none;border-width:color:#EBAF15;background-color:#EBAF15;" /> """, unsafe_allow_html=True)

        st.write("Upgrade your software to the latest version – unlock new features and enhancements!")
        st.markdown("""<hr style="height:10px;margin-left: auto; margin-right: auto;border:none;border-width:color:#EBAF15;background-color:#EBAF15;" /> """, unsafe_allow_html=True)


        st.write("Reminder: Quarterly cybersecurity training session tomorrow – don't miss out on vital security tips!")
        st.markdown("""<hr style="height:10px;margin-left: auto; margin-right: auto;border:none;border-width:color:#EBAF15;background-color:#EBAF15;" /> """, unsafe_allow_html=True)

        st.write("Limited-time offer: Get 20% off on our premium subscription plan – upgrade now and save!")

        st.markdown("""<hr style="height:10px;margin-left: auto; margin-right: auto;border:none;border-width:color:#EBAF15;background-color:#EBAF15;" /> """, unsafe_allow_html=True)


        st.write("Mark your calendars: Company-wide town hall meeting next week – stay informed about important updates and initiatives!")
        st.markdown("""<hr style="height:10px;margin-left: auto; margin-right: auto;border:none;border-width:color:#EBAF15;background-color:#EBAF15;" /> """, unsafe_allow_html=True)


        st.write("Exciting news: We're hiring! Check out our career opportunities and join our dynamic team today!")
        st.markdown("""<hr style="height:10px;margin-left: auto; margin-right: auto;border:none;border-width:color:#EBAF15;background-color:#EBAF15;" /> """, unsafe_allow_html=True)


        st.write("Check out our latest blog......")


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
