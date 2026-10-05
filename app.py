import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="AI Prescription Scanner",
    page_icon="💊",
    layout="centered"
)

st.title("💊 AI Prescription Scanner")
st.write("Upload a doctor's prescription to extract the written information.")

st.divider()

uploaded_file = st.file_uploader(
    "📸 Upload Prescription Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.subheader("📷 Uploaded Prescription")
    st.image(image, caption="Prescription", use_container_width=True)

    if st.button("🔍 Scan Prescription"):

        st.info("OCR processing will be added next...")

        st.subheader("📄 Extracted Text")
        st.write("OCR result will appear here.")

        st.subheader("💊 Medicine Information")
        st.write("Medicine details will appear here.")

        st.subheader("⏰ Medication Schedule")
        st.write("Medication schedule will appear here.")
