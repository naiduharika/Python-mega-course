import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Harika Naidu")
    content = """
    Hey there! I'm Harika, a passionate software developer with a penchant for backend development. Python is my 
    language of choice, but I'm also on a journey exploring GoLang. When I'm not immersed in coding, you can find me 
    diving into a good book, catching up on my favorite TV shows, or indulging in the rhythm of a volleyball game.
    Looking for a collaborative tech enthusiast with diverse interests? You've found one. Let's chat!
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built with Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")
