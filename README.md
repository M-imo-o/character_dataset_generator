# 🎭 CharacterForge
### Universal Character Dataset Generator for LLM Fine-Tuning

CharacterForge is an open-source preprocessing toolkit that converts structured dialogue datasets (movies, TV shows, anime, games, etc.) into high-quality conversational datasets for character-specific Large Language Model (LLM) fine-tuning.

Instead of manually cleaning thousands of dialogue lines, CharacterForge automatically extracts conversations, reconstructs context, merges consecutive replies, removes noisy samples, and exports datasets in **ChatML JSONL format** compatible with **Unsloth**, **TRL**, and **Hugging Face Datasets**.

---

## ✨ Features

- 🎭 Generate datasets for **any character** from a dialogue dataset.
- 📂 Automatic CSV detection.
- 🔍 Automatic column detection (Speaker, Dialogue, Chapter, Place, etc.).
- 💬 Conversation reconstruction using previous dialogue context.
- 🔄 Merge consecutive replies from the target character.
- 📚 Preserve chapter and location boundaries.
- 🧹 Remove duplicates and stage directions.
- ✂️ Filter very short or low-quality responses.
- 📦 Export datasets in ChatML JSONL format.
- 📊 Automatic train / validation / test split.
- ⚙️ Highly configurable preprocessing pipeline.
- 🚀 Ready for fine-tuning using **Unsloth**, **TRL**, and **Hugging Face**.

---

# 📂 Project Structure

```
CharacterForge/
│
├── data/                         # Input CSV files
│
├── output/                       # Generated datasets
│
├── config.py                     # Project configuration
├── detector.py                   # Column detection
├── loader.py                     # Dataset loader
├── utils.py                      # Helper utilities
├── conversation_builder.py       # Conversation reconstruction
├── formatter.py                  # ChatML formatter
├── splitter.py                   # Dataset splitter
├── main.py                       # Main pipeline
│
├── requirements.txt
└── README.md
```

---

# 🚀 How It Works

```
Structured Dialogue Dataset
            │
            ▼
Automatic CSV Detection
            │
            ▼
Column Detection
            │
            ▼
Conversation Extraction
            │
            ▼
Cleaning Pipeline
            │
            ▼
Conversation Formatting
            │
            ▼
Dataset Splitting
            │
            ▼
ChatML JSONL Dataset
```

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/CharacterForge.git
```

Move into the project

```bash
cd CharacterForge
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 📁 Input Dataset

Place all dataset CSV files inside

```
data/
```

Example

```
data/

Dialogue.csv

Characters.csv

Places.csv

Chapters.csv

Spells.csv
```

---

# ▶️ Usage

Run

```bash
python main.py
```

The program will ask for a target character (if not specified in `config.py`).

Example

```
Enter target character:

> Hermione Granger
```

---

# 📤 Output

Generated datasets are stored in

```
output/
```

Example

```
hermione_granger_train.jsonl

hermione_granger_validation.jsonl

hermione_granger_test.jsonl
```

---

# 📄 Output Format

Each sample is exported in ChatML format.

```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are Hermione Granger. Always remain in character."
    },
    {
      "role": "user",
      "content": "Harry: Where are you?"
    },
    {
      "role": "assistant",
      "content": "I'm in the library."
    }
  ]
}
```

---

# ⚙️ Configuration

The preprocessing pipeline can be configured in

```
config.py
```

Example

```python
TARGET_CHARACTER = "Hermione Granger"

CONTEXT_WINDOW = 4

KEEP_SAME_CHAPTER = True

KEEP_SAME_PLACE = True

REMOVE_DUPLICATES = True

REMOVE_SHORT_REPLIES = True
```

---

# 🧠 Supported Datasets

CharacterForge is designed for any structured dialogue dataset, including:

- 🎬 Movie Scripts
- 📺 TV Shows
- 🎮 Video Games
- 📖 Visual Novels
- 🎌 Anime
- 📚 Books (dialogue datasets)
- 🤖 Custom dialogue datasets

---

# 🛠 Tech Stack

- Python
- Pandas
- JSON
- Regular Expressions
- ChatML
- Hugging Face Datasets
- Unsloth

---

# 🔮 Roadmap

- [x] Automatic dialogue extraction
- [x] ChatML formatting
- [x] Train/Validation/Test splitting
- [x] Automatic column detection
- [ ] Intelligent CSV detection
- [ ] Interactive character selection
- [ ] Dataset quality report
- [ ] Multi-format export (CSV, JSON, Parquet)
- [ ] GUI Interface
- [ ] Hugging Face Dataset upload support

---

# 🤝 Contributing

Contributions, feature requests, and bug reports are welcome.

If you'd like to improve CharacterForge, feel free to fork the repository and submit a pull request.

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ If you found this project useful

Please consider giving the repository a ⭐ on GitHub!