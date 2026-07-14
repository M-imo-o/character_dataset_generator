from config import TARGET_CHARACTER
from config import CONTEXT_WINDOW


def build_conversations(dialogue_df):

    conversations = []

    total_rows = len(dialogue_df)

    i = 0

    while i < total_rows:

        row = dialogue_df.iloc[i]

        speaker = row["Character Name"]

        # Skip until Hermione appears
        if speaker != TARGET_CHARACTER:
            i += 1
            continue

        current_chapter = row["Chapter ID"]

        current_place = row["Place ID"]

        # ----------------------------------
        # Build user context
        # ----------------------------------

        history = []

        j = i - 1

        while (
            j >= 0
            and len(history) < CONTEXT_WINDOW
        ):

            previous = dialogue_df.iloc[j]

            # Keep only same chapter
            if previous["Chapter ID"] != current_chapter:
                break

            # Optional:
            # Keep same place

            if previous["Place ID"] != current_place:
                break

            speaker = previous["Character Name"]

            dialogue = str(previous["Dialogue"]).strip()

            history.insert(
                0,
                f"{speaker}: {dialogue}"
            )

            j -= 1

        # ----------------------------------
        # Merge Hermione replies
        # ----------------------------------

        hermione_reply = []

        while i < total_rows:

            current = dialogue_df.iloc[i]

            if current["Character Name"] != TARGET_CHARACTER:
                break

            hermione_reply.append(
                str(current["Dialogue"]).strip()
            )

            i += 1

        if len(history) == 0:
            continue

        conversations.append(
            {
                "history": history,
                "reply": " ".join(hermione_reply),
                "chapter": current_chapter,
                "place": current_place,
            }
        )

    return conversations