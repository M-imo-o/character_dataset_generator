# Hermione Dataset Generator

A Python utility for extracting, cleaning, formatting, and splitting dialogues from CSV source files to generate training datasets for LLM character fine-tuning.

## Project Structure

```text
HermioneDatasetGenerator/
├── data/                  # Raw dialogue and characters CSV files
├── output/                # Generated JSONL datasets (git ignored)
├── outputs/               # Source code scripts
│   ├── config.py          # Settings and path configuration
│   ├── loader.py          # CSV loader
│   ├── conv_build.py      # Conversation processing logic
│   ├── format.py          # Data cleaner and system prompter
│   ├── splitter.py        # Splitting datasets into train/val/test
│   └── main.py            # Execution entry point
├── .gitignore
└── requirements.txt
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd HermioneDatasetGenerator
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows (PowerShell):
   .\venv\Scripts\Activate.ps1
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Put your raw CSV files (`Dialogue.csv`, `Characters.csv`, `Chapters.csv`, `Places.csv`) inside the `data/` folder.
2. Edit settings in `outputs/config.py` as needed (e.g. `TARGET_CHARACTER`).
3. Run the generator script:
   ```bash
   python outputs/main.py
   ```
4. Output `.jsonl` files will be generated in the `output/` folder.
