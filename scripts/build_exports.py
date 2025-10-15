#!/usr/bin/env python3
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from textwrap import shorten

csv_path = Path("backlog/backlog.csv")
outdir = Path("artifacts")
outdir.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(csv_path)

# Excel export
xlsx = outdir / "backlog.xlsx"
df.to_excel(xlsx, index=False)

# PNG preview (first 12 rows)
fig, ax = plt.subplots(figsize=(12, 6))
ax.axis('off')
lines = []
lines.append("Backlog preview (first 12 rows)")
cols = list(df.columns)
lines.append(" | ".join(cols))
for i, row in df.head(12).iterrows():
    vals = [shorten(str(row[c]), width=20, placeholder="…") for c in cols]
    lines.append(" | ".join(vals))
text = "\n".join(lines)
ax.text(0.01, 0.99, text, va="top", family="monospace", fontsize=9)
png = outdir / "backlog_preview.png"
fig.savefig(png, dpi=200, bbox_inches="tight")

# PDF export using matplotlib as well
pdf = outdir / "backlog_preview.pdf"
fig.savefig(pdf, dpi=300, bbox_inches="tight")
print(str(xlsx), str(png), str(pdf))
