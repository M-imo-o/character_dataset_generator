import re
from config import SYSTEM_PROMPT


def clean_text(text):
    """
    Remove stage directions and normalize whitespace.
    """

    if not isinstance(text, str):
        return ""

    # Remove (...)
    text = re.sub(r"\(.*?\)", "", text)

    # Remove [...]
    text = re.sub(r"\[.*?\]", "", text)

    # Remove extra whitespace
    text = " ".join(text.split())

    return text.strip()


def format_dataset(conversations):

    formatted = []

    seen = set()

    for conv in conversations:

        history = "\n".join(conv["history"])

        reply = clean_text(conv["reply"])

        # Skip tiny replies
        if len(reply.split()) < 3:
            continue

        item = {
            "messages": [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
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

        key = (
            history,
            reply
        )

        if key not in seen:
            formatted.append(item)
            seen.add(key)

    return formatted