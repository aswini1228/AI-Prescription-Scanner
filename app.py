import streamlit as st
from PIL import Image
from ocr_engine import extract_text
from medicine_extractor import extract_medicines

st.set_page_config(
    page_title="AI Prescription Scanner",
    page_icon="💊",
    layout="centered"
)

st.title("💊 AI Prescription Scanner")
st.write(
    "Upload a doctor's prescription to extract medicine information."
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

        with st.spinner("Scanning prescription..."):

            extracted_text = extract_text(image)

        st.success("Prescription scanned successfully!")

        # OCR TEXT
        st.subheader("📄 Extracted Text")

        if extracted_text.strip():

            st.text_area(
                "OCR Result",
                extracted_text,
                height=250
            )

            # MEDICINE EXTRACTION
            medicine_data = extract_medicines(extracted_text)

            st.divider()

            st.subheader("💊 Medicine Information")

            if not medicine_data.empty:

                st.dataframe(
                    medicine_data,
                    use_container_width=True,
                    hide_index=True
                )

            else:

                st.warning(
                    "No medicine information could be identified. "
                    "Please verify the prescription manually."
                )

        else:

            st.warning(
                "No readable text found. "
                "Please upload a clearer prescription image."
            )
