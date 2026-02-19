import streamlit as st
import os
from dotenv import load_dotenv
from utils import *

def main():
    load_dotenv()  # Load environment variables

    st.set_page_config(page_title="PDF Summarizer")
    st.title("PDF Summarizing App")
    st.write("Summarize your PDF files in just a few seconds.")
    st.divider()

    pdf = st.file_uploader("Upload your PDF document", type="pdf")
    submit = st.button("Generate Summary")

    if submit:
        response = summarizer(pdf)

        st.subheader("Summary of the File:")
        st.write(response)

if __name__ == "__main__":
    main()
