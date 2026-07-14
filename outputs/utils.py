"""
=========================================================
utils.py

Helper functions used throughout the project.

Author : Adhithya K
Project : Universal Character Dataset Generator
=========================================================
"""

import re


# ==========================================================
# Remove stage directions
# ==========================================================

def remove_stage_directions(text):
    """
    Removes stage directions like:
    (laughs)
    [door opens]
    <sigh>

    Parameters
    ----------
    text : str

    Returns
    -------
    str
    """

    if text is None:
        return ""

    text = str(text)

    # Remove (...)
    text = re.sub(r"\(.*?\)", "", text)

    # Remove [...]
    text = re.sub(r"\[.*?\]", "", text)

    # Remove <...>
    text = re.sub(r"<.*?>", "", text)

    return text.strip()


# ==========================================================
# Normalize whitespace
# ==========================================================

def normalize_text(text):
    """
    Removes extra spaces and line breaks.
    """

    if text is None:
        return ""

    text = str(text)

    text = text.replace("\n", " ")

    text = re.sub(r"\s+", " ", text)

    return text.strip()


# ==========================================================
# Complete cleaning pipeline
# ==========================================================

def clean_text(text):

    text = remove_stage_directions(text)

    text = normalize_text(text)

    return text


# ==========================================================
# Count words
# ==========================================================

def count_words(text):

    if text is None:
        return 0

    return len(str(text).split())


# ==========================================================
# Merge consecutive replies
# ==========================================================

def merge_replies(replies):
    """
    Converts

    [
        "Hello.",
        "How are you?",
        "Nice to meet you."
    ]

    into

    Hello. How are you? Nice to meet you.
    """

    cleaned = []

    for reply in replies:

        reply = clean_text(reply)

        if reply:

            cleaned.append(reply)

    return " ".join(cleaned)


# ==========================================================
# Remove duplicate conversations
# ==========================================================

def remove_duplicate_conversations(conversations):
    """
    Removes duplicated conversations.

    Returns
    -------
    list
    """

    unique = []

    seen = set()

    for conversation in conversations:

        key = (
            tuple(conversation["history"]),
            conversation["reply"]
        )

        if key not in seen:

            seen.add(key)

            unique.append(conversation)

    return unique


# ==========================================================
# Print section titles
# ==========================================================

def print_header(title):

    print()

    print("=" * 60)

    print(title)

    print("=" * 60)

    print()


# ==========================================================
# Safe string conversion
# ==========================================================

def safe_string(value):

    if value is None:
        return ""

    if str(value).lower() == "nan":
        return ""

    return str(value).strip()