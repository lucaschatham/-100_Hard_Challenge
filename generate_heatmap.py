#!/usr/bin/env python3
"""Regenerates data/streaks_data.json into a coloured SVG heat-map."""

import json, pathlib, datetime as dt
import pandas as pd

DATA = pathlib.Path("data/streaks_data.json")

with DATA.open() as f:
    raw = json.load(f)          # raw == {"HabitA": ["2025-06-11", …], …}

# ---- build a long DataFrame of habit, date --------------------------------
rows = [
    {"habit": h, "date": d}
    for h, dates in raw.items()
    for d in dates
]
df = pd.DataFrame(rows)
df["date"] = pd.to_datetime(df["date"])

# ---- very small demo heat-map (CSV pivot) ---------------------------------
pivot = (
    df.pivot_table(index="habit", columns="date", aggfunc="size", fill_value=0)
)
pivot.to_csv("data/heatmap.csv")      # ← your real code can output SVG/PNG etc.

print("Heat-map CSV written ✓")
