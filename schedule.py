import pandas as pd


def create_schedule(medicine_data):
    """
    Create medication schedule only from clearly
    written prescription frequency instructions.
    """

    schedule = []

    for _, row in medicine_data.iterrows():

        medicine = row.get("Prescription Text", "")
        frequency = str(row.get("Frequency", ""))
        food = str(row.get("Food Instruction", ""))

        morning = "❌"
        afternoon = "❌"
        night = "❌"

        if frequency == "Morning":
            morning = "✅"

        elif frequency == "Night":
            night = "✅"

        elif frequency == "Once a day":
            morning = "✅"

        elif frequency == "Twice a day":
            morning = "✅"
            night = "✅"

        elif frequency == "Three times a day":
            morning = "✅"
            afternoon = "✅"
            night = "✅"

        schedule.append({
            "Medicine": medicine,
            "Morning": morning,
            "Afternoon": afternoon,
            "Night": night,
            "Food Instruction": food
        })

    return pd.DataFrame(schedule)
