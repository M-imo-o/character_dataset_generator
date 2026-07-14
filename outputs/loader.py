import pandas as pd
import os

from config import DATA_FOLDER

# -------------------------------------------------------
# Reads every CSV file and joins them together
# -------------------------------------------------------

def load_dataset():

    dialogue = pd.read_csv(
        os.path.join(DATA_FOLDER, "Dialogue.csv"),
        encoding="latin1"
    )

    characters = pd.read_csv(
        os.path.join(DATA_FOLDER, "Characters.csv"),
        encoding="latin1"
    )

    chapters = pd.read_csv(
        os.path.join(DATA_FOLDER, "Chapters.csv"),
        encoding="latin1"
    )

    places = pd.read_csv(
        os.path.join(DATA_FOLDER, "Places.csv"),
        encoding="latin1"
    )

    # --------------------------------------------
    # Map Character IDs to Names
    # --------------------------------------------

    character_map = dict(
        zip(
            characters["Character ID"],
            characters["Character Name"]
        )
    )

    dialogue["Character Name"] = dialogue["Character ID"].map(character_map)

    # --------------------------------------------
    # Map Place IDs to Place Names
    # --------------------------------------------

    if "Place ID" in dialogue.columns:

        place_map = dict(
            zip(
                places["Place ID"],
                places["Place Name"]
            )
        )

        dialogue["Place Name"] = dialogue["Place ID"].map(place_map)

    # --------------------------------------------
    # Sort chronologically
    # --------------------------------------------

    dialogue = dialogue.sort_values("Dialogue ID")

    dialogue.reset_index(drop=True, inplace=True)

    return dialogue