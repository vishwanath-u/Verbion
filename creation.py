from io import BytesIO
from fpdf import FPDF

def create_pdf(translated_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, translated_text)
    return pdf.output(dest="S").encode("utf-8")
