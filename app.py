import streamlit as st
from PyPDF2 import PdfReader
from gtts import gTTS
import os

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to convert text to speech
def text_to_speech(text, output_filename):
    tts = gTTS(text)
    tts.save(output_filename)
    return output_filename

# Streamlit UI
st.title("PDF to Audio Converter")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Extract text from the uploaded PDF
    text = extract_text_from_pdf(uploaded_file)
    
    # Show extracted text for verification (optional)
    st.text_area("Extracted Text", text, height=300)
    
    # Convert the text to speech
    if st.button("Convert to Audio"):
        with st.spinner("Converting..."):
            output_filename = "output.mp3"
            audio_file = text_to_speech(text, output_filename)
            st.success("Conversion complete!")
            
            # Provide a download button for the audio file
            with open(audio_file, "rb") as file:
                st.download_button(
                    label="Download Audio",
                    data=file,
                    file_name=output_filename,
                    mime="audio/mp3"
                )
