from loader import load_dataset

from conv_build import (
    build_conversations
)

from format import (
    format_dataset
)

from splitter import (
    split_dataset
)


def main():

    print("=" * 50)
    print("Loading dataset...")
    print("=" * 50)

    dialogue = load_dataset()

    print(
        f"Total dialogue rows : {len(dialogue)}"
    )

    print("=" * 50)
    print("Building conversations...")
    print("=" * 50)

    conversations = build_conversations(
        dialogue
    )

    print(
        f"Conversations extracted : {len(conversations)}"
    )

    print("=" * 50)
    print("Formatting dataset...")
    print("=" * 50)

    dataset = format_dataset(
        conversations
    )

    print(
        f"Final samples : {len(dataset)}"
    )

    print("=" * 50)
    print("Splitting dataset...")
    print("=" * 50)

    train, val, test = split_dataset(
        dataset
    )

    print()
    print("Done!")
    print()

    print(
        f"Train      : {len(train)}"
    )

    print(
        f"Validation : {len(val)}"
    )

    print(
        f"Test       : {len(test)}"
    )

    print()

    print(
        "Saved inside output/"
    )


if __name__ == "__main__":
    main()