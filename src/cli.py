# src/production-schedule-program/cli.py
from __future__ import annotations

import json
from pathlib import Path

import typer
from rich import print
from .config import ProgramConfig
from .parser import parse_post
from .models import ProgramResult

app = typer.Typer(add_completion=False, help="Production Scheduling Program CLI")

@app.command()
def run(
    out_dir: Path = typer.Option(Path("data/"), "--out-dir", help="Output file path"),
):

    print("[bold green]Done![/bold green]")
    print(f"Output: {out_dir.resolve()}")

    summary_path = out_dir.parent / "run_summary.json"
    summary_path.write_text(json.dumps(result.to_dict(), indent=2), encoding="utf-8")


def main():
    app()


if __name__ == "__main__":
    main()
