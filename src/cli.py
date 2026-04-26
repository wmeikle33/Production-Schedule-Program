# src/production-schedule-program/cli.py
from __future__ import annotations

import json
from pathlib import Path

import typer
from rich import print
from .config import ProgramConfig
from .models import ProgramResult
from .pipeline import run_pipeline

app = typer.Typer(add_completion=False, help="Production Scheduling Program CLI")

@app.command()
def run(
    section: str = typer.Option(..., "--section", help="Autohome section to scrape"),
    pages: int = typer.Option(1, "--pages", min=1, help="Number of list pages to crawl"),
    out_dir: Path = typer.Option(Path("data/"), "--out-dir", help="Output file path"),
):
    run_pipeline
    print("[bold green]Done![/bold green]")
    print(f"Output: {out_dir.resolve()}")

    summary_path = out_dir.parent / "run_summary.json"
    summary_path.write_text(json.dumps(result.to_dict(), indent=2), encoding="utf-8")


def main():
    app()


if __name__ == "__main__":
    main()
