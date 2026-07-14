"""
=========================================================
loader.py

Loads and prepares datasets automatically.

Author : Adhithya K
Project : Universal Character Dataset Generator
=========================================================
"""

import os
import pandas as pd

from config import DATA_FOLDER
from detector import detect_columns


# ==========================================================
# Find every CSV inside data/
# ==========================================================

def find_csv_files():

    csv_files = []

    for file in os.listdir(DATA_FOLDER):

        if file.lower().endswith(".csv"):

            csv_files.append(
                os.path.join(DATA_FOLDER, file)
            )

    return csv_files


# ==========================================================
# Read every CSV
# ==========================================================

def load_all_csv():

    datasets = {}

    csv_files = find_csv_files()

    if len(csv_files) == 0:

        raise FileNotFoundError(
            "No CSV files found inside data folder."
        )

    for file in csv_files:

        try:
            try:
                df = pd.read_csv(file, encoding="utf-8")
            except UnicodeDecodeError:
                df = pd.read_csv(file, encoding="latin-1")

            datasets[file] = df

        except Exception as e:

            print(f"Couldn't read {file}")

            print(e)

    return datasets


# ==========================================================
# Detect which CSV is dialogue table
# ==========================================================

def detect_dialogue_table(datasets):

    for filename, df in datasets.items():

        detected = detect_columns(df)

        if (
            (detected["character"] is not None or detected["character_id"] is not None)
            and detected["text"] is not None
        ):

            return filename

    raise Exception(
        "Couldn't find dialogue dataset."
    )


# ==========================================================
# Detect character table
# ==========================================================

def detect_character_table(datasets):

    for filename, df in datasets.items():

        columns = [c.lower() for c in df.columns]

        if (
            "character name" in columns
            or "character" in columns
        ):
            detected = detect_columns(df)
            if detected["text"] is None:
                return filename

    return None


# ==========================================================
# Load complete dataset
# ==========================================================

def load_dataset():

    datasets = load_all_csv()

    dialogue_file = detect_dialogue_table(
        datasets
    )

    dialogue_df = datasets[dialogue_file]

    character_file = detect_character_table(
        datasets
    )

    print("=" * 50)

    print("Detected Files")

    print("=" * 50)

    print(
        f"Dialogue File : {os.path.basename(dialogue_file)}"
    )

    if character_file:

        print(
            f"Character File : {os.path.basename(character_file)}"
        )

    print()

    detected = detect_columns(dialogue_df)

    print("Detected Columns")

    print("--------------------------")

    for key, value in detected.items():

        print(f"{key:<15}: {value}")

    print()

    # ----------------------------------------------------
    # Merge character names if needed
    # ----------------------------------------------------

    if (
        character_file
        and detected["character"] is None
        and detected["character_id"] is not None
    ):

        character_df = datasets[character_file]

        character_columns = detect_columns(character_df)

        if (
            character_columns["character_id"]
            and character_columns["character"]
        ):

            dialogue_df = dialogue_df.merge(

                character_df[[
                    character_columns["character_id"],
                    character_columns["character"]
                ]],

                left_on=detected["character_id"],

                right_on=character_columns["character_id"],

                how="left"

            )

    return dialogue_df