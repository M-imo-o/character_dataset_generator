"""
=========================================================
splitter.py

Splits the formatted dataset into train, validation
and test sets and saves them as JSONL.

Author : Adhithya K
Project : Universal Character Dataset Generator
=========================================================
"""

import os
import json
import random

import config


# ==========================================================
# Create Output Folder
# ==========================================================

def create_output_folder():

    os.makedirs(
        config.OUTPUT_FOLDER,
        exist_ok=True
    )


# ==========================================================
# Save JSONL
# ==========================================================

def save_jsonl(dataset, filename):

    path = os.path.join(
        config.OUTPUT_FOLDER,
        filename
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        for sample in dataset:

            file.write(
                json.dumps(
                    sample,
                    ensure_ascii=False
                )
            )

            file.write("\n")


# ==========================================================
# Split Dataset
# ==========================================================

def split_dataset(dataset):

    create_output_folder()

    random.shuffle(dataset)

    total = len(dataset)

    train_end = int(
        total * config.TRAIN_SPLIT
    )

    validation_end = train_end + int(
        total * config.VALIDATION_SPLIT
    )

    train = dataset[:train_end]

    validation = dataset[
        train_end:validation_end
    ]

    test = dataset[
        validation_end:
    ]

    return train, validation, test


# ==========================================================
# Save Dataset
# ==========================================================

def save_dataset(dataset):

    train, validation, test = split_dataset(dataset)

    character = (
        config.TARGET_CHARACTER
        .lower()
        .replace(" ", "_")
    )

    train_name = (
        f"{character}_train.jsonl"
    )

    validation_name = (
        f"{character}_validation.jsonl"
    )

    test_name = (
        f"{character}_test.jsonl"
    )

    save_jsonl(
        train,
        train_name
    )

    save_jsonl(
        validation,
        validation_name
    )

    save_jsonl(
        test,
        test_name
    )

    print()

    print("=" * 60)

    print("Dataset Saved Successfully")

    print("=" * 60)

    print()

    print(f"Training Samples   : {len(train)}")

    print(f"Validation Samples : {len(validation)}")

    print(f"Test Samples       : {len(test)}")

    print()

    print(
        f"Output Folder : {config.OUTPUT_FOLDER}"
    )

    print()

    print(train_name)

    print(validation_name)

    print(test_name)