import random
import json
from pathlib import Path

from config import (
    TRAIN_SPLIT,
    VALIDATION_SPLIT,
    OUTPUT_FOLDER
)


def save_jsonl(dataset, filename):

    output = Path(OUTPUT_FOLDER)

    output.mkdir(exist_ok=True)

    with open(
        output / filename,
        "w",
        encoding="utf-8"
    ) as f:

        for sample in dataset:

            f.write(
                json.dumps(
                    sample,
                    ensure_ascii=False
                ) + "\n"
            )


def split_dataset(dataset):

    random.shuffle(dataset)

    total = len(dataset)

    train_end = int(total * TRAIN_SPLIT)

    val_end = train_end + int(
        total * VALIDATION_SPLIT
    )

    train = dataset[:train_end]

    validation = dataset[
        train_end:val_end
    ]

    test = dataset[val_end:]

    save_jsonl(
        train,
        "hermione_train.jsonl"
    )

    save_jsonl(
        validation,
        "hermione_validation.jsonl"
    )

    save_jsonl(
        test,
        "hermione_test.jsonl"
    )

    return train, validation, test