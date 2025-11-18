# Production Schedule Program

This repository is a **public, redaction-safe sample** of a production scheduling program I originally built during my time at SemiLEDs.

The original internal tool projected **future batch schedules** based on date, priority, and capacity constraints for a manufacturing line. This repo recreates the core ideas with **synthetic data and simplified logic**, without exposing any proprietary business rules or customer data.

---

## Why this exists

The real system:

- Ingested batch / work-order data from internal tools
- Applied business rules (due dates, batch size, priorities, line/tool capacity)
- Produced a projected schedule by day

Because the full codebase and rules are proprietary, this project serves as a **safe, illustrative slice** of that work:

- ✅ Demonstrates scheduling logic over realistic-looking data  
- ✅ Shows how I structure a small Python project (src/tests/sample_data, type hints, tests, etc.)  
- ❌ Does **not** contain real customer data, vendor/OCR configs, or proprietary rules

---

## Prerequesites

Python version (e.g. Python 3.11+)
OS assumptions if any (works on macOS/Linux/Windows)
Optional: Git, pip, virtualenv if you want to be very hand-holdy.

---

## What this sample demonstrates

At a high level, the sample code focuses on:

- **Reading batch data** from CSV files (see `sample_data/`)
- **Modeling batches** with attributes like due date, priority, and quantity
- **Assigning batches to future dates** based on simple capacity and priority rules
- **Producing a projected schedule** that can be inspected or saved as a table
- **Unit tests** that exercise the core scheduling logic end-to-end

This is meant to show *how* I approached the problem (project structure, data flow, algorithmic thinking), not to exactly replicate any internal tool.

---

## Repository layout

```text
.
├── src/               # Core library code for reading data and generating schedules
├── sample_data/       # Synthetic example CSVs used in tests / examples
├── tests/             # Unit tests that exercise the scheduling logic
├── .github/workflows/ # CI configuration (pytest etc.)
├── pyproject.toml     # Project metadata / build configuration
├── requirements-dev.txt
├── README.md
└── LICENSE
