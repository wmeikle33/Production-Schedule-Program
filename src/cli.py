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
    value_list: list = typer.Option(..., "--value_list", help="Values for Production Program"),
    date: str = typer.Option(1, "--date", help="Date"),
    new_values: list = typer.Option(..., "--value_list", help="New Values for Production Program"),
):
    print("[bold green]Done![/bold green]")


def main():
    app()


if __name__ == "__main__":
    main()
