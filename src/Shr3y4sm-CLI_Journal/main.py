#!/usr/bin/env python3

from __future__ import annotations

"""Command-line interface for the Mood & Gratitude Journal.

This script wires up argument parsing and calls into the storage layer defined
in `journal.py`. It exposes four subcommands:

- add:   create a new entry with mood and gratitude text
- list:  show recent entries (optionally limit to last N)
- stats: print total entries and counts grouped by mood
- export: write all entries to a Markdown file
"""

import argparse
from pathlib import Path

from .journal import Journal


def get_storage_path() -> Path:
    # Store entries in a repo-local data directory to keep paths predictable
    return Path(__file__).resolve().parent / "data" / "journal.jsonl"


def build_parser() -> argparse.ArgumentParser:
    """Define top-level parser and subcommands."""
    parser = argparse.ArgumentParser(
        description="Mood & Gratitude Journal (beginner-friendly JSONL storage)",
    )

    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Add a new journal entry")
    p_add.add_argument("mood", help="Your mood (e.g., happy, calm, stressed)")
    p_add.add_argument("gratitude", help="One thing you're grateful for")

    p_list = sub.add_parser("list", help="List recent entries")
    p_list.add_argument("--limit", "-n", type=int, default=None, help="Show only the last N entries")

    sub.add_parser("stats", help="Show entry counts by mood")

    p_export = sub.add_parser("export", help="Export entries to Markdown")
    p_export.add_argument("output", type=Path, help="Output .md file path")

    return parser


def cmd_add(journal: Journal, args: argparse.Namespace) -> None:
    """Handle the `add` subcommand."""
    entry = journal.add(args.mood, args.gratitude)
    print(f"Added [{entry.timestamp}]: mood={entry.mood} | gratitude={entry.gratitude}")


def cmd_list(journal: Journal, args: argparse.Namespace) -> None:
    """Handle the `list` subcommand."""
    entries = journal.list_entries(limit=args.limit)
    if not entries:
        print("No entries yet. Use 'add' to create your first one!")
        return
    for e in entries:
        print(f"[{e.timestamp}] mood={e.mood} | gratitude={e.gratitude}")


def cmd_stats(journal: Journal, _args: argparse.Namespace) -> None:
    """Handle the `stats` subcommand."""
    s = journal.stats()
    print(f"Total entries: {s['total']}")
    for mood, count in sorted(s["by_mood"].items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"- {mood}: {count}")


def cmd_export(journal: Journal, args: argparse.Namespace) -> None:
    """Handle the `export` subcommand."""
    output = args.output
    if output.suffix.lower() != ".md":
        output = output.with_suffix(".md")
    path = journal.export_markdown(output)
    print(f"Exported to {path}")


def main() -> None:
    """Entrypoint used when called as a module: `python -m src.Shr3y4sm.main`."""
    parser = build_parser()
    args = parser.parse_args()
    journal = Journal(get_storage_path())

    if args.command == "add":
        cmd_add(journal, args)
    elif args.command == "list":
        cmd_list(journal, args)
    elif args.command == "stats":
        cmd_stats(journal, args)
    elif args.command == "export":
        cmd_export(journal, args)
    else:
        parser.error("Unknown command")


if __name__ == "__main__":
    main()


