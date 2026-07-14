"""
=========================================================
main.py

Universal Character Dataset Generator

Author : Adhithya K
=========================================================
"""

import config

from loader import load_dataset
from conv_build import build_conversations
from format import format_dataset
from splitter import save_dataset


# ==========================================================
# Welcome Screen
# ==========================================================

def welcome():

    print()
    print("=" * 60)
    print(" Universal Character Dataset Generator ")
    print("=" * 60)
    print()


# ==========================================================
# Character Selection
# ==========================================================

def get_character():

    if config.TARGET_CHARACTER is None:

        character = input(
            "Enter target character: "
        ).strip()

        config.TARGET_CHARACTER = character


# ==========================================================
# Main Pipeline
# ==========================================================

def main():

    welcome()

    get_character()

    print()

    print(f"Target Character : {config.TARGET_CHARACTER}")

    print()

    # ------------------------------------------------------
    # Load Dataset
    # ------------------------------------------------------

    print("=" * 60)
    print("Loading Dataset...")
    print("=" * 60)

    dialogue_df = load_dataset()

    print()

    print(
        f"Total Dialogue Rows : {len(dialogue_df)}"
    )

    # ------------------------------------------------------
    # Build Conversations
    # ------------------------------------------------------

    print()

    print("=" * 60)
    print("Building Conversations...")
    print("=" * 60)

    conversations = build_conversations(
        dialogue_df
    )

    print()

    print(
        f"Conversations Created : {len(conversations)}"
    )

    # ------------------------------------------------------
    # Format Dataset
    # ------------------------------------------------------

    print()

    print("=" * 60)
    print("Formatting Dataset...")
    print("=" * 60)

    dataset = format_dataset(
        conversations
    )

    print()

    print(
        f"Final Training Samples : {len(dataset)}"
    )

    # ------------------------------------------------------
    # Save Dataset
    # ------------------------------------------------------

    print()

    print("=" * 60)
    print("Saving Dataset...")
    print("=" * 60)

    save_dataset(dataset)

    # ------------------------------------------------------
    # Finished
    # ------------------------------------------------------

    print()

    print("=" * 60)
    print(" Dataset Generation Complete ")
    print("=" * 60)

    print()

    print(
        "Your dataset is ready for fine-tuning with Unsloth!"
    )

    print()


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":
    main()