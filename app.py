import streamlit as st
from PIL import Image

from ocr_engine import extract_text
from medicine_extractor import extract_medicines
from schedule import create_schedule
from health_advice import get_health_advice
from chart_generator import generate_food_chart


# ---------------------------------
# PAGE CONFIGURATION
# ---------------------------------

st.set_page_config(
    page_title="AI Prescription Scanner",
    page_icon="💊",
    layout="centered"
)


# ---------------------------------
# TITLE
# ---------------------------------

st.title("💊 AI-Powered Prescription Scanner")

st.write(
    "Upload a doctor's prescription to extract "
    "medicine information, medication schedule, "
    "and general supportive health guidance."
)

st.divider()


# ---------------------------------
# IMAGE UPLOAD
# ---------------------------------

uploaded_file = st.file_uploader(
    "📸 Upload Prescription Image",
    type=["png", "jpg", "jpeg"]
)


if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.subheader("📷 Uploaded Prescription")

    st.image(
        image,
        caption="Uploaded Prescription",
        use_container_width=True
    )


    # ---------------------------------
    # SCAN BUTTON
    # ---------------------------------

    if st.button("🔍 Scan Prescription"):

        with st.spinner("Scanning prescription..."):

            # OCR
            extracted_text = extract_text(image)


        st.success("Prescription scanned successfully!")


        # ---------------------------------
        # EXTRACTED TEXT
        # ---------------------------------

        st.subheader("📄 Extracted Text")


        if extracted_text.strip():

            st.text_area(
                "OCR Result",
                extracted_text,
                height=250
            )


            # ---------------------------------
            # MEDICINE INFORMATION
            # ---------------------------------

            medicine_data = extract_medicines(
                extracted_text
            )

            st.divider()

            st.subheader("💊 Medicine Information")


            if not medicine_data.empty:

                st.dataframe(
                    medicine_data,
                    use_container_width=True,
                    hide_index=True
                )


                # ---------------------------------
                # MEDICATION SCHEDULE
                # ---------------------------------

                schedule_data = create_schedule(
                    medicine_data
                )

                st.divider()

                st.subheader("⏰ Medication Schedule")

                st.dataframe(
                    schedule_data,
                    use_container_width=True,
                    hide_index=True
                )


            else:

                st.warning(
                    "No medicine information could be "
                    "identified. Please verify the prescription manually."
                )


            # ---------------------------------
            # HEALTH ADVICE
            # ---------------------------------

            advice = get_health_advice(
                extracted_text
            )

            st.divider()

            st.subheader("🩺 Condition / Symptoms")

            st.info(
                advice["condition"]
            )


            # ---------------------------------
            # SUPPORTIVE FOOD
            # ---------------------------------

            st.subheader(
                "🥗 Supportive Food & Care"
            )

            st.write("### 🍎 Foods & Fluids")

            for food in advice["foods"]:

                st.write(
                    "• " + food
                )


            st.write("### 🛌 Self-Care")

            for care in advice["care"]:

                st.write(
                    "• " + care
                )


            # ---------------------------------
            # VISUAL CHART
            # ---------------------------------

            st.divider()

            st.subheader(
                "📊 Visual Supportive Recovery Guide"
            )

            chart = generate_food_chart(
                advice["condition"],
                advice["foods"],
                advice["care"]
            )

            st.image(
                chart,
                caption="General supportive food and self-care guide",
                use_container_width=True
            )


            # ---------------------------------
            # DISCLAIMER
            # ---------------------------------

            st.divider()

            st.warning(
                "⚠️ This application provides general supportive "
                "information and extracts information from the uploaded "
                "prescription. It does not diagnose diseases, prescribe "
                "medicines, or change dosage instructions. Always verify "
                "unclear prescription information with a doctor or pharmacist."
            )


        else:

            st.warning(
                "No readable text found. "
                "Please upload a clearer prescription image."
            )

            
