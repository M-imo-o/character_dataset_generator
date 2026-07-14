"""
=========================================================
conversation_builder.py

Builds conversational training examples for the
selected character.

Author : Adhithya K
Project : Universal Character Dataset Generator
=========================================================
"""

import config

from detector import detect_columns

from utils import (
    clean_text,
    merge_replies,
    remove_duplicate_conversations,
    safe_string,
)


# ==========================================================
# Build Conversations
# ==========================================================

def build_conversations(dialogue_df):

    columns = detect_columns(dialogue_df)

    character_col = columns["character"]
    text_col = columns["text"]
    chapter_col = columns["chapter"]
    place_col = columns["place"]

    if character_col is None:
        raise Exception("Character column not detected.")

    if text_col is None:
        raise Exception("Dialogue column not detected.")

    conversations = []

    total_rows = len(dialogue_df)

    i = 0

    while i < total_rows:

        current_row = dialogue_df.iloc[i]

        speaker = safe_string(
            current_row[character_col]
        )

        # --------------------------------------------------
        # Skip until target character appears
        # --------------------------------------------------

        if speaker.lower() != config.TARGET_CHARACTER.lower():

            i += 1
            continue

        # --------------------------------------------------
        # Current metadata
        # --------------------------------------------------

        current_chapter = None
        current_place = None

        if chapter_col:
            current_chapter = current_row[chapter_col]

        if place_col:
            current_place = current_row[place_col]

        # --------------------------------------------------
        # Collect previous context
        # --------------------------------------------------

        history = []

        j = i - 1

        while (
            j >= 0
            and len(history) < config.CONTEXT_WINDOW
        ):

            previous = dialogue_df.iloc[j]

            # Stay inside chapter
            if (
                config.KEEP_SAME_CHAPTER
                and chapter_col
            ):

                if previous[chapter_col] != current_chapter:
                    break

            # Stay inside place
            if (
                config.KEEP_SAME_PLACE
                and place_col
            ):

                if previous[place_col] != current_place:
                    break

            prev_character = safe_string(
                previous[character_col]
            )

            prev_text = clean_text(
                previous[text_col]
            )

            if prev_text:

                history.insert(
                    0,
                    f"{prev_character}: {prev_text}"
                )

            j -= 1

        # --------------------------------------------------
        # Merge consecutive replies
        # --------------------------------------------------

        replies = []

        while i < total_rows:

            row = dialogue_df.iloc[i]

            speaker = safe_string(
                row[character_col]
            )

            if speaker.lower() != config.TARGET_CHARACTER.lower():
                break

            text = clean_text(
                row[text_col]
            )

            if text:
                replies.append(text)

            i += 1

        assistant_reply = merge_replies(replies)

        if len(history) == 0:
            continue

        if assistant_reply == "":
            continue

        conversations.append(
            {
                "history": history,
                "reply": assistant_reply,
                "metadata": {
                    "chapter": current_chapter,
                    "place": current_place,
                },
            }
        )

    # ------------------------------------------------------
    # Remove duplicates
    # ------------------------------------------------------

    if config.REMOVE_DUPLICATES:

        conversations = remove_duplicate_conversations(
            conversations
        )

    return conversations