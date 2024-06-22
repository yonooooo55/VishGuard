import streamlit as st
from PIL import Image
import pytesseract

# Set Tesseract path if needed (only necessary if Tesseract is not in PATH)
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'

def ocr_image(image):
    text = pytesseract.image_to_string(image)
    return text

def main():
    st.title('OCR with Pytesseract and Streamlit')
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        st.write("")
        st.write("Extracted Text:")
        text = ocr_image(image)
        st.write(text)

if __name__ == '__main__':
    main()
