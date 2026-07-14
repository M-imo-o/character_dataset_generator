"""
=========================================================
formatter.py

Converts extracted conversations into ChatML format
compatible with Unsloth, HuggingFace Datasets and TRL.

Author : Adhithya K
Project : Universal Character Dataset Generator
=========================================================
"""

import config

from utils import (
    count_words,
)

from detector import detect_columns


# ==========================================================
# Build System Prompt
# ==========================================================

def build_system_prompt():

    return (
        f"You are {config.TARGET_CHARACTER}. "
        f"Always remain in character. "
        f"Respond naturally as {config.TARGET_CHARACTER} would. "
        f"Never mention that you are an AI."
    )


# ==========================================================
# Format Dataset
# ==========================================================

def format_dataset(conversations):

    dataset = []

    system_prompt = build_system_prompt()

    for conversation in conversations:

        history = "\n".join(
            conversation["history"]
        )

        reply = conversation["reply"]

        # --------------------------------------------
        # Remove very short replies
        # --------------------------------------------

        if (
            config.REMOVE_SHORT_REPLIES
            and count_words(reply)
            < config.MIN_REPLY_WORDS
        ):

            continue

        sample = {

            "messages": [

                {
                    "role": "system",
                    "content": system_prompt
                },

                {
                    "role": "user",
                    "content": history
                },

                {
                    "role": "assistant",
                    "content": reply
                }

            ]
        }

        dataset.append(sample)

    return dataset