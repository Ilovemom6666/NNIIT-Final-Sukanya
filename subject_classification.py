"""
This module contains the logic to infer the subject of a flashcard
based on rule-based keyword matching.
"""

def infer_subject(text: str) -> str:
    """
    Infers the subject of the flashcard based on keywords in the question text.

    Args:
        text (str): The question text from the flashcard.

    Returns:
        str: The inferred subject, e.g., "Physics", "Biology".
    """
    text = text.lower()
    keywords = {
        "Physics": [
            "force", "acceleration", "velocity", "newton", "gravity", "energy",
            "momentum", "mass", "friction", "power", "work", "thermodynamics",
            "electricity", "magnetism", "quantum", "wave", "motion"
        ],
        "Biology": [
            "photosynthesis", "cell", "organism", "plant", "enzyme", "mitochondria",
            "dna", "genetics", "evolution", "species", "habitat", "ecology",
            "respiration", "bacteria", "virus", "nucleus", "chromosome"
        ],
        "Chemistry": [
            "atom", "molecule", "reaction", "acid", "base", "compound",
            "electron", "ion", "bond", "periodic", "element", "catalyst",
            "oxidation", "reduction", "solution", "ph", "organic", "inorganic"
        ],
        "Math": [
            "algebra", "geometry", "equation", "derivative", "integral", "calculus",
            "function", "probability", "statistics", "matrix", "vector", "theorem",
            "logarithm", "sequence", "series", "limit", "trigonometry"
        ],
        "History": [
            "war", "revolution", "empire", "ancient", "medieval", "treaty",
            "colonial", "civilization", "kingdom", "dynasty", "constitution",
            "industrial", "battle", "president", "parliament", "government"
        ],
        "Geography": [
            "continent", "river", "mountain", "ocean", "climate", "desert",
            "volcano", "plateau", "island", "valley", "weather", "ecosystem",
            "latitude", "longitude", "earthquake", "terrain", "population"
        ]
    }
    
    for subject, terms in keywords.items():
        if any(word in text for word in terms):
            return subject
    return "General"