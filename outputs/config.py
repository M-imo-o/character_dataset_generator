"""
=========================================================
Universal Character Dataset Generator Configuration
=========================================================
"""

import os

# ======================================================
# CHARACTER SETTINGS
# ======================================================

# Leave as None to be prompted at runtime.
# Or set a default character name.
TARGET_CHARACTER = None
# Example:
# TARGET_CHARACTER = "Hermione Granger"

# ======================================================
# CONTEXT SETTINGS
# ======================================================

# Number of previous dialogue turns to include
CONTEXT_WINDOW = 4

# Keep conversations inside the same chapter
KEEP_SAME_CHAPTER = True

# Keep conversations inside the same place/location
KEEP_SAME_PLACE = True

# ======================================================
# CLEANING SETTINGS
# ======================================================

REMOVE_STAGE_DIRECTIONS = True

REMOVE_SHORT_REPLIES = True

MIN_REPLY_WORDS = 3

REMOVE_DUPLICATES = True

# ======================================================
# DATASET SPLITS
# ======================================================

TRAIN_SPLIT = 0.80
VALIDATION_SPLIT = 0.10
TEST_SPLIT = 0.10

# ======================================================
# SYSTEM PROMPT
# ======================================================

# Automatically generated during formatting.
SYSTEM_PROMPT = None

# ======================================================
# PATHS
# ======================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_FOLDER = os.path.join(BASE_DIR, "data")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "output")

# ======================================================
# COLUMN ALIASES
# (Automatically detected by detector.py)
# ======================================================

CHARACTER_COLUMN = None
TEXT_COLUMN = None
CHARACTER_ID_COLUMN = None
CHAPTER_COLUMN = None
PLACE_COLUMN = None
DIALOGUE_ID_COLUMN = None