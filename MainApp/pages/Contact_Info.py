import streamlit as st

st.header("Contact Info")

with st.form(key = "Mail_info"):
        email = st.text_input("Please enter your email Address")
        message = st.text_area("Please enter you query")
        button = st.form_submit_button("Submit")
if button:
    print(email,message)
print("hello")