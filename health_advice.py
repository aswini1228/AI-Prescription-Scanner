def get_health_advice(text):
    """
    Provides general supportive food and self-care information.
    It does not diagnose or prescribe treatment.
    """

    text_lower = text.lower()

    advice = {
        "condition": "General health support",
        "foods": [
            "Drink adequate water and fluids",
            "Eat light, nutritious meals",
            "Include fruits and vegetables as tolerated"
        ],
        "care": [
            "Take adequate rest",
            "Follow the doctor's prescription exactly",
            "Monitor symptoms"
        ]
    }

    if "fever" in text_lower or "temperature" in text_lower:
        advice = {
            "condition": "Fever",
            "foods": [
                "Water and other suitable fluids",
                "Light nutritious meals",
                "Fruits and vegetables as tolerated",
                "Easy-to-digest foods"
            ],
            "care": [
                "Take adequate rest",
                "Stay hydrated",
                "Follow the prescribed medicines",
                "Monitor temperature and symptoms"
            ]
        }

    elif "cold" in text_lower or "cough" in text_lower:
        advice = {
            "condition": "Cold / Cough symptoms",
            "foods": [
                "Warm fluids",
                "Light nutritious foods",
                "Fruits and vegetables as tolerated",
                "Adequate fluids"
            ],
            "care": [
                "Take adequate rest",
                "Stay hydrated",
                "Follow the prescription",
                "Monitor symptoms"
            ]
        }

    elif "stomach" in text_lower or "gastric" in text_lower:
        advice = {
            "condition": "Stomach-related symptoms",
            "foods": [
                "Light and easy-to-digest foods",
                "Adequate fluids",
                "Small meals if comfortable"
            ],
            "care": [
                "Take adequate rest",
                "Follow the prescribed instructions",
                "Avoid foods that worsen your symptoms"
            ]
        }

    return advice
