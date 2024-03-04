from io import BytesIO
from reportlab.pdfgen import canvas

def create_pdf(translated_text):
    pdf_data = BytesIO()

    # Create PDF with reportlab
    pdf_canvas = canvas.Canvas(pdf_data)
    pdf_canvas.setFont("Helvetica", 12)
    pdf_canvas.drawString(10, 800, translated_text)
    pdf_canvas.save()

    pdf_data.seek(0)
    return pdf_data.read()
