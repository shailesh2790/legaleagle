import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import io
from transformers import pipeline
import pytesseract

import pytesseract

# Replace the below path with the actual path where Tesseract-OCR is installed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to convert PDF page to image
def pdf_page_to_image(page):
    zoom = 2  # Increase resolution of the image
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    img = Image.open(io.BytesIO(pix.tobytes("png")))
    return img

# Function to extract text from PDF
def extract_text_from_pdf(pdf_document):
    document = fitz.open(stream=pdf_document.read(), filetype="pdf")
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        img = pdf_page_to_image(page)
        text += pytesseract.image_to_string(img)
    return text

# Load a pre-trained model for question-answering
question_answerer = pipeline("question-answering",framework="pt")

# Streamlit app layout
st.title('Legal Document Assistant')

# File uploader for PDF
uploaded_file = st.file_uploader("Upload a legal document (PDF)", type=["pdf"])

# Text input for the user's question
question = st.text_input("Enter your legal question")

# Button to get the answer
if st.button("Get Answer"):
    if uploaded_file is not None and question:
        # Extract text from the PDF
        extracted_text = extract_text_from_pdf(uploaded_file)

        # Get answer from the model
        answer = question_answerer(question=question, context=extracted_text)
        st.text_area("Answer", answer['answer'], height=150)
    else:
        st.error("Please upload a file and enter a question.")
