import streamlit as st
from send_email import send_email
from email.header import Header

st.header("Contact me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    topic = st.selectbox("What topic do you want to discuss",
                         ("Job Inquiries", "Project Proposals", "Other"))
    raw_message = st.text_area("Your message")

    subject = f"New Message from {user_email}"
    encoded_subject = Header(subject, "utf-8").encode()

    message = f"Subject: {encoded_subject}\n\n"\
              f"Sender: {user_email}\n"\
              f"Topic: {topic}\n"\
              f"{raw_message}"

    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully")
