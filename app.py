import streamlit as st
from PIL import Image
from ocr_engine import extract_text

st.set_page_config(
    page_title="AI Prescription Scanner",
    page_icon="💊",
    layout="centered"
)

st.title("💊 AI Prescription Scanner")
st.write(
    "Upload a doctor's prescription to extract the written information."
)

st.divider()

uploaded_file = st.file_uploader(
    "📸 Upload Prescription Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.subheader("📷 Uploaded Prescription")
    st.image(
        image,
        caption="Prescription",
        use_container_width=True
    )

    if st.button("🔍 Scan Prescription"):

        with st.spinner("Reading prescription..."):

            extracted_text = extract_text(image)

        st.success("Prescription scanned successfully!")

        st.subheader("📄 Extracted Text")

        if extracted_text.strip():
            st.text_area(
                "OCR Result",
                extracted_text,
                height=250
            )
        else:
            st.warning(
                "No readable text found. Please upload a clearer image."
            )

        st.divider()

        st.subheader("💊 Medicine Information")
        st.info("Medicine extraction will be added in the next step.")

        st.subheader("⏰ Medication Schedule")
        st.info("Morning / Afternoon / Night schedule will be added next.")
