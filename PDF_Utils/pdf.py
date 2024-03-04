import PyPDF2
from io import BytesIO

def extract_text_from_pdf(uploaded_file):
    try:
        # Read the PDF file from the uploaded file
        pdf_data = BytesIO(uploaded_file.read())

        # Initialize an empty string to store extracted text
        extracted_text = ""

        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_data)

        # Iterate through all pages and extract text
        for page_num in range(len(pdf_reader.pages)):
            # Use reader.pages[page_number] instead of reader.getPage(pageNumber)
            page = pdf_reader.pages[page_num]
            extracted_text += page.extract_text()

        return extracted_text

    except Exception as e:
        return f"Error during PDF extraction: {str(e)}"
