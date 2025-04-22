# import streamlit as st
# import base64
# from pathlib import Path
# import tempfile
#
#
# def writer():
#     file = st.file_uploader("选择待上传的PDF文件", type=['pdf'])
#     if st.button("点击"):
#         if file is not None:
#             with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
#                 fp = Path(tmp_file.name)
#                 fp.write_bytes(file.getvalue())
#                 with open(tmp_file.name, "rb") as f:
#                     base64_pdf = base64.b64encode(f.read()).decode('utf-8')
#                 pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" ' \
#                               f'width="800" height="1000" type="application/pdf">'
#                 st.markdown(pdf_display, unsafe_allow_html=True)
#
# writer()

import streamlit as st
import tempfile
import os


def main():
    st.title("PDF Viewer")

    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        # Save the uploaded file to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf", dir="static") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_file_path = tmp_file.name

        # Display the PDF file using a static file URL
        display_pdf(tmp_file_path)


def display_pdf(file_path):
    # Get the file name
    file_name = os.path.basename(file_path)

    # Create the URL for the static file
    file_url = f"static/{file_name}"

    # Embed the PDF in the Streamlit app
    pdf_display = f'<iframe src="{file_url}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


if __name__ == "__main__":
    # Ensure the static directory exists
    if not os.path.exists("static"):
        os.makedirs("static")

    main()






