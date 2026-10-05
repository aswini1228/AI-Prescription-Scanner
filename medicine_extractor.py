import re
import pandas as pd


def extract_medicines(text):
    """
    Extract possible medicine information from prescription text.
    """

    lines = text.split("\n")
    medicines = []

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # Dosage patterns like 500 mg, 10 mg, 5 ml
        dosage_match = re.search(
            r"\b\d+(?:\.\d+)?\s*(mg|ml|g|mcg)\b",
            line,
            re.IGNORECASE
        )

        dosage = dosage_match.group(0) if dosage_match else ""

        # Frequency keywords
        frequency = ""

        if re.search(r"\b(once|od|1-0-0)\b", line, re.IGNORECASE):
            frequency = "Once a day"

        elif re.search(r"\b(twice|bd|bid|1-0-1)\b", line, re.IGNORECASE):
            frequency = "Twice a day"

        elif re.search(r"\b(thrice|tds|tid|1-1-1)\b", line, re.IGNORECASE):
            frequency = "Three times a day"

        elif re.search(r"\b(0-0-1)\b", line):
            frequency = "Night"

        elif re.search(r"\b(1-0-0)\b", line):
            frequency = "Morning"

        # Duration
        duration_match = re.search(
            r"\b(\d+)\s*(days?|weeks?)\b",
            line,
            re.IGNORECASE
        )

        duration = duration_match.group(0) if duration_match else ""

        # Food instruction
        food_instruction = ""

        if re.search(r"before\s*food|before\s*meal", line, re.IGNORECASE):
            food_instruction = "Before food"

        elif re.search(r"after\s*food|after\s*meal", line, re.IGNORECASE):
            food_instruction = "After food"

        # Add line if it contains medicine-related information
        if dosage or frequency or duration:

            medicines.append({
                "Prescription Text": line,
                "Dosage": dosage,
                "Frequency": frequency,
                "Duration": duration,
                "Food Instruction": food_instruction
            })

    return pd.DataFrame(medicines)
