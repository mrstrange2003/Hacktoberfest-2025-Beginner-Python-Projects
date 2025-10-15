from __future__ import annotations

"""Journal storage and data model.

This module defines a very small persistence layer for a Mood & Gratitude
Journal. Entries are saved to disk as newline-delimited JSON (JSONL), which is
easy to read and append to without external libraries.
"""

import json
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Iterable, List, Optional


@dataclass
class Entry:
    """A single journal entry.

    - timestamp: ISO8601 string for when the entry was created
    - mood: free-form mood label (e.g. "happy", "calm")
    - gratitude: short sentence about something you're grateful for
    """

    timestamp: str
    mood: str
    gratitude: str

    @staticmethod
    def create(mood: str, gratitude: str, when: Optional[datetime] = None) -> "Entry":
        """Factory to build a normalized Entry with current timestamp by default."""
        dt = when or datetime.now()
        return Entry(
            timestamp=dt.isoformat(timespec="seconds"),
            mood=mood.strip(),
            gratitude=gratitude.strip(),
        )


class Journal:
    """Thin wrapper around a JSONL file providing simple operations."""

    def __init__(self, storage_path: Path) -> None:
        self.storage_path = storage_path
        # Ensure the directory exists so we can append safely later
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)

    def add(self, mood: str, gratitude: str) -> Entry:
        """Append a new entry to the JSONL file and return it."""
        entry = Entry.create(mood, gratitude)
        # Write one JSON object per line so it's easy to stream later
        with self.storage_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(asdict(entry), ensure_ascii=False) + "\n")
        return entry

    def iter_entries(self) -> Iterable[Entry]:
        """Yield entries from disk lazily, one line at a time.

        If the file doesn't exist yet, yield nothing.
        """
        if not self.storage_path.exists():
            return []
        with self.storage_path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                data = json.loads(line)
                yield Entry(**data)

    def list_entries(self, limit: Optional[int] = None) -> List[Entry]:
        """Return all entries, or only the last N if limit is provided."""
        entries = list(self.iter_entries())
        if limit is not None:
            return entries[-limit:]
        return entries

    def stats(self) -> dict:
        """Compute simple counts per mood and total entries."""
        counts: dict[str, int] = {}
        total = 0
        for e in self.iter_entries():
            total += 1
            counts[e.mood] = counts.get(e.mood, 0) + 1
        return {"total": total, "by_mood": counts}

    def export_markdown(self, output_path: Path) -> Path:
        """Export all entries to a simple Markdown bullet list."""
        entries = self.list_entries()
        lines = ["# Mood & Gratitude Journal", ""]
        for e in entries:
            lines.append(f"- [{e.timestamp}] Mood: {e.mood} — Gratitude: {e.gratitude}")
        output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return output_path


