import streamlit as st
from request_image import get_content

nasa_content = get_content()
date = nasa_content['date']
st.header(nasa_content["title"])
st.image("image.png", caption=f"NASA Image of the day for {date}", use_column_width=True)

with st.sidebar:
    st.title("NASA image of the day")
    st.header("Explanation")
    st.write(nasa_content["explanation"])

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
