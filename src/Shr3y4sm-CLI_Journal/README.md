# Mood & Gratitude Journal (Beginner Friendly)

A simple CLI to record your mood and one thing you're grateful for. Entries are stored in newline-delimited JSON (JSONL) for easy reading and exporting.

## Commands (PowerShell, run from repo root)

```powershell
# Add entries
python -m src.Shr3y4sm.main add happy "A great cup of coffee"
python -m src.Shr3y4sm.main add calm "Finished my workout"

# List entries (all or last N)
python -m src.Shr3y4sm.main list
python -m src.Shr3y4sm.main list -n 5

# See stats by mood
python -m src.Shr3y4sm.main stats

# Export to Markdown
python -m src.Shr3y4sm.main export journal.md
```

## Where data is stored

Entries are saved at `src/Shr3y4sm/data/journal.jsonl` within the repository.

## Why this is beginner-friendly and unique

- Focuses on practical file I/O with a human-readable format (JSONL)
- Teaches CLI argument parsing with subcommands
- Encourages daily reflection with simple stats and export features

## Requirements

- Python 3.9+; no external dependencies


