AI-Powered Prescription Scanner & Medication Schedule Assistant

An AI-powered Streamlit application that scans a doctor's prescription image using OCR, extracts readable prescription information, identifies medicine-related instructions, creates a medication schedule, and provides general supportive food and self-care guidance.

 Live Application

Streamlit App:
Add your existing Streamlit app link here.

 Project Overview

Reading handwritten prescriptions can sometimes be difficult. This project uses Optical Character Recognition (OCR) to extract readable text from a prescription image and organize the information into an easy-to-understand format.

The application can:

-  Upload a prescription image
-  Extract text using OCR
-  Identify possible medicine-related information
- Extract dosage, frequency, duration, and food instructions when clearly available
-  Create a morning/afternoon/night medication schedule
-  Provide general supportive health information based on detected symptoms
-  Suggest general supportive foods and fluids
-  Provide basic self-care guidance
-  Generate a visual supportive food & care chart automatically

---

 Workflow

Doctor Prescription
        ↓
Upload Prescription Image
        ↓
Image Preprocessing
        ↓
OCR
        ↓
Extracted Text
        ↓
Medicine Information Extraction
        ↓
Medication Schedule
        ↓
Condition / Symptoms
        ↓
Supportive Food & Self-Care
        ↓
Visual PNG Chart

---

 Features

1.  Prescription Image Upload

Users can upload a prescription in:

- PNG
- JPG
- JPEG

2.  OCR-Based Text Extraction

The application uses EasyOCR to extract readable text from the uploaded prescription.

3.  Medicine Information Extraction

The system attempts to identify:

- Medicine-related prescription text
- Dosage
- Frequency
- Duration
- Food instructions such as before/after food

4.  Medication Schedule

Based on clearly written prescription instructions, the application creates a schedule for:

Time| Status
Morning| ✅ / ❌
 Afternoon| ✅ / ❌
 Night| ✅ / ❌

The application does not change or invent dosage instructions.

5.  General Health Guidance

The system checks the extracted text for common symptom-related keywords such as:

- Fever
- Cold
- Cough
- Stomach-related symptoms

It then provides general supportive information.

6.Supportive Food & Self-Care

The application provides general suggestions such as:

- Adequate fluids
- Light nutritious meals
- Fruits and vegetables as tolerated
- Adequate rest
- Following the doctor's prescription
- Monitoring symptoms

7. Automatic Visual Chart

The application automatically generates a visual PNG chart containing:

Condition / Symptoms → Supportive Foods & Fluids → Self-Care Tips

This makes the information easier to understand visually.

---

 Technologies Used

- Python
- Streamlit
- EasyOCR
- Pillow (PIL)
- OpenCV
- NumPy
- Pandas
- Regular Expressions

---

 Project Structure

AI-Prescription-Scanner/
│
├── app.py
├── ocr_engine.py
├── medicine_extractor.py
├── schedule.py
├── health_advice.py
├── chart_generator.py
├── requirements.txt
└── README.md

File Description

File| Purpose
"app.py"| Main Streamlit application
"ocr_engine.py"| Prescription OCR using EasyOCR
"medicine_extractor.py"| Extracts medicine-related information
"schedule.py"| Creates medication schedule
"health_advice.py"| Provides general supportive health guidance
"chart_generator.py"| Generates visual food & self-care chart
"requirements.txt"| Required Python packages

---

 Installation

Clone the repository:

git clone https://github.com/aswini1228/AI-Prescription-Scanner.git

Move into the project folder:

cd AI-Prescription-Scanner

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

---

 Requirements

streamlit
easyocr
opencv-python-headless
Pillow
numpy
pandas

---

 Future Enhancements

- Better handwritten prescription recognition
- Multi-language OCR support
- Improved medicine-name identification
- Medicine database integration
- More accurate prescription information extraction
- Voice-based medication reminders
- Downloadable medication schedule
- Improved visual health charts
- Mobile-friendly interface

---

 Medical Disclaimer

This project is intended for educational and informational purposes only.

It does not:

- Diagnose diseases
- Prescribe medicines
- Change medicine dosage
- Replace a doctor or pharmacist
- Guarantee that a food or self-care suggestion will cure a medical condition

OCR results may contain errors, especially with handwritten prescriptions. Always verify prescription details, medicine names, dosage, and timing with a qualified doctor or pharmacist.

The food and self-care section provides only general supportive guidance and should not be considered medical treatment.

---

 Author

Aswini S
B.Sc. Computer Science with Artificial Intelligence

🔗 Project Repository

https://github.com/aswini1228/AI-Prescription-Scanner
