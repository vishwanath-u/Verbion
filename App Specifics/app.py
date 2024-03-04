

import streamlit as st

from Language_Utils.language import supported_languages
from PDF_Utils.pdf import extract_text_from_pdf
from Language_Utils.translate import translate
from PDF_Utils.creation import create_pdf

# Page-Config

st.set_page_config(page_title="SwapAI", page_icon="🌐", layout="wide")

# Page-Title
st.title("SwapAI 🌍")
st.subheader("Translate to your Comfort!")

st.sidebar.header("Options")

uploaded_file = st.sidebar.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    # PDF processing and text extraction
    original_text = extract_text_from_pdf(uploaded_file)

    # Display original text on the left
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original Text from PDF")
        st.write(original_text)

    # Language selection in the sidebar
    target_language = st.sidebar.selectbox("Select target language", list(supported_languages.keys()))

    # Translate text using the language code from the mapping
    target_language_code = supported_languages[target_language]
    translated_text = translate(original_text, target_language_code)

    # Display translated text on the right
    with col2:
        st.subheader("Translated Text")
        st.write(translated_text)

    # Create downloadable PDF using BytesIO
    if st.sidebar.button("Download Translated PDF"):
        pdf_data = create_pdf(translated_text)
        st.sidebar.download_button("Download Translated PDF", pdf_data, key="download_btn", file_name="translated_text.pdf")