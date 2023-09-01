import streamlit as st


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with st.container():
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

with st.container():
    content2 = """
    Below you can find some of the apps I have built with Python. Feel free to contact me!
    """
    st.write(content2)
