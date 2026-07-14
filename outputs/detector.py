"""
=========================================================
detector.py

Automatically detects important columns in dialogue
datasets.

Author : Adhithya K
Project : Universal Character Dataset Generator
=========================================================
"""


# =========================================================
# Candidate column names
# =========================================================

CHARACTER_COLUMNS = [
    "Character Name",
    "Character",
    "Speaker",
    "speaker",
    "Name",
    "Actor",
    "character",
]

TEXT_COLUMNS = [
    "Dialogue",
    "dialogue",
    "Text",
    "text",
    "Utterance",
    "Sentence",
    "Line",
]

CHARACTER_ID_COLUMNS = [
    "Character ID",
    "CharacterID",
    "character_id",
]

CHAPTER_COLUMNS = [
    "Chapter ID",
    "Chapter",
    "Scene",
    "Episode",
    "scene",
]

PLACE_COLUMNS = [
    "Place ID",
    "Place",
    "Location",
    "Setting",
]

DIALOGUE_ID_COLUMNS = [
    "Dialogue ID",
    "DialogueID",
    "ID",
    "id",
]


# =========================================================
# Generic detector
# =========================================================

def detect_column(df, candidates):
    """
    Returns the first matching column.

    Parameters
    ----------
    df : pandas.DataFrame

    candidates : list

    Returns
    -------
    str or None
    """

    for column in candidates:

        if column in df.columns:

            return column

    return None


# =========================================================
# Detect all important columns
# =========================================================

def detect_columns(df):

    detected = {

        "character":

            detect_column(
                df,
                CHARACTER_COLUMNS
            ),

        "text":

            detect_column(
                df,
                TEXT_COLUMNS
            ),

        "character_id":

            detect_column(
                df,
                CHARACTER_ID_COLUMNS
            ),

        "chapter":

            detect_column(
                df,
                CHAPTER_COLUMNS
            ),

        "place":

            detect_column(
                df,
                PLACE_COLUMNS
            ),

        "dialogue_id":

            detect_column(
                df,
                DIALOGUE_ID_COLUMNS
            ),
    }

    return detected