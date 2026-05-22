import streamlit as st 
from src.database.db import create_subject

@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.write("Enter the details of new Subject")
    subject_code = st.text_input("Subject Code", placeholder="CS101")
    sub_name = st.text_input("Subject Name", placeholder="Introduction to computer science")
    sub_section = st.text_input("Section", placeholder="A")

    if st.button("Create Subject Now", type="primary", width="stretch"):
        if subject_code and sub_name and sub_section:
            try:
                create_subject(subject_code.strip(), sub_name, sub_section, teacher_id)
                st.toast("Subject Created Successfully")
            except Exception as e:
                st.error(f"Error creating subject: {e}")
        else:
            st.warning("Please fill in all the fields to create a subject.")



